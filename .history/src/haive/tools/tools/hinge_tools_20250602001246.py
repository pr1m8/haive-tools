from squeaky_hinge import HingeAPI

# Initialize client
api = HingeAPI()

# Login (requires manual SMS verification)
api.login(phone_number="+15555555555")

# Fetch messages
conversations = api.fetch_messages()

# Send message
# api.send_message(user_id="USER_ID", text="Hello from Python!")
