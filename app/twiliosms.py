import twilio
import twilio.rest
from twilio.rest import TwilioRestClient
import capitalData


account_sid = "ACc21fbf5413690aa9b013780eb73c722d"
auth_token = "7e1b5aafb00d3bfa211a7a3fa7707e92"
twilio_number = "4106566222"

def send_message():
	name = capitalData.get_Name()
	current_balance = capitalData.get_Balance()
	desired_balance = 
	desired_item = 
	send_number = "4436949031"
	if (current_balance >= desired_balance)
		message_to_send = "Hello " + name + ", you now have enough money to buy " + desired_item + " yay!!"
	client = TwilioRestClient(account_sid, auth_token)
 	message = client.messages.create(body=message_to_send,
    to=send_number,    # your phone number
    from_= twilio_number) # your Twilio number
	print message.sid


send_message()