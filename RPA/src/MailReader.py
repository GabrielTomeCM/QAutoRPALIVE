from imbox import Imbox
import time
import datetime as dt

# SSL Context docs https://docs.python.org/2/library/ssl.html#ssl.create_default_context

def get_messages():
	with Imbox(
	   'imap.gmail.com',
		username="qautomail",
		password="Codemen1234",
		ssl=True,
		ssl_context=None,
		starttls=False
		) as imbox:
				
			
		messages = imbox.messages(date__gt=dt.datetime.now(), sent_from='gabriel.tome@codemen.fi')
		for uid, message in messages:			
			msg_flags = str (message.flags)
			print(dt.datetime.now())
			print(str(message.date))
			print(str(uid))
			if not msg_flags.find("Seen"):								
				imbox.mark_seen(uid)
				handle_message(uid, message)
			else:
				print ("Awesome!")
				#imbox.delete(uid) 
				

def handle_message(uid, message):
	#print (uid, message.body)
	print(message.keys())
	print(str(message.flags))
	print("Sender: " + str(message.sent_from[0]["name"]) + 
		" Sent on:" + str(message.date) + 
		" Message body: " + str(message.body["plain"]))


get_messages()