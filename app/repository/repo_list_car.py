import boto3


dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("Cars")

def repo_list_car(limit: int, last_key: dict | None):
    params = {
        "Limit": limit
    }

    if last_key:
        params["ExclusiveStartKey"] = last_key

    resp = table.scan(**params)

    return {
        "items": resp.get("Items", []),
        "next_page": resp.get("LastEvaluatedKey", {}).get("car_id"),
        "count": len(resp.get("Items", []))
    }

