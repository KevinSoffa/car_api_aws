from decimal import Decimal
import boto3


dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("Cars")


def repo_update_car(car_id: str, fields: dict):

    update_expression = "SET "
    expression_attribute_values = {}
    expression_attribute_names = {}
    updates = []

    for key, value in fields.items():

        # CONVERSÃO OBRIGATÓRIA
        if isinstance(value, float):
            value = Decimal(str(value))

        updates.append(f"#{key} = :{key}")
        expression_attribute_names[f"#{key}"] = key
        expression_attribute_values[f":{key}"] = value

    update_expression += ", ".join(updates)

    response = table.update_item(
        Key={"car_id": car_id},
        UpdateExpression=update_expression,
        ExpressionAttributeNames=expression_attribute_names,
        ExpressionAttributeValues=expression_attribute_values,
        ReturnValues="ALL_NEW"
    )

    return response["Attributes"]
