import customtkinter as ctk
import modules.create_frame as m_frame

class App(ctk.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{700}+{150}")
        self.resizable(False,False)
        self.title("Music_player")
        self.FRAME = m_frame.My_Frame(text = "назви треків що додано.", master = self, width = 233, height = 367, border_width = 5, fg_color = "#BDBDBD", border_color = "#000000", corner_radius = 20)
        self.FRAME.grid(row = 0, column = 0, padx = 5 , pady = 10)
        self.FRAME1 = m_frame.My_Frame(text= "", master = self,width = 169, height = 298, border_width = 5, fg_color = "#4CB7CE", border_color="#4CB7CE", corner_radius =20)
        self.FRAME1.grid(row = 0, column = 1, padx = 20, pady = 10, sticky=ctk.SW)
        self.FRAME_TRACK = m_frame.My_Frame(text = "", master = self, width = 150, height = 69, border_width = 5, fg_color = "#BDBDBD", border_color = "#BDBDBD", corner_radius = 0)
        self.FRAME_TRACK.grid(row = 0, column = 0, padx = 5 , pady = 10)
        self.FRAME_CURR_TRACK = m_frame.My_Frame(text = "", master = self, width = 160, height = 59, border_width = 5, fg_color = "#4CB7CE", border_color = "#4CB7CE", corner_radius = 0)
        self.FRAME_CURR_TRACK.place(x = 270, y = 15)

app = App(454,469)
app.configure(bg = "#4CB7CE")
