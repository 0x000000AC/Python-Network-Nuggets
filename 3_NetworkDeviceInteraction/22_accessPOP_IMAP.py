#Python 3
# If you've sent an SMTP message, you probably want
# to retrieve it.  Shows POP3 / IMAP 4

#pop/imap library 
import poplib, imaplib, getpass

# greating instance of pop3, mail server on local network 110 default port
p = poplib.POP3("x.x.x.x", 110)

# could do ssl/pop together
# p = poplib.POP3_SSL("x.x.x.x", 995)

#get the banner it gives you, then login
print(p.getwelcome()
p.user("USER")
p.pass_("PASSWORD")

# List all messages on server
print(p.list())
p.quit()

# instance of imap4 object.  diff than pop3, pop3 designed for local mail
# imap expects messages will be on server, client retrieves as necessary
i = imaplib.IMAP4("x.x.x.x", 143)

# could use getpass here, but don't
# i.login(getpass.getuser(), getpass.getpass_())

# select the mailbox you're using
i.select()
t, l = i.list()
print("Response code: ", t)
print (l)

# could search for certian things, but want all here
t, ids = i.search(None, "ALL")
print("Response code: ", t)

# get message ids, in this case just get '1'
print(ids)

# getting message body in text form
t, msg = i.fetch('1', "(UID BODY[TEXT])")
# store messages on the server
# i.store()
print(msg)
i.close()
i.logout()
