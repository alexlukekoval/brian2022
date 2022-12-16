from als_gpt import AlsGPT
from amazon_boto import AlsBoto
from pygame_sound_player3 import play_drip, play_sonar, play_brian, play_glass
from my_speech_recognition2 import AlsSpeechToText
import config
import os

gpt = AlsGPT(human_name=config.human_name)  # for conversation
boto = AlsBoto()  # for text to speech
listener = AlsSpeechToText()  # for mic to text


def speak(text):
    boto.make_file(text)
    play_brian()


while True:
    print('please speak')
    user_said = ''
    prompted_user_to_speak = False
    while not user_said:
        try:
            play_sonar()
            user_said = listener.listen_to_mic()
            play_drip()
        except Exception as e:
            continue
    print('user said:', user_said)
    bot_response = gpt.say_to_bot(user_said)
    print('bot responded:', bot_response)
    speak(bot_response)

#
# boto.say('speaking again')
# while True:
#     output = gpt.say_to_bot(input('input here: '))
#     print(output)
