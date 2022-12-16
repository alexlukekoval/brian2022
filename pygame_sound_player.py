import pygame
import time


def _play_file(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(1)
    while pygame.mixer.music.get_busy():
        time.sleep(0.03)


class AlsSoundPlayer:
    pygame.init()

    def __init__(self):
        self.bot_response_file = '/home/ally/PycharmProjects/projectLinux/gpt/brians_response.mp3'

    def play_recent_bot_response(self):
        pygame.mixer.music.load(self.bot_response_file)
        pygame.mixer.music.play(1)
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

