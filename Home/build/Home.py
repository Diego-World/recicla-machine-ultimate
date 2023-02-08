from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame
from tkVideoPlayer import TkinterVideo
from Acess.build import Acess

class Home:
    def __init__(self, master=None):
        self.window = master if master else Tk()
        self.window.geometry("1366x768")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Recicla Machine")
        img = PhotoImage(file='assets/Icone.png')
        self.window.tk.call('wm', 'iconphoto', self.window._w, img)

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Apollo\Desktop\UltimateRecicla\Home\build\assets\frame0")

        # self.main_frame = Frame(self.window)
        # self.main_frame.configure(width=1366, height=768)
        # self.main_frame.pack(fill="both", expand=True)
        #
        # def open_new_window():
        #     self.acess = Acess.Acess(self.main_frame)

        def open_new_window():
            self.window.destroy()
            acess = Acess.Acess()

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def loopVideo(event):
            videoplayer.play()

        canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(
            683.0,
            684.0,
            image=image_image_1
        )

        canvas.create_rectangle(
            0.0,
            0.0,
            1366.0,
            601.0,
            fill="#64C562",
            outline="")

        videoplayer = TkinterVideo(master=self.window,scaled=True,anchor="nw",
                         padx=0, pady=0)
        videoplayer.load(r"assets/frame0/video.mp4")
        videoplayer.place(x=0, y=0, width=1366, height=601)
        videoplayer.play()


        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=open_new_window,
            relief="flat"
        )
        button_1.place(
            x=383.0,
            y=632.0,
            width=600.0,
            height=105.35211181640625
        )

        videoplayer.bind('<<Ended>>', loopVideo)
        self.window.resizable(False, False)
        self.window.mainloop()
