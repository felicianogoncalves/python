import json
import tkinter as tk
from tkinter import messagebox, simpledialog

# --- Dados ---
tarefas = []

def carregar():
    global tarefas
    try:
        with open("memoria_tarefas.json", "r", encoding="utf-8") as f:
            tarefas = json.load(f)
    except FileNotFoundError:
        tarefas = []

def salvar():
    with open("memoria_tarefas.json", "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=2)

# --- Funções de lógica ---
def atualizar_lista():
    lista_tarefas.delete(0, tk.END)
    for t in tarefas:
        status = "✔ Concluída" if t["concluida"] else "❌ Pendente"
        lista_tarefas.insert(tk.END, f"{t['descricao']} - {status}")

def adicionar_tarefa():
    desc = simpledialog.askstring("Nova Tarefa", "Digite a tarefa:")
    if desc:
        tarefas.append({"descricao": desc, "concluida": False})
        atualizar_lista()
        salvar()

def concluir_tarefa():
    sel = lista_tarefas.curselection()
    if not sel:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para concluir.")
        return
    index = sel[0]
    tarefas[index]["concluida"] = True
    atualizar_lista()
    salvar()
    if messagebox.askyesno("Remover?", "Quer remover esta tarefa da lista?"):
        tarefas.pop(index)
        atualizar_lista()
        salvar()

def remover_tarefa():
    sel = lista_tarefas.curselection()
    if not sel:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")
        return
    index = sel[0]
    tarefas.pop(index)
    atualizar_lista()
    salvar()

# --- Interface ---
root = tk.Tk()
root.title("📋 To-Do List")
root.geometry("500x400")
root.resizable(False, False)

# Cabeçalho
titulo = tk.Label(root, text="Minhas Tarefas", font=("Helvetica", 20, "bold"), fg="#333")
titulo.grid(row=0, column=0, columnspan=3, pady=15)

# Lista de tarefas
lista_tarefas = tk.Listbox(root, width=50, height=15, font=("Helvetica", 12))
lista_tarefas.grid(row=1, column=0, columnspan=3, padx=10)

# Botões
btn_adicionar = tk.Button(root, text="➕ Adicionar", command=adicionar_tarefa,
                          bg="#4CAF50", fg="white", width=12, font=("Helvetica", 12, "bold"))
btn_adicionar.grid(row=2, column=0, padx=5, pady=10)

btn_concluir = tk.Button(root, text="✅ Concluir", command=concluir_tarefa,
                         bg="#2196F3", fg="white", width=12, font=("Helvetica", 12, "bold"))
btn_concluir.grid(row=2, column=1, padx=5, pady=10)

btn_remover = tk.Button(root, text="🗑 Remover", command=remover_tarefa,
                        bg="#f44336", fg="white", width=12, font=("Helvetica", 12, "bold"))
btn_remover.grid(row=2, column=2, padx=5, pady=10)

carregar()
atualizar_lista()

root.mainloop()

