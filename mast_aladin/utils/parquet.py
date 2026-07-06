import fsspec
from astropy.table import Table


def table_from_parquet_s3(file_path, **kwargs):
    """
    Load a parquet file from S3 and return it as an astropy Table.

    parameters
    ----------
    file_path : str
        The path to the parquet file in S3.
    **kwargs : dict
        Additional keyword arguments to pass to the astropy Table.read function.

    returns
    -------
    astropy.table.Table
        The loaded table.
    """
    fsspec_filesystem = fsspec.filesystem(protocol='s3', anon=True)
    file_stream = fsspec_filesystem.open(file_path)

    return Table.read(file_stream, **kwargs)
