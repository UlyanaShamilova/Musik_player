import pygame
import customtkinter as ctk
import random
import modules.create_button as m_button
from customtkinter import filedialog
import modules.font as m_font
import modules.create_app as m_app
import os
import modules.create_frame as m_frame
from tkinter import Listbox
pygame.mixer.init()
list_sounds = ["sounds/another_love.mp3",
               "sounds/i_am_yours.mp3",
               "sounds/me_gustas_tu.mp3",
               "sounds/sweater_weather.mp3"]

list_sounds1 = ["another_love",
               "i_am_yours",
               "me_gustas_tu",
               "sweater_weather"]

pygame.mixer.music.load(list_sounds[0])
pygame.mixer.music.set_volume(1)

def play():
    pygame.mixer.music.play()
    for track in list_sounds1:
        track = (cur_track)% len(list_sounds1)
        current_track = ctk.CTkLabel(
            master = m_app.app,
            width = 160,
            height = 59,
            bg_color = "#4CB7CE",
            text = list_sounds1[track],
            text_color = "white",
            font = m_font.font_label
        )
        current_track.place(x = 270, y = 15)

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

def add_track():
    global file_path
    file_path = ctk.filedialog.askopenfilename(initialdir="track/", filetypes=(("mp3", "*.mp3;*.wav"),))
    if file_path:
        list_sounds.append(file_path)
    
    file_path1 = os.path.splitext(os.path.basename(file_path))[0]
    if file_path1:
        list_sounds1.append(file_path1)
        update_tracks()
  
def update_tracks():
    global label
    for widget in m_app.app.FRAME_TRACK.winfo_children():
        widget.destroy()
    for i,track in enumerate(list_sounds1):
        label = ctk.CTkLabel(master = m_app.app.FRAME_TRACK, text = f"{i+1}.{track}", text_color = "black", font = m_font.font_label)
        label.pack(anchor = "w")


cur_track = 0

def delete():
    global list_sounds
    global cur_track
    pygame.mixer.music.unload()
    list_sounds.pop(cur_track)
    list_sounds1.pop(cur_track)
    cur_track -= 1
    update_tracks()
    print(list_sounds1[cur_track])


def next_track ():
    global cur_track
    if cur_track >= len(list_sounds1):
        pass
    cur_track += 1
    pygame.mixer.music.load(list_sounds[cur_track])
    pygame.mixer.music.play()
    curr_track = ctk.CTkLabel(
        master = m_app.app,
        width = 160,
        height = 59,
        bg_color = "#4CB7CE",
        text = list_sounds1[cur_track],
        text_color = "white",
        font = m_font.font_label
        )
    curr_track.place(x = 270, y = 15)

def before_track ():
    global cur_track
    if cur_track < len(list_sounds1):
        pass
    cur_track -= 1
    pygame.mixer.music.load(list_sounds[cur_track])
    pygame.mixer.music.play()
    curr_track = ctk.CTkLabel(
        master = m_app.app,
        width = 160,
        height = 59,
        bg_color = "#4CB7CE",
        text = list_sounds1[cur_track],
        text_color = "white",
        font = m_font.font_label
        )
    curr_track.place(x = 270, y = 15)

    
for track in list_sounds1:
    label = ctk.CTkLabel(master = m_app.app.FRAME_TRACK, text_color= "black", font = m_font.font_label, text = track)
    label.pack(fill = "x", anchor = "w") 
