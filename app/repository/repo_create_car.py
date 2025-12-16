from app.models.car_dao import CarDAO
import boto3
import uuid


dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("Cars")


def repo_create_car(dao: CarDAO):
    dao.car_id = str(uuid.uuid4())
    table.put_item(Item=dao.__dict__)
    return dao
