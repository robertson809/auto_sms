# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

import time
# # Your Account Sid and Auth Token from twilio.com/console
# # DANGER! This is insecure. See http://twil.io/secure
# # Download the helper library from https://www.twilio.com/docs/python/install
# from twilio.rest import Client
#
# # account_sid = 'ACd4c94328b42fed39f08c204322447709'
# # auth_token = 'd818d4cc4265af5f9628599bf05eeb32'
# # client = Client(account_sid, auth_token)
# client = Client()
# from_whatsapp_number='whatsapp:+14155238886'
# O_to_whatsapp_number= 'whatsapp:+17044511441'
# to_whatsapp_number='whatsapp:+19739328700'
# print('hello')
# message = client.messages.create(
#                               from_='whatsapp:+14155238886',
#                               body='if you get th',
#                               to='whatsapp:+19739328700')
# time.sleep(1)
# latest_message = client.messages(message.sid).fetch()
# print(latest_message.status)



from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC1e1e420cecc71721849eacdf47a6226d"
# Your Auth Token from twilio.com/console
auth_token  = "2cb63e36a3458ab86eac7cae35403b5a"

client = Client(account_sid,auth_token)
s_number = 'whatsapp:+17044929850'
my_number = 'whatsapp:+19739328700'
O_number = "whatsapp:+17044511411"
p_number = "whatsapp:+16177747415"

from_number = '+19893421996'
message = client.messages.create(
    to=p_number,
    from_="whatsapp:+14155238886",
    body="Hello World!")

time.sleep(1)
latest_message = client.messages(message.sid).fetch()
print('message {}, recipient {}'.format(latest_message.status,
                        latest_message.to))
