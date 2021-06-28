import os
import datetime
from twilio.rest import Client


class SMSMessage:
    """
    This class represents the message to be sent via Twilio.
    """

    def __init__(self, body: str = ""):
        # Set SMS body text
        if not body:
            self.body = f"Test message. Timestamp: {datetime.datetime.now()}"
        else:
            self.body = body

        # Get Twilio credentials from env variables
        self.account_sid: str = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token: str = os.getenv("TWILIO_AUTH_TOKEN")

        # Set to and from numbers.
        self.to_number: str = os.getenv("TWILIO_TO_NUMBER")
        self.from_number: str = os.getenv("TWILIO_FROM_NUMBER")

        self.sid = None  # Will be set upon successful sending of the message

    def send(self) -> str:
        """
        Makes an API call to the Twilio API via the twilio helper library. Returns the message SID.
        """
        client = Client(self.account_sid, self.auth_token)

        # Submit the message to the Twilio API. This is the point where the SMS is actually sent
        message = client.messages.create(
            body=self.body, from_=self.from_number, to=self.to_number
        )

        # Twilio returns a SID which is a unique reference for a successfully sent SMS
        self.sid: str = message.sid

        return self.sid


x = SMSMessage()
sid = x.send()
print()
