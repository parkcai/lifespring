from inspect import signature
from lifespring.bucket_tools import set_database_path
from lifespring.bucket_tools import create_bucket
from lifespring.bucket_tools import list_buckets
from lifespring.bucket_tools import revalue_bucket
from lifespring.bucket_tools import archive_bucket
from lifespring.bucket_tools import dearchive_bucket
from lifespring.bucket_tools import produce_value
from lifespring.bucket_tools import consume_value
from lifespring.bucket_tools import transfer_value


set_database_path(
    # change this to your own database_path
    database_path = "D:\\Projects\\lifespring\\lifespring_data",
)
print("============ LifeSpring imported. ============")
print("Frequently-used LifeSpring APIs:")
print(f"    1. create_bucket{signature(create_bucket)}")
print(f"    2. list_buckets{signature(list_buckets)}")
print(f"    3. revalue_bucket{signature(revalue_bucket)}")
print(f"    4. archive_bucket{signature(archive_bucket)}")
print(f"    5. dearchive_bucket{signature(dearchive_bucket)}")
print(f"    6. produce_value{signature(produce_value)}")
print(f"    7. consume_value{signature(consume_value)}")
print(f"    8. transfer_value{signature(transfer_value)}")
