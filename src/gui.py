import tkinter as tk

def launch_app():
    root = tk.Tk()
    root.title("Système de Recherche d'Information")

    label = tk.Label(root, text="Entrez votre requête :")
    label.pack()

    entry = tk.Entry(root, width=50)
    entry.pack()

    root.mainloop()