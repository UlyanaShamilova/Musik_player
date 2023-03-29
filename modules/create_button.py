import customtkinter as ctk
import modules.create_app as m_app
from PIL import Image
import modules.find_path as m_path
import modules.font as m_font
import modules.sounds as m_sounds
button_play = ctk.CTkButton(
    master = m_app.app.FRAME1,
    width = 169,
    height = 60,
    border_width = 4,
    border_color = "#251F1F",
    corner_radius = 20,
    fg_color = "#BDBDBD",
    bg_color = "#4CB7CE",
    text = "",
    command = m_sounds.play,
    image = ctk.CTkImage
    (light_image=Image.open(m_path.search_path("images/button_play.png")),
    size = (82, 43)))
button_play.place(x = 0, y = 0, anchor = ctk.NW)

button_stop = ctk.CTkButton(
    master = m_app.app.FRAME1,
    width = 169,
    height = 60,
    border_width = 4,
    border_color = "#251F1F",
    corner_radius = 20,
    fg_color = "#BDBDBD",
    bg_color = "#4CB7CE",
    text = "",
    command = m_sounds.stop,
    image = ctk.CTkImage
    (light_image=Image.open(m_path.search_path("images/button_stop.png")),
    size = (45, 43)))
button_stop.place(x = 0, y = 235, anchor = ctk.NW)  

button_pause = ctk.CTkButton(
    master = m_app.app.FRAME1,
    width = 169,
    height = 60,
    border_width = 4,
    border_color = "#251F1F",
    corner_radius = 20,
    fg_color = "#BDBDBD",
    bg_color = "#4CB7CE",
    text = "",
    command = m_sounds.pause,
    image = ctk.CTkImage
    (light_image=Image.open(m_path.search_path("images/button_pause.png")),
    size = (50, 50)))
button_pause.place(x = 0, y = 160, anchor = ctk.NW)

button_back = ctk.CTkButton(
    master = m_app.app.FRAME1,
    width = 61,
    height = 58,
    border_width = 4,
    border_color = "#251F1F",
    corner_radius = 20,
    fg_color = "#BDBDBD",
    bg_color = "#4CB7CE",
    text = "",
    command= m_sounds.before_track,
    image = ctk.CTkImage
    (light_image=Image.open(m_path.search_path("images/button_back.png")),
    size = (28, 21)))
button_back.place(x = 95, y = 80, anchor = ctk.NW)

button_next = ctk.CTkButton(
    master = m_app.app.FRAME1,
    width = 61,
    height = 58,
    border_width = 4,
    border_color = "#251F1F",
    corner_radius = 20,
    fg_color = "#BDBDBD",
    bg_color = "#4CB7CE",
    text = "",
    command= m_sounds.next_track,
    image = ctk.CTkImage
    (light_image=Image.open(m_path.search_path("images/button_next.png")),
    size = (28, 21)))
button_next.place(x = 0, y = 80, anchor = ctk.NW)

button_sound_plus = ctk.CTkButton(
    master = m_app.app,
    width = 61,
    height = 58,
    border_width = 4,
    border_color = "#251F1F",
    corner_radius = 20,
    fg_color = "#BDBDBD",
    bg_color = "#4CB7CE",
    text = "",
    command = m_sounds.volum_plus,
    image = ctk.CTkImage
    (light_image=Image.open(m_path.search_path("images/button_sound+.png")),
    size = (28, 31)))
button_sound_plus.place(x = 280, y = 400, anchor = ctk.NW)

button_sound_minus = ctk.CTkButton(
    master = m_app.app,
    width = 61,
    height = 58,
    border_width = 4,
    border_color = "#251F1F",
    corner_radius = 20,
    fg_color = "#BDBDBD",
    bg_color = "#4CB7CE",
    text = "",
    command= m_sounds.volum_minus,
    image = ctk.CTkImage
    (light_image=Image.open(m_path.search_path("images/button_sound-.png")),
    size = (28, 31)))
button_sound_minus.place(x = 370, y = 400, anchor = ctk.NW)
button_mix = ctk.CTkButton(
    master = m_app.app,
    width = 61,
    height = 58,
    border_width = 4,
    border_color = "#251F1F",
    corner_radius = 20,
    fg_color = "#BDBDBD",
    bg_color = "#4CB7CE",
    text = "",
    command = m_sounds.mix,
    image = ctk.CTkImage
    (light_image=Image.open(m_path.search_path("images/button_mix.png")),
    size = (30, 20)))
button_mix.place(x = 190, y = 400, anchor = ctk.NW)

button_delete = ctk.CTkButton(
    master = m_app.app,
    width = 61,
    height = 58,
    border_width = 4,
    border_color = "#251F1F",
    corner_radius = 20,
    fg_color = "#BDBDBD",
    bg_color = "#4CB7CE",
    text = "",
    command = m_sounds.delete,
    image = ctk.CTkImage
    (light_image=Image.open(m_path.search_path("images/button_delete.png")),
    size = (30, 20)))
button_delete.place(x = 100, y = 400, anchor = ctk.NW)

button_plus = ctk.CTkButton(
    master = m_app.app,
    width = 61,
    height = 58,
    border_width = 4,
    border_color = "#251F1F",
    corner_radius = 20,
    fg_color = "#BDBDBD",
    bg_color = "#4CB7CE",
    text = "+",
    command= m_sounds.add_track,
    text_color = "black",
    font = m_font.font
    )

button_plus.place(x = 20, y = 400, anchor = ctk.NW)
