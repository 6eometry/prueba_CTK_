import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

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
        ventana()
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


#VENTANA PRINCIPAL //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def ventana():

    def actualizar_tiempo():
        label_time.config(text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        frame_1.after(1000, actualizar_tiempo)

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


    #Label_Time
    label_time = tk.Label(frame_1, font=("times", 10))
    label_time.pack(side=RIGHT)
    actualizar_tiempo()


    boton3 = tk.Button(frame_inicio, text="Ingreso de articulos porque fer se confunde", font=("Times", 10), bg="Pale Turquoise", bd=0,
                       command=sub_ventana)
    boton3.pack(fill=tk.X, padx=100, pady=0)




    ven_prog.mainloop()



    return ven_prog

#SUBVENTANA DE INGRESO //////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def sub_ventana():

    def actualizar_tiempo():
        label_time1.config(text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        frame_1.after(1000, actualizar_tiempo)


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


    label_time1 = tk.Label(frame_1, font=('times', 10))
    label_time1.pack(side=RIGHT)
    actualizar_tiempo()

    #Frame_inicio_boton
    #frame_inicio = tk.Frame(frame_1,bd=0, height=32, width=32, relief=tk.SOLID, padx=5, pady=5, bg="pink")
    #frame_inicio.pack(side=LEFT, anchor=tk.N)


    #Frame_Pestañas
    frame_pest = tk.Frame(sub_ven, bd=0, relief=tk.SOLID, bg="light blue")
    frame_pest.pack(side=BOTTOM, fill=tk.BOTH, expand=YES)

    #CREACION DE PESATAÑAS
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

    #INGRESAR CODIGO DEL ARTICULO

    label_codigo = tk.Label(frame_tab2, text="Codigo de Artículo :")
    label_codigo.pack(side=tk.LEFT)
    codigo = tk.Entry(frame_tab2)
    codigo.pack(side=tk.LEFT)

    #INGRESAR DESCRIPCION DEL ARTICULO

    label_des = tk.Label(frame_tab2, text="Descipción del Artículo :")
    label_des.pack(side=tk.LEFT)
    descripcion = tk.Entry(frame_tab2)
    descripcion.pack(side=tk.LEFT)


    return sub_ven.mainloop()

ven1.mainloop()

