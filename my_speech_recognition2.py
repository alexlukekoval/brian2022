import speech_recognition
from pygame_sound_player import AlsSoundPlayer
import contextlib
import os
import pyaudio  # needed for the sonar and glass sounds to work
import sys


@contextlib.contextmanager
def ignoreStderr():
    devnull = os.open(os.devnull, os.O_WRONLY)
    old_stderr = os.dup(2)
    sys.stderr.flush()
    os.dup2(devnull, 2)
    os.close(devnull)
    try:
        yield
    finally:
        os.dup2(old_stderr, 2)
        os.close(old_stderr)


class AlsSpeechToText:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.sound_player = AlsSoundPlayer()

    def listen_to_mic(self):
        with ignoreStderr():
            # obtain audio from the microphone
            with speech_recognition.Microphone() as source:
                print("Say something!")
                try:
                    # self.recognizer.adjust_for_ambient_noise(source)
                    audio = self.recognizer.listen(source, timeout=2)
                    print('recieved audio')
                except:
                    print('got error waiting for mic')
            # recognize speech using Google Speech Recognition
            output_text = ''
            try:
                print('converting to text')
                output_text += self.recognizer.recognize_google(audio)
                # print("Google Speech Recognition thinks you said: " + )
            except speech_recognition.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
                raise Exception('Couldnt hear mic')
            except speech_recognition.RequestError as e:
                print("Could not request results from Google Speech Recognition service: {0}".format(e))
                raise Exception('couldnt get the mic results from google')
            return output_text


if __name__ == "__main__":
    a = AlsSpeechToText()
    print(a.listen_to_mic())
    # p = pyaudio.PyAudio()
    # c = p.get_device_count()
    # print(c)
    # print(p.get_default_input_device_info())
    # for i in range(c):
    #     info = p.get_device_info_by_index(i)
    #     print(info)
    #     for k, v in info.items():
    #         if 'usb' in str(k).lower() or 'usb' in str(v).lower():
    #             print(info)
