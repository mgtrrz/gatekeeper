import json
import os
from urllib.parse import unquote
from urllib.parse import parse_qs
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client


def main(event, context):
    # Start our TwiML response
    resp = VoiceResponse()
    
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    new_body = parse_qs(event['body'])
    calling_number = new_body['From'][0]
    
    if calling_number == os.environ['GATE_PHONE_NUMBER']:
        print("This number is calling: " + calling_number)
        resp.play('', digits='w99')
        message = client.messages.create(
            body="Alert! Apartment gates were opened",
            from_=os.environ['TWILIO_NUMBER'],
            to=os.environ['USER_FWD_NUMBER']
        )
    else:
        print("No number or recognized number called, forwarding..")
        resp.dial(os.environ['USER_FWD_NUMBER'])


    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/xml',
        },
        'body': str(resp)
    }

if __name__ == "__main__":
    main('', '')