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

dict_sounds = {"another_love",
               "i_am_yours",
               "me_gustas_tu",
               "sweater_weather"}

pygame.mixer.music.load(list_sounds[0])
pygame.mixer.music.set_volume(0.3)

def play():
    pygame.mixer.music.play()
    input_play()

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
    


index1 = 0
def next_track():
    global index1
    pygame.mixer.music.stop()
    pygame.mixer.music.load(list_sounds[index1])
    pygame.mixer.music.play()
    index1 = (index1 + 1)% len(list_sounds)
    print_index = index1 - 1
    print(list_sounds[print_index])
    input_next()

index2 = 0
def before_track():
    global index2
    pygame.mixer.music.stop()
    index2 = (index2 - 1)% len(list_sounds)
    pygame.mixer.music.load(list_sounds[index2])
    pygame.mixer.music.play()
    print(list_sounds[index2])
    input_before()

for track in list_sounds1:
    label = ctk.CTkLabel(master = m_app.app.FRAME_TRACK, text_color= "black", font = m_font.font_label, text = track)
    label.pack(fill = "x", anchor = "w") 

def input_next():
    for track in list_sounds1:
        track = (index1 + 1)% len(list_sounds1)
        next_print_index = track - 2
        current_track = ctk.CTkLabel(
            master = m_app.app,
            width = 160,
            height = 59,
            bg_color = "#4CB7CE",
            text = list_sounds1[next_print_index],
            text_color = "white",
            font = m_font.font_label
        )
        current_track.place(x = 270, y = 15)
def input_before():
    for track in list_sounds1:
        track = (index2 - 1)% len(list_sounds1)
        before_print_index = list_sounds1[index2]
        current_track = ctk.CTkLabel(
            master = m_app.app,
            width = 160,
            height = 59,
            bg_color = "#4CB7CE",
            text = before_print_index,
            text_color = "white",
            font = m_font.font_label
        )
        current_track.place(x = 270, y = 15)
def input_play():
    for track in list_sounds1:
        track = (index1 + 1)% len(list_sounds1)
        play_print_index = track - 2
        current_track = ctk.CTkLabel(
            master = m_app.app,
            width = 160,
            height = 59,
            bg_color = "#4CB7CE",
            text = list_sounds1[play_print_index],
            text_color = "white",
            font = m_font.font_label
        )
        current_track.place(x = 270, y = 15)

index = 0
def delete():
    global index
    del list_sounds[index]
    if index >= len(list_sounds):
        index = 0
    FRAME_TRACK = m_frame.My_Frame(text = "", master = m_app.app, width = 150, height = 69, border_width = 5, fg_color = "#BDBDBD", border_color = "#BDBDBD", corner_radius = 0)
    FRAME_TRACK.grid(row = 0, column = 0, padx = 5 , pady = 10)
    pygame.mixer.music.load(list_sounds[index])
    pygame.mixer.music.play()
    for index in list_sounds:
        label = ctk.CTkLabel(master = m_app.app.FRAME_TRACK, text_color= "black", font = m_font.font_label, text = index)
        label.pack(fill = "x", anchor = "w") 
    print(list_sounds)
