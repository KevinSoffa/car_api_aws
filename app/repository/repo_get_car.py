import boto3


dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("Cars")


def repo_get_car(car_id: str):
    response = table.get_item(Key={"car_id": car_id})
    return response.get("Item")
