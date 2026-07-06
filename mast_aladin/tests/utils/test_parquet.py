import pytest
from unittest.mock import Mock, patch
from pathlib import Path
import io
from astropy.table import Table

from mast_aladin.utils.parquet import table_from_parquet_s3

TEST_PARQUET_PATH = Path(__file__).parent / 'r0034201001001001001_0001_wfi01_f087_cat.parquet'
TEST_S3_PATH = 's3://some-bucket/r0034201001001001001_0001_wfi01_f087_cat.parquet'


def _load_test_parquet_bytes():
    """Load parquet file bytes once at module level."""
    with open(TEST_PARQUET_PATH, 'rb') as f:
        return f.read()


TEST_PARQUET_BYTES = _load_test_parquet_bytes()


@pytest.fixture
def mock_s3_filesystem():
    """Fixture that provides a mock S3 filesystem with test parquet data."""
    with patch('mast_aladin.utils.parquet.fsspec.filesystem') as mock_filesystem:
        mock_fs = Mock()
        mock_filesystem.return_value = mock_fs
        file_like_object = io.BytesIO(TEST_PARQUET_BYTES)
        mock_fs.open.return_value = file_like_object
        yield mock_filesystem, mock_fs


class TestTableFromParquetS3:
    def test_table_from_parquet_s3(self, mock_s3_filesystem):
        """Test loading a parquet file from S3 using local file mock."""
        mock_filesystem, mock_fs = mock_s3_filesystem
        s3_path = TEST_S3_PATH

        # Call the function
        result = table_from_parquet_s3(s3_path)

        # Verify it returns an astropy Table
        assert isinstance(result, Table)
        assert len(result) > 0

        # Verify the filesystem was called correctly
        mock_filesystem.assert_called_once_with(protocol='s3', anon=True)
        mock_fs.open.assert_called_once_with(s3_path)

    def test_table_from_parquet_s3_with_kwargs(self, mock_s3_filesystem):
        """Test that kwargs are passed to astropy.Table.read."""
        mock_filesystem, mock_fs = mock_s3_filesystem
        s3_path = TEST_S3_PATH
        test_kwargs = {'include_names': ['ra', 'dec']}

        # Call the function with kwargs
        result = table_from_parquet_s3(s3_path, **test_kwargs)

        # Verify kwargs were passed to open
        assert isinstance(result, Table)
        assert result.colnames == ['ra', 'dec']
        mock_fs.open.assert_called_once_with(s3_path, **test_kwargs)
