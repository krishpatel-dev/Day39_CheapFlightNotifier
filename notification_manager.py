import os
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.getenv("TWILIO_VIRTUAL_NUMBER"),
            body=message_body,
            to=os.getenv("TWILIO_VERIFIED_NUMBER")
        )
        # Prints if successfully sent.
        print(message.sid)
        print(message.status)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.getenv("TWILIO_WHATSAPP_NUMBER")}',
            body=message_body,
            to=f'whatsapp:{os.getenv("TWILIO_VERIFIED_NUMBER")}'
        )
        print(message.sid)
        print(message.status)