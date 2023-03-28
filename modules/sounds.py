import pygame
import customtkinter as ctk
import random
import modules.create_button as m_button
pygame.mixer.init()
list_sounds = ["sounds/isabel-larosa-i-m-yours-sped-up-mp3.mp3",
               "sounds/moonlight.mp3",
               "sounds/tom-odell-another-love-speed-up_456239068.mp3",
               "sounds/yell0wknife-me-gusta-speed-up-mp3.mp3"]

pygame.mixer.music.load(list_sounds[0])
pygame.mixer.music.set_volume(1)

def play():
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def volum_plus():
    volume = pygame.mixer.music.get_volume() + 0.1
    if volume > 1.0:
        volume = 1.0
    pygame.mixer.music.set_volume(volume)

def volum_minus():
    volume = pygame.mixer.music.get_volume() - 0.1
    if volume > 1.0:
        volume = 1.0
    pygame.mixer.music.set_volume(volume)

def mix():
    random.shuffle(list_sounds)
    pygame.mixer.music.load(list_sounds[0])
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()
