import os
from flask import Flask, request, redirect
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route("/responding", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()
    body = request.values.get('Body', None)
    print(body)
    # print(request.values)
    who_from = request.values.get('From', None)
    cleaned_who_from = who_from[who_from.index(':')+1:]
    resp.message('This message was sent from {}'.format(cleaned_who_from))
    # resp.message('Thanks for messaging!')
    storage_file = open('sandbox_output.txt', 'a')
    if cleaned_who_from != '+19739328700':
        storage_file.write(cleaned_who_from + '\n')
    else:
        resp.message('Your number was not recorded because you are Michael')
    # Spamming not that hard?
    # for i in range(10):
    #     resp.message("Thanks for messaging, (now it's time to subscribe {})".format(i+2))
    resp.message('I heard you like west world')
    # print(type(request.values.get('From', None)))
    # print(type(str(resp)), 'is the type, but its an XML string, \
    #                        so dont do it urself')
    # print(str(resp))
    # return 'This message was sent from yo moma dick {}'.format(cleaned_who_from)
    return str(resp)

if __name__=="__main__":
    app.run(debug=True)