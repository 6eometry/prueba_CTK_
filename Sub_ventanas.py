import tkinter as tk
from tkinter import ttk
from tkinter import *
from time import strftime


def sub_ventana():
    def actualizar_tiempo():
        tiempo_actual = strftime('%H:%M:%S')  # Formato de 24 horas
        fecha_actual = strftime('%Y/%m/%d')  # Formato de fecha
        etiqueta_hora.config(text=tiempo_actual)
        etiqueta_fecha.config(text=fecha_actual)
        etiqueta_hora.after(1000, actualizar_tiempo)  # Actualiza cada segundo

    sub_ven = tk.Tk()
    sub_ven.title("SubVentana Principal Del Programa")
    h_v, w_v = (600, 800)
    w_p, h_p = (sub_ven.winfo_screenwidth(), sub_ven.winfo_screenheight())
    pos_x = (w_p // 2) - (w_v // 2)
    pos_y = (h_p // 2) - (h_v // 2)
    sub_ven.geometry(f"{w_v}x{h_v}+{pos_x}+{pos_y}")
    sub_ven.resizable(width=False, height=False)



    #Frame_Principal_superior
    frame_1 = tk.Frame(sub_ven, bd=0, height=25, relief=tk.SOLID)
    frame_1.pack(side=TOP, expand=FALSE, fill=tk.X)
    # Label_perfil
    #label_name = tk.Label(frame_1, text=)
    #label_name.pack(side=LEFT)
    #label_hora
    etiqueta_hora = tk.Label(frame_1, font=('Arial', 10), fg='black')
    etiqueta_hora.pack(side=RIGHT)

    etiqueta_fecha = tk.Label(frame_1, font=('Arial', 10), fg='black')
    etiqueta_fecha.pack(side=RIGHT)

    actualizar_tiempo()
    #Frame_inicio_boton
    #frame_inicio = tk.Frame(frame_1,bd=0, height=32, width=32, relief=tk.SOLID, padx=5, pady=5, bg="pink")
    #frame_inicio.pack(side=LEFT, anchor=tk.N)


    #Frame_Pestañas
    frame_pest = tk.Frame(sub_ven, bd=0, relief=tk.SOLID, bg="light blue")
    frame_pest.pack(side=BOTTOM, fill=tk.BOTH, expand=YES)

    pest = ttk.Notebook(frame_pest)
    pest.pack(fill=BOTH, expand=True)

    tab1 = ttk.Frame(pest)
    pest.add(tab1, text="Ingreso de articulos")

    tab2 = ttk.Frame(pest)
    pest.add(tab2, text="Registro de artículo nuevo")

    frame_tab2 = tk.Frame(tab2, bd=0, height=20, bg="light blue")
    frame_tab2.pack(side=TOP, fill=tk.X, expand=FALSE)

    frame_tab2 = tk.Frame(tab2, bd=0, height=20, bg="light green")
    frame_tab2.pack(side=TOP, fill=tk.BOTH, expand=FALSE)

    label_codigo = tk.Label(frame_tab2, text="Codigo de Artículo :")
    label_codigo.pack(side=tk.LEFT)
    codigo = tk.Entry(frame_tab2)
    codigo.pack(side=tk.LEFT)
    #panel_pestañas
    #pest = ttk.Notebook(sub_ven)
    #pest.pack(fill=BOTH, expand=YES)


    sub_ven.mainloop()





    return sub_ven

