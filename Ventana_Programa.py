import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import Sub_ventanas
from time import strftime



def ventana():

    def actualizar_tiempo():
        tiempo_actual = strftime('%H:%M:%S')  # Formato de 24 horas
        fecha_actual = strftime('%Y/%m/%d')  # Formato de fecha
        etiqueta_hora.config(text=tiempo_actual)
        etiqueta_fecha.config(text=fecha_actual)
        etiqueta_hora.after(1000, actualizar_tiempo)  # Actualiza cada segundo

    # Función para manejar el cierre de la ventana
    def on_closing():
        if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
            ven_prog.destroy()  # Cierra la ventana si el usuario confirma


    ven_prog = tk.Tk()
    ven_prog.title("Ventana Principal Del Programa")
    h_v, w_v = (600, 800)
    w_p, h_p = (ven_prog.winfo_screenwidth(), ven_prog.winfo_screenheight())
    pos_x = (w_p // 2) - (w_v // 2)
    pos_y = (h_p // 2) - (h_v // 2)
    ven_prog.geometry(f"{w_v}x{h_v}+{pos_x}+{pos_y}")
    ven_prog.resizable(width=False, height=False)
    ven_prog.protocol("WM_DELETE_WINDOW", on_closing)

    #Frame_principal_sup
    frame_1 = tk.Frame(ven_prog, bd=0, height=25, relief=tk.SOLID)
    frame_1.pack(side=TOP, expand=FALSE, fill=tk.X)
    #Frame_inicio
    frame_inicio = tk.Frame(ven_prog,bd=0, height=100, relief=tk.SOLID, padx=10, pady=10, bg="light green")
    frame_inicio.pack(side="top", expand=tk.NO, fill=tk.BOTH)


    #Label_perfil
    label_name = tk.Label(frame_1, text="usario")
    label_name.pack(side=LEFT)


    etiqueta_hora = tk.Label(frame_1, font=('Arial', 10), fg='black')
    etiqueta_hora.pack(side=RIGHT)

    etiqueta_fecha = tk.Label(frame_1, font=('Arial', 10), fg='black')
    etiqueta_fecha.pack(side=RIGHT)

    actualizar_tiempo()


    boton3 = tk.Button(frame_inicio, text="Ingreso de articulos porque fer se confunde", font=("Times", 10), bg="Pale Turquoise", bd=0,
                       command= Sub_ventanas.sub_ventana)
    boton3.pack(fill=tk.X, padx=100, pady=0)




    ven_prog.mainloop()



    return ven_prog


