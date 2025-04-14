import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import Ventana_Programa

usuarios = {
        "s":"2"
}


ven1 = tk.Tk()
ven1.title("Ventana Principal")
al_v, an_v = (600, 800)
an_p, al_p = (ven1.winfo_screenwidth(), ven1.winfo_screenheight())

pos_x = (an_p // 2) - (an_v // 2)
pos_y = (al_p // 2) - (al_v // 2)

ven1.geometry(f"{an_v}x{al_v}+{pos_x}+{pos_y}")
ven1.resizable(width=False, height=False)


#Frame_Panel

frame_panel = tk.Frame(ven1, bd=0, width=400, relief=tk.SOLID, padx=10, pady=10, bg="#00DB9A")
frame_panel.pack(side="left", expand=tk.NO, fill=tk.BOTH)
#label = tk.Label(frame_panel, text="Logo", bg="Pale Turquoise")
#label.place(x=0, y=0, relwidth=1, relheight=1)


#Frame_Titulo
frame_title = tk.Frame(ven1, bd=0, height=50, relief=tk.SOLID, bg="#333333")
frame_title.pack(side="top", fill=tk.X)

title = tk.Label(frame_title, text="Inicio de Sesión", font=("Times", 20), bg="#333333", fg="#00DB9A", pady=50)
title.pack(expand=tk.YES, fill=tk.BOTH)

#Frame_2
frame_2 = tk.Frame(ven1, height=50, bd=0, relief=tk.SOLID, bg="#333333")
frame_2.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)


def verificar_mi_usuario():
    usuario1 = usuario.get()
    passw1 = passw.get()
    if usuario1 in usuarios and usuarios[usuario1] == passw1:
        ven1.destroy()
        Ventana_Programa.ventana(usuario1)
    else:
        messagebox.showerror("Error", "Usuario no es valido")

#Etiqueta_de_usuario_con_entrada
label_usuario = tk.Label(frame_2, text="Usuario", font=("Times", 15), bg="#333333", fg="#FFFFFF", anchor=tk.W)
label_usuario.pack(fill=tk.X, padx=20, pady=5)
usuario = Entry(frame_2, font=("Times", 12), bg="#FFFFFF")
usuario.pack(fill=tk.X, padx=24, pady=5)

#Etiqueta_de_contraseña_con_entrada
label_pass = tk.Label(frame_2, text="Contraseña", font=("Times", 15), bg="#333333", fg="#FFFFFF", anchor=tk.W)
label_pass.pack(fill=tk.X, padx=20, pady=5)
passw = Entry(frame_2, font=("Times", 12), bg="#FFFFFF")
passw.pack(fill=tk.X, padx=24, pady=5)
passw.config(show="*")
passw.bind("<Return>",  (lambda event: verificar_mi_usuario() ))

iniciar_sesion = tk.Button(frame_2, text="Iniciar Sesión", font=("Times", 10), bg="#00DB9A", bd=3, relief=RAISED, command=verificar_mi_usuario)
iniciar_sesion.pack(fill=tk.X, padx=100, pady=20)
iniciar_sesion.bind("<Return>", (lambda event: verificar_mi_usuario()))



ven1.mainloop()