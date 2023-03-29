import customtkinter as ctk
import modules.create_app as m_app
import modules.font as m_font
import modules.sounds as m_sounds

lable = ctk.CTkLabel(master = m_app.app.FRAME,
                     width = 173,
                     height = 79,
                     bg_color = "#BDBDBD",
                     text_color ="black",
                     text = "another_love",
                     font = m_font.font_label
                     )
lable.place(x = 28, y = 37)

lable1 = ctk.CTkLabel(master = m_app.app.FRAME,
                     width = 173,
                     height = 79,
                     bg_color = "#BDBDBD",
                     text_color ="black",
                     text = "i_am_yours",
                     font = m_font.font_label
                     )
lable1.place(x = 28, y = 86)
lable2 = ctk.CTkLabel(master = m_app.app.FRAME,
                     width = 173,
                     height = 79,
                     bg_color = "#BDBDBD",
                     text_color ="black",
                     text = "me_gustas_tu",
                     font = m_font.font_label
                     )
lable2.place(x = 28, y = 135)

lable3 = ctk.CTkLabel(master = m_app.app.FRAME,
                     width = 173,
                     height = 79,
                     bg_color = "#BDBDBD",
                     text_color ="black",
                     text = "sweater_weather",
                     font = m_font.font_label
                     )
lable3.place(x = 28, y = 184)

current_track = ctk.CTkLabel(master = m_app.app,
                             width = 160,
                             height = 59,
                             bg_color = "#4CB7CE",
                             text_color = "white",
                             font = m_font.font_label,
                             text = ""
                             )
                    