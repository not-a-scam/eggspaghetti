import requests
import json
import time
import random
import urllib
import os
import re
from emoji import emojize


"""
def telegram_bot_sendtext(bot_message):
    bot_token = '975642105:AAHJWLnTfxmLt8fr1giBI0yMsUy3aP0jBm4'
    bot_chatID = '473042816'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

test = telegram_bot_sendtext("Testing Telegram bot")
print(test)

"""
cool = emojize(':cool:',use_aliases = True)
bigSick = emojize(':face_vomiting:', use_aliases = True)
sick = emojize(':nauseated_face:', use_aliases = True)
moon = emojize(':new_moon_with_face:', use_aliases = True)
skull = emojize(':skull:',use_aliases = True)
com = [cool+cool+cool,'you are extremely cool', 'you are very extremely cool', 'wow what a cool guy', 'u r cool', 'you are big cool', 'stay cool','have i ever told you that u r cool','u r cool kid']
no = [bigSick,sick,skull,'go away big gay', 'stop talking to me', 'u r ew', 'u not cool','can u like actualy stop being not cool','u r uncool','go away!','i dont talk to uncool people so stop talking to me']
TOKEN = "975642105:AAHJWLnTfxmLt8fr1giBI0yMsUy3aP0jBm4"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
fileName = re.compile(r'([a-zA-Z0-9_]+)(\.)(txt)')
fileContent = re.compile(r'[\d]{9}')

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js

def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)    

def echo_all(updates):
    print('ACTIVE')
    for update in updates["result"]:
        try:
            chat = update["message"]["chat"]["id"]
            if "last_name" not in update["message"]["from"]:
                lastname = ' '
            else:
                lastname = update["message"]["from"]["last_name"]
            file = open('history.txt')
            content = file.read()
            mo = fileContent.findall(content)
            if str(chat) not in mo:
                file.close()
                file2 = open('history.txt','a')
                file2.write(str(update["message"]["from"]["first_name"])+' '+str(lastname)+'\n'+str(chat)+'\n')
                file2.close()
            else:
                file.close()
            if int(chat) == 473042816:
                x = random.randint(0,len(com)-1)
                send_message(com[x], chat)
            elif int(chat) == 504061876:
                lizard = emojize(':lizard:', use_aliases=True)
                send_message(lizard,chat)
            elif 'text' in update['message']:
                x = random.randint(0,len(no)-1)
                send_message(no[x], chat)
                try:
                    print(update['message']['text'])
                except Exception as p:
                    print(p)
            elif 'sticker' in update['message']:
                send_message('dont u dare send me stickers again', chat)
            elif 'photo' in update['message']:
                send_message('i dont want to see ur dumb pictures', chat)         
            elif 'video' in update['message']:
                send_message('i dont care about ur video. dont. send. them. to. me.', chat)
            elif 'animation' in update['message']:
                send_message('your GIFs are bad', chat)
            elif 'location' in update['message']:
                send_message('im going to go as far away from there as possible', chat)
            elif 'document' in update['message']:
                send_message('i dont want ur documents.',chat)
            elif 'contact' in update['message']:
                if '+6590606444' == update['message']['contact']['phone_number'] or '90606444' == update['message']['contact']['phone_number']:
                    send_message('looks like a cool guy',chat)
                else:
                    send_message('this person is irrelevant',chat)
            else:
                x = random.randint(0,len(com)-1)
                send_message(no[x], chat)
        except Exception as e:
            print(e)

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)
        


if __name__ == '__main__':
    main()
