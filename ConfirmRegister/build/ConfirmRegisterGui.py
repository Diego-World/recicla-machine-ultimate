
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Apollo\Desktop\python-figma\tela10\build\assets\frame0")


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
    384.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=46.0,
    y=604.0,
    width=600.0,
    height=105.35211181640625
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=699.0,
    y=604.0,
    width=600.0,
    height=105.35211181640625
)

canvas.create_text(
    32.0,
    242.0,
    anchor="nw",
    text="Perfeito!",
    fill="#000000",
    font=("Aldrich Regular", 60 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    223.0,
    84.0,
    image=image_image_2
)

canvas.create_text(
    32.0,
    308.0,
    anchor="nw",
    text="Agora, por favor ",
    fill="#000000",
    font=("Aldrich Regular", 30 * -1)
)

canvas.create_text(
    646.0,
    26.0,
    anchor="nw",
    text="Nome",
    fill="#000000",
    font=("Aldrich Regular", 40 * -1)
)

canvas.create_text(
    32.0,
    350.0,
    anchor="nw",
    text="CONFIRA SEUS DADOS",
    fill="#000000",
    font=("Aldrich Regular", 24 * -1)
)

canvas.create_text(
    646.0,
    119.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("Aldrich Regular", 40 * -1)
)

canvas.create_text(
    646.0,
    216.0,
    anchor="nw",
    text="CPF",
    fill="#000000",
    font=("Aldrich Regular", 40 * -1)
)

canvas.create_text(
    646.0,
    328.0,
    anchor="nw",
    text="Celular",
    fill="#000000",
    font=("Aldrich Regular", 40 * -1)
)

canvas.create_text(
    646.0,
    429.0,
    anchor="nw",
    text="CEP",
    fill="#000000",
    font=("Aldrich Regular", 40 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1047.5,
    50.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=796.0,
    y=26.0,
    width=503.0,
    height=47.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1047.5,
    143.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=796.0,
    y=119.0,
    width=503.0,
    height=47.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1047.5,
    240.5,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=796.0,
    y=216.0,
    width=503.0,
    height=47.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1047.5,
    342.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=796.0,
    y=318.0,
    width=503.0,
    height=47.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    1047.5,
    453.5,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=796.0,
    y=429.0,
    width=503.0,
    height=47.0
)
window.resizable(False, False)
window.mainloop()