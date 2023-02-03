from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from tkVideoPlayer import TkinterVideo
from Acess.build import Acess

def open_new_window():
    window.destroy()
    acess = Acess.Acess()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Apollo\Desktop\python-figma\tela01\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1366x768")
window.configure(bg = "#FFFFFF")
window.title("Recicla Machine")
img = PhotoImage(file='assets/frame0/Icone.png')
window.tk.call('wm', 'iconphoto', window._w, img)

canvas = Canvas(
    window,
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

def loopVideo(event):
    videoplayer.play()

canvas.create_rectangle(
    0.0,
    0.0,
    1366.0,
    601.0,
    fill="#64C562",
    outline="")

videoplayer = TkinterVideo(master=window,scaled=True,anchor="nw",
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
window.resizable(False, False)
window.mainloop()
