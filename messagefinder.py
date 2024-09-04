import requests
import json
headers = {
  
}

def return_msg(channel_id ,msg_count):
    
    messages = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=1",headers=headers).json()
    # print(messages[0]['content'])
    return messages[0]['content']
    # print(messages)