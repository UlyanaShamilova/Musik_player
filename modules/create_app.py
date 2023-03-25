import customtkinter as ctk
import modules.create_frame as m_frame

class App(ctk.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        self.geometry(f"{454}x{469}+{700}+{150}")
        self.resizable(False,False)
        self.title("Music_player")
        self.FRAME = m_frame.My_Frame(text = " ", master = self, width = 440, height = 367, border_width = 5)


app = App(454,469)