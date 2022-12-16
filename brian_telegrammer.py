from telegramski2 import AlsTelegram
import time
import os
from als_gpt import AlsGPT
from amazon_boto import AlsBoto

from config import human_name
from brian_utils import now


class TelegramBrian:
    def __init__(self):
        self.gpt = AlsGPT(human_name=human_name)  # for conversation
        self.voice = False
        self.boto = AlsBoto()  # for text to speech
        # listener = AlsSpeechToText()  # for mic to text

        # creating the telegram starts listening
        print('telegram listening...')
        self.tele = AlsTelegram(custom_handler=self.on_message)

    def on_message(self, message: str):
        lower = message.lower()
        print('Human:', message)
        if 'help' in lower and len(message) < 12:
            print('doing help')
            self.send_message('here are the help options: ' +
                              '\nask for bobby for mycroftai TODO' +
                              '\nincrease bot response length TODO' +
                              '\nask for voice on or off')
        elif 'voice' in lower and 'off' in lower:
            self.voice = False
            self.send_message('turned voice off')
        elif 'voice' in lower and 'on' in lower:
            self.voice = True
            self.send_message('turned voice on')
        elif 'bobby' in message.lower():
            self.bobby(message)
        else:
            self.brian(message)

    def send_message(self, message):
        self.tele.send_message_to_user(message)
        if self.voice:
            self.boto.make_file(message)
            self.tele.send_audio_from_file(self.boto.file)
        # self.tele

    def bobby(self, message):
        self.send_message('not yet implemented bobby')
        return

    def brian(self, message):
        # print('asking brian for a response to:', message[:20])
        result = self.gpt.say_to_bot(message)
        # print(result)
        self.send_message(result)
        return


if __name__ == "__main__":
    TelegramBrian()
