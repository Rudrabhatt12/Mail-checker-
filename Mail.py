import imaplib 
import email

imap_server = "imap.gmail.com"
email_address = input("What is your gmail: ")
password = input("What is your passowrd (use your app password): ")

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")


_, msgnums = imap.search(None, "ALL")


for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")

    message = email.message_from_bytes(data[0][1])

    print(f"Message Number:  {msgnum}")
    print(f"From: {message.get('From')}")
    print(f"From: {message.get('To')}")
    print(f"From: {message.get('BCC')}")
    print(f"From: {message.get('Date')}")
    print(f"From: {message.get('Subject')}")

    print("content: ")
    for part in message.walk():
        if part.get_content_type() == "text/plain": 
            print(part.as_string())

imap.close()




