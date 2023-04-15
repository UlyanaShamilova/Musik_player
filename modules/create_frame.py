import customtkinter as ctk
import modules.create_app as m_app

class My_Frame(ctk.CTkFrame):
    def __init__(self, text, master, width, height, border_width, fg_color, 
                 border_color, corner_radius, **kwargs):
        super().__init__(master = master,width= width, height= height, border_width = border_width, 
                fg_color = fg_color, border_color = border_color, corner_radius = corner_radius, **kwargs)

        def track_names(self, text, text_color, fg_color, bg_color):
            return ctk.CTkLabel(
                master = m_app.app.FRAME_TRACK,
                text = text,
                font = track_names,
                text_color = 'black',
                fg_color = 'transparent',
                bg_color = 'transparent'
            )
