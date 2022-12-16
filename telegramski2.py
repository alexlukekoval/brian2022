from config import telegram_token as TOKEN, telegram_chat_id as IDD
from telegram.ext import Updater, MessageHandler, Filters
import telegram
from telegram.error import TimedOut
import time


class AlsTelegram:
    def __init__(self, custom_handler):
        self.custom_handler = custom_handler
        self.updater = Updater(token=TOKEN, use_context=True)
        self.updater.dispatcher.add_handler(MessageHandler(Filters.text, self.message_handler))
        self.updater.start_polling(poll_interval=0.1, timeout=1)
        self.bot = telegram.Bot(token=TOKEN)
        return

    def message_handler(self, update, context):
        """message_handler just deals with unneeded context object"""
        self.custom_handler(update.message.text)

    def send_audio_from_file(self, file):
        self.bot.send_audio(chat_id=IDD, audio=open(file, 'rb'))

    def send_message_to_user(self, message):
        try:
            self.bot.send_message(chat_id=IDD, text=message)
        except TimedOut:
            print('got time out error with message:', message)
            time.sleep(1)
            self.bot.send_message(chat_id=IDD, text=message)
            print('succeded with 2nd attempt sending message')

# updater = Updater(token=TOKEN, use_context=True)
#
# # Register the message handler function
# updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
#
# # Start the bot
# updater.start_polling()
