# slack

from slack import WebClient
from datetime import datetime
import os

# Initialize the Slack API client with your OAuth token
slack_token = os.environ["SLACK_TOKEN"]
client = WebClient(token=slack_token)

# Define the channel and the message you want to send
channel = "#rsi_lower_30"  # Replace with the name of your channel or its ID
message = f"Hello, Goldhand!{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n {os.getcwd()}\n {os.listdir('/home/')}"

# Send the message to the specified channel
response = client.chat_postMessage(channel=channel, text=message)

# Check if the message was sent successfully
if response["ok"]:
    print(f"Message sent to {channel}: {message}")
else:
    print(f"Failed to send the message: {response['error']}")
    
    
import pandas as pd
import os
tw = Tw()
tw.stock.to_csv(f"{os.getcwd()}/data/{datetime.now().strftime('stock_%Y_%m_%d_%H_%M_%S')}.csv", index=False)
