import tkinter as tk
from Quadro import Quadro
from Escultura import Escultura  
from tkinter import messagebox
from tkinter import ttk

lista = []

def cadastrarObra():
    titulo = entryTitulo.get()
    ano = entryAno.get()
    tipo = varTipo.get()
    artista = entryArtista.get()
    variavel = entryVariavel.get()
    
    if tipo == "Quadro":
        c = Quadro(titulo, artista, ano, variavel)
        lista.append(c)
        messagebox.showinfo("Cadastro", f"{tipo} cadastrado com sucesso!")
    else:
        t = Escultura(titulo, artista, ano, variavel)
        lista.append(t)
        messagebox.showinfo("Cadastro", f"{tipo} cadastrado com sucesso!")

def atualizarListbox():
    listbox.delete(0, tk.END)
    for obj in lista:
        listbox.insert(tk.END, obj.mostrar())

janela = tk.Tk()
janela.title("Cadastro de obra")
janela.geometry("800x600")

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

janelinha = ttk.Notebook(janela)
janelinha.grid(row=0, column=0, sticky="nsew")

tab1 = ttk.Frame(janelinha)
for i in range(6):
    tab1.grid_rowconfigure(i, weight=1)
tab1.grid_columnconfigure(0, weight=1)
tab1.grid_columnconfigure(1, weight=1)

tab2 = ttk.Frame(janelinha)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

janelinha.add(tab1, text="Cadastro")
janelinha.add(tab2, text="Lista")

# Labels e Entradas
tk.Label(tab1, text="Titulo:", font=("", 15)).grid(row=0, column=0, sticky="w", padx=10)
entryTitulo = tk.Entry(tab1, font=("", 15))
entryTitulo.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Ano:", font=("", 15)).grid(row=1, column=0, sticky="w", padx=10)
entryAno = tk.Entry(tab1, font=("", 15))
entryAno.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Cor/Modelo:", font=("", 15)).grid(row=2, column=0, sticky="w", padx=10)
entryVariavel = tk.Entry(tab1, font=("", 15))
entryVariavel.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Artista:", font=("", 15)).grid(row=3, column=0, sticky="w", padx=10)
entryArtista = tk.Entry(tab1, font=("", 15))
entryArtista.grid(row=3, column=1, sticky="nsew", padx=10, pady=5)

tk.Label(tab1, text="Tipo:", font=("", 15)).grid(row=4, column=0, sticky="w", padx=10)
varTipo = tk.StringVar(value="Quadro")
tk.Radiobutton(tab1, text="Quadro", font=("", 15), variable=varTipo, value="Quadro").grid(row=4, column=1, sticky="w", padx=10, pady=5)
tk.Radiobutton(tab1, text="Escultura", font=("", 15), variable=varTipo, value="Escultura").grid(row=4, column=1, sticky="e", padx=10, pady=5)

tk.Button(tab1, text="Cadastrar", font=("", 15), command=cadastrarObra).grid(row=5, columnspan=2)

# Listbox para exibição das obras cadastradas
listbox = tk.Listbox(tab2)
listbox.config(font=("", 15))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)
tk.Button(tab2, text="Atualizar", font=("", 15), command=atualizarListbox).grid(row=1, column=0)

janela.mainloop()
