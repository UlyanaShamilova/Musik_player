import pygame
import customtkinter as ctk
import random
import modules.font as m_font
import modules.create_app as m_app
import os
pygame.mixer.init()

list_sounds = []
list_sounds1 = []

num_track = 0

def play():
    global num_track
    global cur_track
    # загрузка трека
    pygame.mixer.music.load(list_sounds[cur_track])
    # воспроизвидение трека
    pygame.mixer.music.play()

    update_tracks()
    label_track = ctk.CTkLabel(
        master = m_app.app.FRAME_CURR_TRACK,
        text = list_sounds1[cur_track],
        text_color = "white",
        font = m_font.font)
    label_track.place(x = 10, y = 10) 
    num_track = 1

# свойство паузы
paused = True

def pause_track():
    global paused
    # условие если трек играет
    if not paused:
        pygame.mixer.music.pause()
        paused = True
    else:
        pygame.mixer.music.unpause()
        paused = False 


def stop():
    pygame.mixer.music.stop()
    
# функция добавления звука
pygame.mixer.music.set_volume(1)
def volume_plus():
    # переменная единица добавления звука
    volume = pygame.mixer.music.get_volume() + 0.1
    # ограничения максимального звука
    if volume > 1.0:
        volume = 1.0
    pygame.mixer.music.set_volume(volume)

def volume_minus():
    # пременная еденицы убавления звука
    volume = pygame.mixer.music.get_volume() - 0.1
    if volume > 1.0:
        volume = 1.0
    pygame.mixer.music.set_volume(volume)

cur_track = 0

def next_track():
    global cur_track
    global num_track
    # условие если переменная больше или равно длинны списка
    if cur_track >= len(list_sounds1):
        pass
    # увеличение индекса трека на 1
    cur_track += 1
    pygame.mixer.music.load(list_sounds[cur_track])
    pygame.mixer.music.play(1)


    update_tracks()
    # лейбл который показывает текущий трек
    label_track = ctk.CTkLabel(
        master = m_app.app.FRAME_CURR_TRACK,
        text = list_sounds1[cur_track],
        text_color = "white",
        font = m_font.font)
    label_track.place(x = 10, y = 10) 
    num_track = 1

def before_track():
    global cur_track
    global num_track
    global label
    # если индекс песни меньше или равен нулю то мы его пропускаем
    if cur_track <= 0:
        pass
    # уменьшение индекса трека на 1
    cur_track -= 1
    pygame.mixer.music.load(list_sounds[cur_track])
    pygame.mixer.music.play(1)


    update_tracks()
    # выводим текущий трек на фрейм
    label = ctk.CTkLabel(
        master = m_app.app.FRAME_CURR_TRACK,
        text = list_sounds1[cur_track],
        text_color = "white",
        font = m_font.font)
    label.place(x = 10, y = 10)
    num_track = 1 


def mix():
    global cur_track
    global num_track
    # выбираем рандомную песню из списка
    cur_track = random.randint(0,(len(list_sounds1)) - 1)
    pygame.mixer.music.load(list_sounds[cur_track])
    pygame.mixer.music.play(1)

    update_tracks()
    label_track = ctk.CTkLabel(
        master = m_app.app.FRAME_CURR_TRACK,
        text = list_sounds1[cur_track],
        text_color = "white",
        font = m_font.font)
    label_track.place(x = 0, y = 10) 
    num_track = 1

def add_track():
    global file_path
    # вызываем окно которое позволяет выбрать любую песню
    file_path = ctk.filedialog.askopenfilename(initialdir="track/", filetypes=(("mp3", "*.mp3;*.wav"),))
    if file_path:
        # добовляем путь трека к списку
        list_sounds.append(file_path)
    
    # оставляет только песню без пути
    file_path1 = os.path.splitext(os.path.basename(file_path))[0]
    if file_path1:
        # добавление в список название треков 
        list_sounds1.append(file_path1)
        update_tracks()
  
def update_tracks():
    # расположение текста по иксу
    text_x = 10
    # расположение текста по игрику
    text = 10
    # перебераем все виджеты которые находяться на фрейме 
    for widget in m_app.app.FRAME.winfo_children():
        # уничтожаем старые и добавляем новые значение
        widget.destroy()
        # перебераем все виджеты которые находяться на другом фрейме 
    for widget in m_app.app.FRAME_CURR_TRACK.winfo_children():
        widget.destroy()
        # перебираем список и выводим треки на фрейм
    for i, track in enumerate(list_sounds1):
        label = ctk.CTkLabel(
        master = m_app.app.FRAME_TRACK, 
        text = f"{track}", 
        text_color = "black", 
        font = m_font.font_label)
        label.place(x = text_x, y = text)
        text = text + 30

    
def delete():
    global list_sounds
    global cur_track
    global num_track

    num_track = 0
    update_tracks()
    # удаляем песню
    pygame.mixer.music.unload()
    # удаляем песню из списка с путями
    list_sounds.pop(cur_track)
    # удаляем песню из списка с названием трека
    list_sounds1.pop(cur_track)
    cur_track -= 1
    update_tracks()