# slack

from slack import WebClient
from datetime import datetime

# Initialize the Slack API client with your OAuth token
slack_token = os.environ["SOME_SECRET"]
client = WebClient(token=slack_token)

# Define the channel and the message you want to send
channel = "#rsi_lower_30"  # Replace with the name of your channel or its ID
message = f"Hello, Goldhand!{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Send the message to the specified channel
response = client.chat_postMessage(channel=channel, text=message)

# Check if the message was sent successfully
if response["ok"]:
    print(f"Message sent to {channel}: {message}")
else:
    print(f"Failed to send the message: {response['error']}")