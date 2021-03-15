from flask import Flask, request
import requests
import json
import giphy_client
from giphy_client.rest import ApiException
import random
############## Bot details ##############

bot_name = 'lilbot@webex.bot'
roomId = 'your room ID'
token = 'My personal bot token'
header = {"content-type": "application/json; charset=utf-8", 
          "authorization": "Bearer " + token}

############## Flask Application ##############
app = Flask(__name__)
api_instance = giphy_client.DefaultApi()

def search_gifs(keyword):
    try:
        response = api_instance.gifs_search_get('UFuEWhLXRTBCKSAOAToPjDR9kSsmzwJX', keyword, limit=3, rating='g')
        lst = list(response.data)
        gif = random.choices(lst)
        return gif[0].id 

    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

@app.route("/", methods=["GET", "POST"])
def sendMessage():
    webhook = request.json
    url = 'https://webexapis.com/v1/messages'
    msg = {"roomId": webhook["data"]["roomId"]}
    
    sender = webhook["data"]["personEmail"]
    message = getMessage()
    gif_command = message.partition("Gif")
    if (sender != bot_name):
       
        if(gif_command[1] == "Gif"):
            
            if (gif_command[2] != None):
                
                gif = search_gifs(gif_command[2])
                
                msg['files'] = ["https://media.giphy.com/media/"+gif+"/giphy.gif"]
                                      
            requests.post(url,data=json.dumps(msg), headers=header, verify=True) #

def getMessage():
    webhook = request.json
    url = 'https://webexapis.com/v1/messages/' + webhook["data"]["id"]
    get_msgs = requests.get(url, headers=header, verify=True)
    message = get_msgs.json()['text']
    return message

app.run(debug = True)
