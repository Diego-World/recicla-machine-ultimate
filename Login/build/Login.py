from Constants import DATA_STAGE_LOGIN_FILE
from Keyboard import KeyboardTwoEntry
from StageLoginHelper import copy_login_data_stage_to_master
import json
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from Menu.build import Menu

class Login:
    def __init__(self, master=None):
        self.window = master if master else Tk()
        self.window.title=("Recicla Machine")
        self.window.geometry("1366x768")
        self.window.configure(bg="#FFFFFF")
        img = PhotoImage(file='assets/Icone.png')
        self.window.tk.call('wm','iconphoto',self.window._w,img)

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Apollo\Desktop\python-figma\TelaDeLogin\build\assets\frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def save_Login():
            username = entry_1.get()
            password = entry_2.get()

            if username == "" or password == "":
                messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            else:
                try:
                    with open(DATA_STAGE_LOGIN_FILE, "r") as f:
                        data = json.load(f)
                except:
                    data = []

                dic = {
                    "username": username,
                    "password": password
                }
                with open(DATA_STAGE_LOGIN_FILE, "w") as f:
                    f.write(json.dumps(dic))

        def destroy_call():
            self.window.destroy()
            menu = Menu.Menu()

        def save_login_data():
            save_Login()
            copy_login_data_stage_to_master()
            destroy_call()

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            683.0,
            384.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))

        self.canvas.create_text(
            58.0,
            202.0,
            anchor="nw",
            text="Informe seus\ndados para \nacessar sua conta",
            fill="#000000",
            font=("Aldrich Regular", 60 * -1)
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            223.0,
            84.0,
            image=image_image_2
        )

        self.canvas.create_text(
            826.0,
            11.0,
            anchor="nw",
            text="Email ou CPF",
            fill="#000000",
            font=("Aldrich Regular", 40 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
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
        entry_bg_2 = self.canvas.create_image(
            948.5,
            296.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial 35"),
            show="*"
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
            command=save_login_data
        )
        button_1.place(
            x=866.0,
            y=386.0,
            width=148.0,
            height=50.0
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))

        self.canvas.create_text(
            58.0,
            202.0,
            anchor="nw",
            text="Informe seus\ndados para \nacessar sua conta",
            fill="#000000",
            font=("Aldrich Regular", 60 * -1)
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            223.0,
            84.0,
            image=image_image_2
        )

        self.canvas.create_text(
            885.0,
            195.0,
            anchor="nw",
            text="Senha",
            fill="#000000",
            font=("Aldrich Regular", 40 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
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
        entry_bg_2 = self.canvas.create_image(
            948.5,
            296.0,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
            font=("Arial 35"),
            show=("*")
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
            command=save_login_data
        )
        button_1.place(
            x=866.0,
            y=386.0,
            width=148.0,
            height=50.0
        )

        KeyboardTwoEntry.create_keyboard(self.window,entry_1,entry_2)

        self.mainloop()