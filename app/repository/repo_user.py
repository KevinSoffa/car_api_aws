import boto3


dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("Users")

# Pegando usuários no DynamoDB [ AWS ]
def get_user_by_email(email: str):
    response = table.get_item(
        Key={"email": email}
    )
    return response.get("Item")
