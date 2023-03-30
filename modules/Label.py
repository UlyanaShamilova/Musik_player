import customtkinter as ctk
import modules.create_app as m_app
import modules.font as m_font
import modules.sounds as m_sounds

current_track = ctk.CTkLabel(master = m_app.app,
                             width = 160,
                             height = 59,
                             bg_color = "#4CB7CE",
                             text_color = "white",
                             font = m_font.font_label,
                             text = ""
                             )
                    