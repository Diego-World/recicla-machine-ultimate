from tkinter import Tk
from Login.build import Login
from Username.build import Username

class Acess:
    def __init__(self, master=None):
        from pathlib import Path
        from tkinter import Tk, Canvas,Button, PhotoImage

        self.window = master if master else Tk()
        self.window.geometry("1366x768")
        self.window.title("Recicla Machine")
        self.window.configure(bg="#FFFFFF")
        img = PhotoImage(file='assets/Icone.png')
        self.window.tk.call('wm','iconphoto',self.window._w,img)

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Apollo\Desktop\python-figma\tela02\build\assets\frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def open_login_window():
            self.window.destroy()
            login = Login.Login()

        def open_create_username_window():
            self.window.destroy()
            username = Username.Username()

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

        self.canvas.create_text(
            362.0,
            276.0,
            anchor="nw",
            text="Você já possui conta?",
            fill="#000000",
            font=("Aldrich Regular", 64 * -1)
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            278.0,
            87.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=open_create_username_window,
            relief="flat"
        )
        button_1.place(
            x=721.0,
            y=483.0,
            width=600.0,
            height=105.35211181640625
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=open_login_window,
            relief="flat"
        )
        button_2.place(
            x=46.0,
            y=483.0,
            width=600.0,
            height=105.35211181640625
        )

        self.mainloop()