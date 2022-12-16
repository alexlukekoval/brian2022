import pygame
import time
import os

pygame.init()

_drip_file = '/usr/share/sounds/gnome/default/alerts/drip.ogg'
_sonar_file = '/usr/share/sounds/gnome/default/alerts/sonar.ogg'
_glass_file = '/usr/share/sounds/gnome/default/alerts/glass.ogg'
_brian_file = os.getcwd() + '/brians_response.mp3'
print('brian voice file at:', _brian_file)

_drip_sound = pygame.mixer.Sound(_drip_file)
_sonar_sound = pygame.mixer.Sound(_sonar_file)
_glass_sound = pygame.mixer.Sound(_glass_file)

_drip_sound.set_volume(0.5)
_sonar_sound.set_volume(0.5)
_glass_sound.set_volume(0.4)


def play_drip():
    _drip_sound.play()


def play_sonar():
    _sonar_sound.play()


def play_glass():
    _glass_sound.play()


def play_brian():
    pygame.mixer.music.load(_brian_file)
    pygame.mixer.music.play(1)
    while pygame.mixer.music.get_busy():
        time.sleep(0.05)


if __name__ == """__main__""":
    play_sonar()
    time.sleep(1)
    play_glass()
    time.sleep(1)
    play_drip()
    time.sleep(1)
    play_brian()