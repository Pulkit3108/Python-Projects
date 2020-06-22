import smtplib, ssl

# Ignore SSL certificate errors 
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email =  input("Enter Sender Email Address : ") 
receiver_email = input("Enter Reciever Email Address : ")   
password = input("Enter Password : ")
message = input("Enter Your Message : ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

print("Success !!!")
