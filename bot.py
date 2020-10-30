# Request to api to respons API or json file

'''
import requests
from pprint import pprint

# url_request_meaning_api

url = "https://api.telegram.org/test"
response = requests.get(url)
#pprint(response.json())

for mse in response.json()['result']:
    pprint(mse['message']['text'])

'''
# telegram 
'''
import telegram

bot = telegram.Bot(token='test')

print(bot.getMe())

for msg in bot.get_updates():
    print(msg.message.text)
'''
'''
from telegram.ext import Updater, CommandHandler

updater = Updater(token='test')
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello man")


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)
updater.start_polling()
'''
'''
from telegram.ext import Updater, MessageHandler, Filters

updater = Updater(token='test')
dispatcher = updater.dispatcher


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=update.message.text.upper())


echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()
'''










'''



#option

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

updater = Updater(token='test')
dispatcher = updater.dispatcher

def option(bot, update):
    button = [
        [InlineKeyboardButton("Kirollos Noshy", callback_data="Kirollos Noshy"),
         InlineKeyboardButton("Selvana Noshy", callback_data="Selvane Noshy")],
        [InlineKeyboardButton("Yostina Noshy", callback_data="Yostina Noshy")]
    ]
    reply_markup = InlineKeyboardMarkup(button)

    bot.send_message(chat_id=update.message.chat_id,
                     text="Click anyone",
                     reply_markup=reply_markup)


option_handler = CommandHandler("option", option)
dispatcher.add_handler(option_handler)


def button(bot, update):
    querydata = update.callback_query
    bot.send_message(chat_id=querydata.message.chat_id,
                     text="You select {}.".format(querydata.data))


button_handler = CallbackQueryHandler(button)
dispatcher.add_handler(button_handler)
updater.start_polling()





'''



import nmap
from telegram.ext import Updater, CommandHandler

updater = Updater(token='test')
dispatcher = updater.dispatcher


def command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="/scanports \n /checkstatus")
start_handler = CommandHandler("c", command)
dispatcher.add_handler(start_handler)




def scanports(bot, update):
    nm = nmap.PortScanner()
    scan_range = nm.scan(hosts="197.57.2.0")
    data = scan_range['scan']
    print(data)
    bot.send_message(chat_id=update.message.chat_id, text=data)
scanports_handler = CommandHandler("scanports", scanports)
dispatcher.add_handler(scanports_handler)



def checkstatus(bot, update):
    nm = nmap.PortScanner()
    scan_range = nm.scan('197.57.2.0', '21-443')
    for host in nm.all_hosts():
        print('Host : %s' % (host))
        print('State : %s' % nm[host].state())
    bot.send_message(chat_id=update.message.chat_id, text='Host : 197.57.2.0' + '  =>  ' + nm[host].state())
checkstatus_handler = CommandHandler("checkstatus", checkstatus)
dispatcher.add_handler(checkstatus_handler)


updater.start_polling()
