import json
import boto3
import os

# Initialize SES client
ses = boto3.client('ses', region_name='us-east-1')

# Your verified sender email
SENDER_EMAIL = "chennusramyasri@gmail.com"

def send_email(event, context):
    try:
        # Parse the body
        body = json.loads(event.get('body', '{}'))

        # Validate inputs
        receiver = body.get('receiver_email')
        subject = body.get('subject')
        text = body.get('body_text')

        if not receiver or not subject or not text:
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "receiver_email, subject, and body_text are required"})
            }

        # Send email via SES
        response = ses.send_email(
            Source=SENDER_EMAIL,
            Destination={"ToAddresses": [receiver]},
            Message={
                "Subject": {"Data": subject},
                "Body": {"Text": {"Data": text}}
            }
        )

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Email sent successfully"})
        }

    except ses.exceptions.MessageRejected as e:
        return {
            "statusCode": 403,
            "body": json.dumps({"message": "Email rejected", "error": str(e)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error", "error": str(e)})
        }
