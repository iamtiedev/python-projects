import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

your_email = "your@email.com"
your_password = "yourpassword"

recipient = "destination@email.com"

message = MIMEMultipart()
message["From"] = your_email
message ["To"] = recipient
message["Subject"] = "example"

body = "Insert here your text"
message.attach(MIMEText(body, "plain"))

smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.starttls()
smtp_server.login(your_email, your_password)

smtp_server.sendmail(your_email, recipient, message.as_string())
smtp_server.quit()
print("Email sent")
