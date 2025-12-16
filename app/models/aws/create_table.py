import boto3


# ----------------------------
# CRIACAO DO DB NA AWS
#-----------------------------
dynamodb = boto3.client("dynamodb", region_name="us-east-1")
table_name = "Cars"

response = dynamodb.create_table(
    TableName=table_name,
    AttributeDefinitions=[
        {"AttributeName": "car_id", "AttributeType": "S"},
    ],
    KeySchema=[
        {"AttributeName": "car_id", "KeyType": "HASH"},
    ],
    BillingMode="PAY_PER_REQUEST",
)

print("Tabela criada com sucesso:", response)
