#!/usr/bin/python3
# Example: ./sendmail.py '{"justin":"sanderson", "key":"value", "key2":"value2"}'

import sys
import smtplib
from email.message import EmailMessage
import ssl
import json

# 1. Check if an argument was passed
if len(sys.argv) < 2:
    print("Error: Missing JSON argument.")
    print("Usage: python script.py '<json_string>'")
    sys.exit(1)

# 2. Parse the CLI string argument into JSON data
try:
    raw_json_string = sys.argv[1]
    incoming_json_data = json.loads(raw_json_string)
except Exception as e:
    print(f"Error: Invalid JSON string provided. Details: {e}")
    sys.exit(1)

# 3. Format the JSON data into a clean string for the email body
email_body = json.dumps(incoming_json_data, indent=4)

# Define Gmail details
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "justin.sanderson104@gmail.com"
# Paste the 16-character App Password here (without spaces)
SENDER_PASSWORD = ""
RECIPIENT_EMAIL = "15558675309@mypixmessages.com"

# Create message
msg = EmailMessage()
msg["Subject"] = "TRADINGVIEW ALERT"
msg["From"] = SENDER_EMAIL
msg["To"] = RECIPIENT_EMAIL
msg.set_content(email_body)


# Create a secure SSL context
print("Attempting ssl connection to google mail servers")
context = ssl.create_default_context()

try:
    # Connect using explicit TLS/STARTTLS
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls(context=context)
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    print("Email sent successfully through Gmail!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()

