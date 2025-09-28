from .lifespring import lifespring


__all__ = [
    "create_bucket",
    "revalue_bucket",
    "archive_bucket",
    "consume_value",
    "transfer_value",
]


def create_bucket(
    bucket: str,
    bucket_type: str = "account",
    note: str = "",
):
    
    pass


def revalue_bucket(
    bucket: str,
    value: float,
    value_unit: str,
    bucket_type: str = "account",
    note: str = "",
):
    
    pass


def archive_bucket(
    bucket: str,
    note: str = "",
):
    
    pass


def consume_value(
    value: float,
    value_unit: str,
    bucket: str,
    note: str = "",
):
    
    pass


def transfer_value(
    value: float,
    value_unit: str,
    source_bucket: str,
    destination_bucket: str,
    note: str = "",
):
    
    pass