import boto3
import json

client = boto3.client("bedrock-runtime", region_name="ap-south-1")

response = client.converse(
    modelId="apac.amazon.nova-pro-v1:0",
    messages=[
        {
            "role": "user",
            "content": [{"text": "Hello, Nova Pro!"}]
        }
    ]
)

print(response["output"]["message"]["content"][0]["text"])
