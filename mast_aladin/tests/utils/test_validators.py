import mast_aladin.utils.validators as validators


class TestUtils:
    def test_is_valid_s3_uri(self):
        # Arrange
        uri = "s3://my-bucket/my-file.parquet"
        # Act
        result = validators.is_valid_s3_uri(uri)
        # Assert
        assert result is True

    def test_non_s3_uri(self):
        # Arrange
        uri = "http://my-bucket/my-file.parquet"
        # Act
        result = validators.is_valid_s3_uri(uri)
        # Assert
        assert result is False

    def test_file_in_not_s3_uri(self):
        # Arrange
        uri = "file:///path/to/my-file.parquet"
        # Act
        result = validators.is_valid_s3_uri(uri)
        # Assert
        assert result is False
