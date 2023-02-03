import json
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from keyboard08 import create_keyboard

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Apollo\Desktop\python-figma\TelaDeLogin\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

data = {}

def on_button_click():
    username = entry_1.get()
    password = entry_2.get()

    if username == "" or password == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    else:
        try:
            with open("loginData.json", "r") as f:
                data = json.load(f)
        except:
            data = []

        entry = {"username": username, "password": password}
        data.append(entry)

        with open("loginData.json", "w") as f:
            json.dump(data, f)

        messagebox.showinfo("Sucesso", "Dados salvos com sucesso.")

window = Tk()

window.geometry("1366x768")
window.configure(bg = "#FFFFFF")
img = PhotoImage(file='assets/frame0/icone.png')
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

canvas.create_text(
    58.0,
    202.0,
    anchor="nw",
    text="Informe seus\ndados para \nacessar sua conta",
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
    826.0,
    11.0,
    anchor="nw",
    text="Email ou CPF",
    fill="#000000",
    font=("Aldrich Regular", 40 * -1)
)


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    948.5,
    114.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Arial 35")
)

entry_1.place(
    x=615.0,
    y=64.0,
    width=667.0,
    height=98.0,
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    948.5,
    296.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Arial 35")
)
entry_2.place(
    x=615.0,
    y=246.0,
    width=667.0,
    height=98.0
)

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=lambda:on_button_click()
)
button_1.place(
    x=866.0,
    y=386.0,
    width=148.0,
    height=50.0
)

keyboard = create_keyboard(window,entry_1,entry_2)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

canvas.create_text(
    58.0,
    202.0,
    anchor="nw",
    text="Informe seus\ndados para \nacessar sua conta",
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
    885.0,
    195.0,
    anchor="nw",
    text="Senha",
    fill="#000000",
    font=("Aldrich Regular", 40 * -1)
)


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    948.5,
    114.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Arial 35")
)

entry_1.place(
    x=615.0,
    y=64.0,
    width=667.0,
    height=98.0,
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    948.5,
    296.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font=("Arial 35")
)
entry_2.place(
    x=615.0,
    y=246.0,
    width=667.0,
    height=98.0
)

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    relief="flat",
    command=lambda:on_button_click()
)
button_1.place(
    x=866.0,
    y=386.0,
    width=148.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()
