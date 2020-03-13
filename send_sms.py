from twilio.rest import Client

account_sid = 'enter account sid'
auth_token = 'enter auth token'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Alert. Intruder!",
                     from_='ENTER SENDER NO',
		     media_url=[ENTER MEDIA LINK],
                     to='ENTER RECEIVER NO'
                 )

print(message.sid)

