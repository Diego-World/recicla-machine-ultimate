import tkinter as tk
import json

class Form:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulário de Registro")
        self.root.geometry("500x500")
        
        self.label_nome = tk.Label(self.root, text="Nome")
        self.label_nome.pack()
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()

        self.label_data_nasc = tk.Label(self.root, text="Data de Nascimento")
        self.label_data_nasc.pack()
        self.entry_data_nasc = tk.Entry(self.root)
        self.entry_data_nasc.pack()

        self.label_endereco = tk.Label(self.root, text="Endereço")
        self.label_endereco.pack()
        self.entry_endereco = tk.Entry(self.root)
        self.entry_endereco.pack()

        self.label_cep = tk.Label(self.root, text="CEP")
        self.label_cep.pack()
        self.entry_cep = tk.Entry(self.root)
        self.entry_cep.pack()

        self.label_celular = tk.Label(self.root, text="Celular")
        self.label_celular.pack()
        self.entry_celular = tk.Entry(self.root)
        self.entry_celular.pack()

        self.label_email = tk.Label(self.root, text="Email")
        self.label_email.pack()
        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        nome = self.entry_nome.get()
        data_nasc = self.entry_data_nasc.get()
        endereco = self.entry_endereco.get()
        cep = self.entry_cep.get()
        celular = self.entry_celular.get()
        email = self.entry_email.get()

        try:
            with open("registros.json", "r") as file:
                data = json.load(file)
        except:
            data = []
        
        registro = {
            "id": len(data) + 1,
            "nome": nome,
            "data_nasc": data_nasc,
            "endereco": endereco,
            "cep": cep,
            "celular": celular,
            "email": email
        }

        self.entry_nome.delete(0, tk.END)
        self.entry_data_nasc.delete(0, tk.END)
        self.entry_endereco.delete(0, tk.END)
        self.entry_cep.delete(0, tk.END)
        self.entry_celular.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_nome.focus()

        with open("registros.json", "a") as file:
            file.write(json.dumps(registro))
            file.write("\n")
            
#        with open("registros.json", "w") as file:
#            for item in data:
#                file.write(json.dumps(item))
#                file.write("\n")

            
root = tk.Tk()
app = Form(root)
root.mainloop()
