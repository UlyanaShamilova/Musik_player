import pygame
import customtkinter as ctk
import random
import modules.create_button as m_button
from customtkinter import filedialog
pygame.mixer.init()
list_sounds = ["sounds/another_love.mp3",
               "sounds/i_am_yours.mp3",
               "sounds/me_gustas_tu.mp3",
               "sounds/sweater_weather.mp3"]

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
paused = False
def pause():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True
    else:
        pygame.mixer.music.unpause()
        paused = False
index = 0      
def delete():
    global index
    del list_sounds[index]
    if index >= len(list_sounds):
        index = 0
    pygame.mixer.music.load(list_sounds[index])
    pygame.mixer.music.play()

def add_track():
    track = ctk.filedialog.askopenfilename(initialdir="track/", filetypes=(("mp3", "*.mp3"),))
    
index1 = 0
def next_track():
    global index1
    pygame.mixer.music.stop()
    pygame.mixer.music.load(list_sounds[index1])
    pygame.mixer.music.play()
    index1 = (index1 + 1)% len(list_sounds)
    print_index = index1 - 1
    print(list_sounds[print_index])
index2 = 0
def before_track():
    global index2
    pygame.mixer.music.stop()
    index2 = (index2 - 1)% len(list_sounds)
    pygame.mixer.music.load(list_sounds[index2])
    pygame.mixer.music.play()
    print(list_sounds[index2])
