import boto3


dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("Cars")

def repo_delete_car(car_id: str):
    table.delete_item(Key={"car_id": car_id})
    return {"message": "Car deleted"}
