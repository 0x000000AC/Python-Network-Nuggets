# Python 3

# Communicating with SMTP servers, mime not used here, but could be
# to just send the message or if you needed to include attachements

import smtplib

# x.x.x.x would be your local mail server running
s = smtplib.SMTP("X.X.X.X", 25)
#s.login("user", "password")

try
	m = "\nThis is message"
	# source address, destination address, message
	s.sendmail("aapclark@gmail.com", "apoh@outlook.com", m)
	print ("Finished sending message")
except Exception as e:
	print("Unable to send message: ", e)

s.quit()
