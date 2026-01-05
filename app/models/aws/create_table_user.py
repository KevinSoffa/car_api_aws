import boto3

# ----------------------------
# CRIAÇÃO DA TABELA USERS
# ----------------------------
dynamodb = boto3.client("dynamodb", region_name="us-east-1")

table_name = "Users"

response = dynamodb.create_table(
    TableName=table_name,
    AttributeDefinitions=[
        {"AttributeName": "email", "AttributeType": "S"},
    ],
    KeySchema=[
        {"AttributeName": "email", "KeyType": "HASH"},
    ],
    BillingMode="PAY_PER_REQUEST",
)

print("Tabela criada com sucesso:", response)
