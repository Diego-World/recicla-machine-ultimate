from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from AccountCreated.build import AccountCreated

class Password:
    def __init__(self,master=None):
        self.window = master if master else Tk()
        self.window.geometry("1366x768")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Recicla Machine")
        img = PhotoImage(file='assets/Icone.png')
        self.window.tk.call('wm', 'iconphoto', self.window._w, img)

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Apollo\Desktop\UltimateRecicla\Password\build\assets\frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def create_account():
            self.window.destroy()
            accountCreate = AccountCreated.AccountCreated()

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
            384.0,
            image=image_image_1
        )

        canvas.create_text(
            486.0,
            243.0,
            anchor="nw",
            text="Senha de acesso",
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
            486.0,
            320.0,
            anchor="nw",
            text="Foi encaminhado para o seu e-mail uma senha aleatória.",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=create_account,
            relief="flat"
        )
        button_1.place(
            x=383.0,
            y=584.0,
            width=600.0,
            height=105.35211181640625
        )

        image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(
            350.0,
            318.0,
            image=image_image_3
        )

        canvas.create_text(
            486.0,
            399.0,
            anchor="nw",
            text="Não se preocupe, será possível alterar posteriormente.",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )
        self.window.resizable(False, False)
        self.window.mainloop()
