import fsspec
from astropy.table import Table


def table_from_s3(s3_uri, **kwargs):
    """
    Load a parquet file from S3 and return it as an astropy Table.

    parameters
    ----------
    s3_uri : str
        The URI to the parquet file in S3.
    **kwargs : dict
        Additional keyword arguments to pass to the astropy Table.read function.
        The possible values are documented in `Astropy Table
        <https://docs.astropy.org/en/stable/table/>`

    returns
    -------
    astropy.table.Table
        The loaded table.
    """
    fsspec_filesystem = fsspec.filesystem(protocol='s3', anon=True)
    file_stream = fsspec_filesystem.open(s3_uri)

    return Table.read(file_stream, **kwargs)
