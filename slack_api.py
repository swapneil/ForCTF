from slacker import Slacker
import base64

slack_api_token_base64= "eG94cC04NTQzMDMxNDIwNTUtODU0MzAzMTQyOTUxLTg1NTM1MzgwNzA2Mi0yMDY5YTU0M2I1MjQ1MjBkOTBiMmEzMjEwOTNjMDY3Mg=="
slack_api_token= base64.b64decode(slack_api_token_base64)
slack = Slacker(slack_api_token)
#something try
#kya hai haa
if slack.api.test().successful:
    print(
        f"Connected to {slack.team.info().body['team']['name']}.")
else:
    print('Try Again!')

r = slack.channels.list()
channels = r.body
# Iterate through channels
for c in channels['channels']:
    print(f'Channel {c["name"]} Purpose: {c["purpose"]["value"]}')
