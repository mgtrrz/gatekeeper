# Gatekeeper

A serverless Python lambda script to open gates.

## How this works

The apartments I live at use a tele-entry box for entry. A guest enters a code that then dials my phone. When I answer, I can talk to the person at the gate and dial the number 9 on my phone to command the system to open the gates.

I don't always have my cell phone around with me to answer it if I have a guests or food delivery/packages. Therefore, the script is set up to answer requests from Twilio.

I registered a number with Twilio that I then gave to the apartment community. When the tele-entry boxes calls the Twilio number, it makes an API request to the Lambda script which then decides what to do with the request. If we recognize the number that's calling as being from the tele-entry box, we just send the 9 dial tone command so the gates open up automatically. It also sends me a text that the apartment gates were opened. If we receive a call from any other number, it forwards to my phone.

## Requirements

Uses https://serverless.com/blog/serverless-python-packaging/ for local development. 

This is also based on a much simpler version of: https://blog.expo.io/how-to-never-miss-or-even-answer-a-buzzer-call-from-friends-ever-again-1-2-ad90144030c4

There's no additional verification or security measures in this system, but I may look into adding it without using Facebook.