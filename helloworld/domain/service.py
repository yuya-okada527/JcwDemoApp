from typing import List

from helloworld.domain.models import WorkBook
from helloworld.infra.s3 import S3Client


WORKBOOK_PREFIX = "materials/workbooks"


def get_workbooks() -> List[WorkBook]:
    workbook_objects = S3Client.list_objects(WORKBOOK_PREFIX)
    workbook_keys = [obj.key for obj in workbook_objects]
    return [WorkBook(key, key.split("/")[-1]) for key in workbook_keys if not key.endswith("/")]


def get_workbook(key: str):
    workbook_object = S3Client.get_object(key)
    return workbook_object.get()["Body"].read()

