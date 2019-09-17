import datetime
import imaplib

m = imaplib.IMAP4_SSL("imap.gmail.com")  # server to connect to

print("Connecting to mailbox...")
email= input("Enter your gmail: ")
pwd= input("Enter your password: ")
m.login(email, pwd)

#This block empties trash, remove if you want to keep, Gmail auto purges trash after 30 days.
print("Emptying Trash & Expunge...")
m.select('[Gmail]/Trash')  # select all trash
m.store("1:*", '+FLAGS', '\\Deleted')  #Flag all Trash as Deleted
m.expunge()  # not need if auto-expunge enabled

#This block empties spam, remove if you want to keep, Gmail auto purges spam after 30 days.
print("Emptying Spam & Expunge...")
m.select('[Gmail]/Spam')  # select all spam
m.store("1:*", '+FLAGS', '\\Deleted')  #Flag all Spam as Deleted
m.expunge()  # not needed if auto-expunge enabled

print("Done. Closing connection & logging out.")
m.close()
m.logout()
print("All Done.")