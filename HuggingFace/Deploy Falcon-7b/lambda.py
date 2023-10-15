import json
import os 
import boto3

ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    try:
        print("Received event:" + json.dumps(event))

        if 'body' in event:
            # Check if the event has a 'body' field (API Gateway format)
            event_body = json.loads(event['body'])
        else:
            event_body = event

        payload = json.dumps(event_body)

        # Invoke the SageMaker endpoint and get the inference response
        response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                           ContentType='application/json',
                                           Body=bytes(payload, 'utf-8'))
        print(response) 
        
        # Parse the JSON response 
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            result = json.loads(response['Body'].read().decode())
            print(result)
            return {
                "statusCode": 200,
                "body": json.dumps(result)
            }
        else:
            # Handle non-200 status codes here
            error_message = f"Endpoint returned a non-200 status code: {response['ResponseMetadata']['HTTPStatusCode']}"
            print(error_message)
            return {
                "statusCode": response['ResponseMetadata']['HTTPStatusCode'],
                "body": error_message
            }

    except Exception as e:
        # Handle exceptions here
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        return {
            "statusCode": 500,  # Internal Server Error
            "body": error_message
        }

