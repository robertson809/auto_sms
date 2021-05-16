# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

# account_sid = 'ACd4c94328b42fed39f08c204322447709'
# auth_token = 'd818d4cc4265af5f9628599bf05eeb32'
# client = Client(account_sid, auth_token)
client = Client()
from_whatsapp_number='k'
to_whatsapp_number ='whatsapp:+19739328700'
O_number = "+17044511411"
message = client.messages.create(
                              from_="whatsapp:+14155238886",
                              body='tell me if you get this--Michael',
                              to=to_whatsapp_number)
print(message.sid)
time.sleep(2)
latest_message = client.messages(message.sid).fetch()

