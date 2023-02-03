from Keyboard import KeyboardTwoEntry

class Login:
    def __init__(self, master=None):
        import json
        from pathlib import Path
        from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
        from Menu.build import Menu

        self.window = master if master else Tk()
        self.window.title=("Recicla Machine")
        self.window.geometry("1366x768")
        self.window.configure(bg="#FFFFFF")
        img = PhotoImage(file='assets/frame0/icone.png')
        self.window.tk.call('wm','iconphoto',self.window._w,img)

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=768,
            width=1366,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

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
                self.window.destroy()
                menu = Menu.Menu()

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
            command=on_button_click
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
            command=lambda: on_button_click()
        )
        button_1.place(
            x=866.0,
            y=386.0,
            width=148.0,
            height=50.0
        )

        KeyboardTwoEntry.create_keyboard(self.window,entry_1,entry_2)

        # def create_keyboard(entry_1,entry_2):
        #
        #     allButtons = []
        #     DEF_WIDTG = 1366
        #     DEF_HEIGHT = 330
        #
        #     CONTRASTCLICK_COL = "#4169E1"
        #     row1 = ["q+/1", "w+/2", "e+/3", "r+/4", 't+/5', 'y+/6', 'u+/7', 'i+/8', 'o+/9', 'p+/0', "Backspace"]
        #     row2 = ["Caps", "a", "s", "d", "f", "g", "h", "j", "k", "l", "Enter"]
        #     row3 = ["Shift", "z", "x", "c", "v", "b", "n", "m", ",", ".", "?"]
        #     row4 = ["Simbolos", "@", " ", ".com", "<=", "=>"]
        #
        #     rows = [row1, row2, row3, row4]
        #
        #     shiftSp = row1[0:10]
        #     symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";",
        #                ":", "'",
        #                ",", ".", "/", "`", "~"]
        #     specials = ["Caps", "Shift", "Simbolos", "Backspace", "Enter", "<=", "=>", " "] + symbols
        #     nonLetterKey = specials
        #
        #     width15 = ["Caps"]
        #     width20 = ["<=", "=>", "Enter"]
        #     width25 = ["Shift", "Backspace"]
        #     width55 = [" "]
        #
        #     def on_enter(e):
        #         e.widget.configure(bg="#ccc", fg="#000")
        #         if btnLabels[e.widget]:
        #             btnLabels[e.widget].configure(bg="#ccc", fg="#666")
        #
        #     def on_leave(e):
        #         e.widget.configure(bg="#333", fg="#fff")
        #         if btnLabels[e.widget]:
        #             btnLabels[e.widget].configure(bg="#333", fg="#888")
        #
        #     index = 0
        #     letter_to_symbol = {"q": "!", "w": "@", "e": "#", "r": "$", "t": "%", "y": "^", "u": "&", "i": "*",
        #                         "o": "(",
        #                         "p": ")", "a": "-", "s": "_", "d": "+", "f": "=", "g": "[", "h": "]", "j": "{",
        #                         "k": "}",
        #                         "l": ";", "z": ",", "x": ".", "c": "/", "v": "`", "b": "~", "m": "'", "n": ":"}
        #     switched_buttons = []
        #
        #     caps_mode = False
        #     shift_mode = False
        #     symbols_mode = False
        #
        #     def handleClick(event):
        #         global shift_mode, symbols_mode, caps_mode
        #         text = event.widget['text']
        #         if text == "Backspace":
        #             current_widget = self.window.focus_get()
        #             if current_widget == entry_1:
        #                 entry_1.delete(len(entry_1.get()) - 1)
        #             elif current_widget == entry_2:
        #                 entry_2.delete(len(entry_2.get()) - 1)
        #         elif text == "<=":
        #             current_widget = self.window.focus_get()
        #             if current_widget == entry_1:
        #                 entry_1.icursor(entry_1.index(INSERT) - 1)
        #             elif current_widget == entry_2:
        #                 entry_2.icursor(entry_2.index(INSERT) - 1)
        #         elif text == "=>":
        #             current_widget = self.window.focus_get()
        #             if current_widget == entry_1:
        #                 entry_1.icursor(entry_1.index(INSERT) + 1)
        #             elif current_widget == entry_2:
        #                 entry_2.icursor(entry_2.index(INSERT) + 1)
        #         elif text == "Enter":
        #             current_widget = self.window.focus_get()
        #             if current_widget == entry_1:
        #                 entry_2.focus_set()
        #             elif current_widget == entry_2:
        #                 entry_1.focus_set()
        #         elif text == "Shift":
        #             shift_mode = not shift_mode
        #             for i, button in enumerate(row1[0:10]):
        #                 letter, number = button.split("+/")
        #                 if shift_mode:
        #                     allButtons[i].config(text=number)
        #                 else:
        #                     allButtons[i].config(text=letter)
        #         elif text == "Caps":
        #             #caps_mode = False
        #             caps_mode = not caps_mode
        #             for button in allButtons:
        #                 if button['text'].isalpha() and button['text'] not in specials and button['text'] != "Caps":
        #                     if caps_mode:
        #                         button.config(text=button['text'].upper())
        #                     else:
        #                         button.config(text=button['text'].lower())
        #         elif text == "Simbolos":
        #             symbols_mode = not symbols_mode
        #             if symbols_mode:
        #                 for button in allButtons:
        #                     if button['text'] not in nonLetterKey:
        #                         switched_buttons.append(button)
        #                         button['text'] = letter_to_symbol.get(button['text'], button['text'])
        #             else:
        #                 for button in switched_buttons:
        #                     button['text'] = next(
        #                         (letter for letter, symbol in letter_to_symbol.items() if symbol == button['text']),
        #                         button['text'])
        #                 switched_buttons.clear()
        #         else:
        #             current_widget = self.window.focus_get()
        #             if current_widget == entry_1:
        #                 entry_1.insert("end", text)
        #             elif current_widget == entry_2:
        #                 entry_2.insert("end", text)
        #
        #     # ACOMPANHA O BLOCO DE CÒDIGO ACIMA
        #     def symbol_on_release(event, btn):
        #         global index
        #         index = 0
        #
        #     btnLabels = {}
        #
        #     Y = 465
        #
        #     for r in rows:
        #         X = 4
        #         for i in r:
        #             btnWidth = 0.079 * DEF_WIDTG
        #             btnHeight = 0.2 * DEF_HEIGHT
        #
        #             padx = round(btnWidth / 9)
        #             pady = round(btnHeight / 10)
        #
        #             frame = tk.Frame(self.window, highlightbackground="#1E1E1E", highlightthickness=4)
        #
        #             if i in shiftSp:
        #                 anchor = "se"
        #                 labelT = i.split("+/")
        #                 label = tk.Label(self.window, text=labelT[1], fg="#888", bg="#333", font=font(size=11))
        #                 label.place(x=X + padx, y=Y + pady)
        #                 i = labelT[0]
        #             else:
        #                 anchor = "nw"
        #                 label = None
        #
        #             btn = tk.Button(frame, activebackground=CONTRASTCLICK_COL, text=i, bg="#333", fg="#fff",
        #                             relief="flat",
        #                             padx=padx,
        #                             pady=pady, borderwidth=0, anchor=anchor, font=font(size=15))
        #
        #             if i in width15:
        #                 btnWidth *= 1.5
        #             if i in width20:
        #                 btnWidth *= 2
        #             elif i in width25:
        #                 btnWidth *= 2.5
        #             elif i in width55:
        #                 btnWidth *= 5.5
        #
        #             btn.place(x=0, y=0, width=btnWidth, height=btnHeight)
        #             frame.place(x=X, y=Y, width=btnWidth, height=btnHeight)
        #
        #             X += btnWidth
        #
        #             btn.bind("<Button-1>", handleClick)
        #             btn.bind("<ButtonRelease-1>", on_enter)
        #             btn.bind("<Enter>", on_enter)
        #             btn.bind("<Leave>", on_leave)
        #
        #             btnLabels[btn] = label
        #             allButtons.append(btn)
        #
        #         Y += btnHeight
        #
        # create_keyboard(entry_1, entry_2)

        self.mainloop()