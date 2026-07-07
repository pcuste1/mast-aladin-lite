from mast_aladin.app import MastAladin, gca
from unittest.mock import Mock, patch
from astropy.table import Table
import pytest


def test_current_app(MastAladin_app):
    # MastAladin_app should be the current instance of the app
    assert gca() == MastAladin_app

    # create new app instance
    instance2 = MastAladin()

    # gca should refer to the newly instantiated app:
    assert gca() == instance2


@patch("mast_aladin.utils.parquet.table_from_s3")
def test_add_astropy_table(mock_table_from_s3, MastAladin_app):
    """Test loading an astropy table."""
    # Arrange
    table = Table()

    # Act
    result = MastAladin_app.add_table(table)

    # Assert
    mock_table_from_s3.assert_not_called()
    assert result["type"] == "table"


@patch("mast_aladin.utils.parquet.table_from_s3")
def test_add_parquet_table(mock_table_from_s3, MastAladin_app):
    """Test loading a parquet table."""
    # Arrange
    mock_table = Table()
    mock_table_from_s3.return_value = mock_table
    parquet_uri = "s3://some-bucket/test.parquet"

    # Act
    result = MastAladin_app.add_table(parquet_uri)
    print(result)
    # Assert
    mock_table_from_s3.assert_called_once_with(parquet_uri)
    assert result["type"] == "table"


@patch("mast_aladin.utils.parquet.table_from_s3")
def test_add_invalid_table(mock_table_from_s3, MastAladin_app):
    """Test loading a parquet table."""
    # Arrange
    mock_table = Mock()
    mock_table_from_s3.return_value = mock_table
    parquet_uri = "https://some-bucket/test.parquet"

    # Act/Assert
    with pytest.raises(ValueError):
        MastAladin_app.add_table(parquet_uri)

    # Assert
    mock_table_from_s3.assert_not_called()
