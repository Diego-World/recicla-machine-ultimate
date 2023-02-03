from tkinter import Tk

class Menu:
    def __init__(self,master=None):
        from pathlib import Path
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

        self.window = master if master else Tk()
        self.window.geometry("1366x768")
        self.window.configure(bg = "#FFFFFF")
        self.window.title("Recicla Machine")
        img = PhotoImage(file='assets/frame0/Icone.png')
        self.window.tk.call('wm', 'iconphoto', self.window._w, img)

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 768,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Apollo\Desktop\UltimateRecicla\Menu\build\assets\frame0")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            683.0,
            384.0,
            image=image_image_1
        )

        self.canvas.create_text(
            310.0,
            276.0,
            anchor="nw",
            text="O que você deseja fazer?",
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
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=729.0,
            y=384.0,
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
            x=30.0,
            y=384.0,
            width=600.0,
            height=105.35211181640625
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=382.0,
            y=552.0,
            width=600.0,
            height=105.35211181640625
        )
        self.window.resizable(False, False)
        self.window.mainloop()
