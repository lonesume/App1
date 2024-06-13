# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import dotenv_values

config = dotenv_values(".env")

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid = config["ACCOUNT_SID"]
auth_token = config["AUTH_TOKEN"]
from_number = config["FROM_NUMBER"]
to_number = config["TO_NUMBER"]

client = Client(account_sid, auth_token)

def send_message(body: str, media_url: str):

    message = client.messages \
        .create(
            body=body,
            from_=from_number,
            to=to_number,
            media_url=media_url
        )
    
    print(message.sid)
