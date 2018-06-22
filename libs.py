import requests
import time
from database import get_user_id, check_silenced

def post_text(user_text, bot_id):
    time.sleep(1)
    if len(user_text.strip()) == 0:
        raise ValueError("Can't post empty message")
    if(not check_silenced(bot_id)[0]):
        requests.post('https://api.groupme.com/v3/bots/post', params = {'bot_id' : bot_id, 'text' : user_text}).raise_for_status()

def post_text_mention(user_text, bot_id, mention_id):
    time.sleep(1)
    if len(user_text.strip()) == 0:
        raise ValueError("Can't post empty message")
    print("User id: " + mention_id)

    payload = {
      'text': user_text,
      'bot_id': bot_id,
      'attachments': [{ 'loci': [[0,0]], 'type': "mentions", 'user_ids': [mention_id] }]
    };

    requests.post('https://api.groupme.com/v3/bots/post', json=payload).raise_for_status()
