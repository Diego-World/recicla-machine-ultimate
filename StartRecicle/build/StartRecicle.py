from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class StartRecicle:
    def __init__(self,master=None):
        self.window = master if master else Tk()
        self.window.geometry("1366x768")
        self.window.configure(bg = "#FFFFFF")
        self.window.title("Recicla Machine")
        img = PhotoImage(file='assets/Icone.png')
        self.window.tk.call('wm', 'iconphoto',self.window._w, img)

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Apollo\Desktop\UltimateRecicla\StartRecicle\build\assets\frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

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
            66.0,
            166.0,
            anchor="nw",
            text="Vamos começar a incluir os itens",
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
            298.0,
            336.0,
            anchor="nw",
            text="APONTE O\n CÓDIGO DE\n BARRAS\n PARA O LEITOR\n",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
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
            x=736.0,
            y=598.0,
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
            x=32.0,
            y=598.0,
            width=600.0,
            height=105.35211181640625
        )

        canvas.create_text(
            230.0,
            336.0,
            anchor="nw",
            text="01",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        canvas.create_text(
            539.0,
            336.0,
            anchor="nw",
            text="02",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        canvas.create_text(
            608.0,
            336.0,
            anchor="nw",
            text="INSIRA O\n ITEM NO\n COLETOR",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        canvas.create_text(
            821.0,
            351.0,
            anchor="nw",
            text="03\n",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        canvas.create_text(
            882.0,
            336.0,
            anchor="nw",
            text="REPITA O\n PROCESSO\n ATÉ O FIM\n DOS ITENS",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )
        self.window.resizable(False, False)
        self.window.mainloop()
