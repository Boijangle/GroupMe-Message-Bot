import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask
from flask import request
app = Flask(__name__)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bot_id = os.environ.get("BOT_ID")

def post_Text(user_Text):
    requests.post('https://api.groupme.com/v3/bots/post', params = {'bot_id' : bot_id, 'text' : user_Text})

@app.route('/callback', methods=['POST'])
def parse_messages():
    print("FrickleFrackle")
    message = request.get_json()
    print(message)
    if message['sender_type'] != "user":
        print("not a user")
        return 'OK'
    if "bupd" in message['text'].lower():
        print("JLaw test")
        post_Text("JOHNNY LAW")
    if "Hi" in message['text']:
        print("hi xyz test")
        post_Text("Hi " + message['name'].split(" ")[0] + "!")
    return 'OK'
