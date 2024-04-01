from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Retrieve message details
message_id = 'SMe7c21571d9cad5aebfa8bdd6cb9192c0'
message = client.messages(message_id).fetch()

# Print message details
print("Message SID:", message.sid)
print("Status:", message.status)
print("Body:", message.body)
print("From:", message.from_)
print("To:", message.to)
