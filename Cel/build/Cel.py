from tkinter import Tk

from Constants import DATA_STAGE_FILE


class Cel:
    def __init__(self,master=None):
        import json
        from pathlib import Path
        from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
        from Keyboard import KeyboardOneEntry
        from Cep.build import Cep

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Apollo\Desktop\UltimateRecicla\Cel\build\assets\frame0")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        def on_button_click():
            cel = entry_1.get()

            if cel == "":
                messagebox.showerror("Erro", "Por favor, preencha o campo.")
            else:
                try:
                    with open(DATA_STAGE_FILE, "r") as f:
                        data = json.load(f)
                except:
                    data = []

                data["cel"] = cel

                with open(DATA_STAGE_FILE, "w") as f:
                    f.write(json.dumps(data))
                self.window.destroy()
                cep = Cep.Cep()

        self.window = master if master else Tk()
        self.window.geometry("1366x768")
        self.window.configure(bg = "#FFFFFF")
        self.window.title("Recicla Machine")
        img = PhotoImage(file='assets/frame0/Icone.png')
        self.window.tk.call('wm', 'iconphoto', self.window._w, img)

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )


        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            683.0,
            384.0,
            image=image_image_1
        )

        self.canvas.create_text(
            32.0,
            160.0,
            anchor="nw",
            text="Vamos criar o \nseu cadastro",
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
            32.0,
            308.0,
            anchor="nw",
            text="É RAPIDINHO, PROMETO!",
            fill="#000000",
            font=("Aldrich Regular", 30 * -1)
        )

        self.canvas.create_text(
            787.0,
            141.0,
            anchor="nw",
            text="Qual o seu Celular?",
            fill="#000000",
            font=("Aldrich Regular", 40 * -1)
        )

        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            944.0,
            268.0,
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
            x=583.0,
            y=218.0,
            width=722.0,
            height=98.0
        )

        button_image_1 = PhotoImage(
                    file=relative_to_assets("button_1.png"))
        button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=on_button_click,
        relief="flat"
        )
        button_1.place(
        x=870.0,
        y=350.0,
        width=148.0,
        height=50.0
        )

        KeyboardOneEntry.create_keyboard(self.window,entry_1)

        self.canvas.create_rectangle(
            549.0,
            325.0,
            1334.0,
            330.0,
            fill="#000000",
            outline="")

        self.window.resizable(False, False)
        self.window.mainloop()
