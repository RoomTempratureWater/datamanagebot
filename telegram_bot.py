import requests
from config import TELEGRAM_SEND_MESSAGE_URL,TELEGRAM_SEND_PHOTO_URL,TELEGRAM_PIC_URL,TELEGRAM_PIC_jURL
from maps import nearby_search
import replies
import STATES
from datetime import datetime as dt
import pytz
import dbhandler

class TelegramBot:

    def __init__(self):
        self.chat_id = None
        self.text = None
        self.first_name = None
        self.last_name = None
        self.raw = None

    def parse_webhook_data(self, data):
        #print(data)
        message = data['message']

        self.chat_id = message['chat']['id']
        try:
            self.incoming_message_text = message['text'].lower()
        except:
            self.incoming_message_text = None
        self.first_name = message['from']['first_name']
        try:
            self.last_name = message['from']['last_name']
        except:
            self.last_name = ""
        self.raw = data


    def action(self):

        success = None

        if STATES.state == None and self.incoming_message_text == '/sstart':
            self.outgoing_message_text = 'Hewo!,you can do some cool stuff with this bot like\n\n'+replies.note
            success = self.send_message()

        elif STATES.state == None and self.incoming_message_text == '/nnnotes':
            self.outgoing_message_text = replies.note
            success = self.send_message()

        elif STATES.state == None and self.incoming_message_text == '/hello':
            self.outgoing_message_text = replies.welcome(self.first_name)
            success = self.send_message()

        elif STATES.state == None and self.incoming_message_text == '/developer':
            self.outgoing_message_text = 'semen cheescake'
            success = self.send_message()


        elif STATES.state == None and self.incoming_message_text == '/accounts':
            data = dbhandler.getdata()
            self.outgoing_message_text = data
            success = self.send_message()

        elif STATES.state == None and self.incoming_message_text == '/del_acc':
            STATES.state = "datadel"
            self.outgoing_message_text = "Enter name and rank"
            success = self.send_message()

        elif STATES.state == None and self.incoming_message_text == '/add_account':
            STATES.state = "dataentry"
            self.outgoing_message_text = "Enter name and rank"
            success = self.send_message()

        elif STATES.state == None and self.incoming_message_text == '/showall':
            data_str = dbhandler.get_all()
            self.outgoing_message_text = data_str
            success = self.send_message()


        elif STATES.state == "dataentry":
            STATES.state = None
            try:
                txt = self.incoming_message_text
                txt = txt.split(" ")
                #print(txt)
                dbhandler.append(txt[0],txt[1])
                self.outgoing_message_text = "Done"
                success = self.send_message()
            except:
                self.outgoing_message_text = "Failed"
                success = self.send_message()
        elif STATES.state == 'datadel':
            STATES.state = None
            try:
                txt = self.incoming_message_text
                txt = txt.split(" ")
                dbhandler.del_acc(txt[0],txt[1])
                self.outgoing_message_text = "Done"
                success = self.send_message()
            except:
                self.outgoing_message_text = "Failed"
                success = self.send_message()

        else:
            pass
            #self.outgoing_message_text = 'Invalid command!, pls enter valid commands'
            #success = self.send_message()
        return success


    def send_message(self):
        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text))

        return True if res.status_code == 200 else False
    def send_photo(self):
        res = requests.get(TELEGRAM_SEND_PHOTO_URL.format(self.chat_id,self.outgoing_photo,self.caption))
        return True if res.status_code == 200 else False

    @staticmethod
    def init_webhook(url):
        requests.get(url)


