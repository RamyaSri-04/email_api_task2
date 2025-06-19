# 📧 Serverless Email Sender API (Python + AWS SES)

This project demonstrates how to create a REST API using the **Serverless Framework** and **AWS Lambda** (Python runtime). The API allows users to send emails via **AWS Simple Email Service (SES)** by submitting `receiver_email`, `subject`, and `body_text`.

---

## 🌐 Live Endpoint

endpoint: POST - https://mv09et7srg.execute-api.us-east-1.amazonaws.com/dev/send-email

## 📁 Project Structure
emailapi/
├── handler.py # Lambda function for sending email
├── serverless.yml # Configuration for Serverless Framework
├── email_form.html # Optional: HTML frontend to submit form
└── README.md # Project documentation


---

## 🔧 How It Works

1. User submits `receiver_email`, `subject`, and `body_text`.
2. Lambda function uses AWS SES to send the email.
3. Returns:
   - `200 OK` on success
   - `400 Bad Request` if fields are missing
   - `403 Forbidden` if SES rejects the email (e.g., unverified email)
   - `500 Internal Server Error` for general exceptions

---

## 🧪 How to Test

### ✅ Test with Postman

**URL**:  
https://mv09et7srg.execute-api.us-east-1.amazonaws.com/dev/send-email


**Method**: `POST`

**Headers**:
#### Content-Type: application/json


**Body (raw JSON)**:
```json
{
  "receiver_email": "test@example.com",
  "subject": "Hello!",
  "body_text": "This is a test email sent using Serverless + AWS SES."
}

```
## 🛠️ Deploy Instructions ##

1. Navigate to project folder - cd emailapi

2. Deploy to AWS using Serverless - serverless deploy

## 🧰 Built With ##

Serverless Framework

AWS Lambda

AWS SES

Python 3.10+

## 👤 Author

Chennu Ramya Sri
GitHub: github.com/RamyaSri-04

## 📄 License ##


---

Let me know if you want me to update this with your actual name, GitHub username, or endpoint.
