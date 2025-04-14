import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import sqlite3
import pandas as pd
import os

# Configuración de rutas y base de datos
base_dir = os.path.dirname(__file__)
db_path = os.path.join(base_dir, "base_de_datos.db")

# Variables globales
fila_seleccionada = None
conexion = None
cursor = None


# Inicializar conexión a la base de datos
def iniciar_conexion():
    global conexion, cursor
    try:
        conexion = sqlite3.connect(db_path)
        cursor = conexion.cursor()
        return True
    except sqlite3.Error as e:
        messagebox.showerror("Error de Base de Datos", f"No se pudo conectar a la base de datos: {e}")
        return False


# Función para cerrar la ventana principal (login)
def on_closing_main():
    try:
        # Cerrar la conexión a la base de datos si está abierta
        if conexion:
            conexion.close()
        ventana.quit()  # Detén el bucle principal
        ventana.destroy()  # Destruye la ventana de forma segura
    except Exception as e:
        print(f"Error al cerrar la ventana principal: {e}")


# Función para verificar usuario
def verificar_mi_usuario():
    usuario_passw = (usuario.get(), passw.get())
    cursor.execute("SELECT * FROM usuarios")
    filas = cursor.fetchall()
    if usuario_passw in filas:
        ventana.withdraw()  # Oculta la ventana en lugar de destruirla
        ventana2()
        #on_closing_main()
    else:
        messagebox.showerror("Error", "Usuario no válido")


# Configuración inicial de CustomTkinter mabsdjksahgdkjsad
ctk.set_appearance_mode("dark")  # Opciones: "dark", "light", "system"
ctk.set_default_color_theme("blue")  # Opciones: "blue", "green", "dark-blue"

# Iniciar conexión a la base de datos
if not iniciar_conexion():
    exit(1)  # Salir si no se puede conectar a la base de datos

# Ventana principal
ventana = ctk.CTk()
ventana.title("Ventana Principal")
al_v, an_v = (600, 800)
an_p, al_p = (ventana.winfo_screenwidth(), ventana.winfo_screenheight())
pos_x = (an_p // 2) - (an_v // 2)
pos_y = (al_p // 2) - (al_v // 2)
ventana.geometry(f"{an_v}x{al_v}+{pos_x}+{pos_y}")
ventana.resizable(False, False)
ventana.protocol("WM_DELETE_WINDOW", on_closing_main)

# Frame lateral (panel)
frame_panel = ctk.CTkFrame(ventana, width=400, corner_radius=0, fg_color="#00DB9A")
frame_panel.pack(side="left", fill="y")

# Título (en panel superior)
frame_title = ctk.CTkFrame(ventana, height=80, corner_radius=10, fg_color="#333333")
frame_title.pack(side="top", fill="x", padx=20, pady=20)

title = ctk.CTkLabel(frame_title, text="Inicio de Sesión", font=ctk.CTkFont("Arial", 24, weight="bold"),
                     text_color="#00DB9A")
title.pack(expand=True, fill="both", pady=20)

# Frame para los campos de usuario y contraseña
frame_centro = ctk.CTkFrame(ventana, corner_radius=10, fg_color="#333333")
frame_centro.pack(side="top", expand=True, fill="both", padx=20, pady=20)

# Etiqueta y campo de entrada para usuario
label_usuario = ctk.CTkLabel(frame_centro, text="", font=ctk.CTkFont("Arial", 16), text_color="#FFFFFF", anchor='w')
label_usuario.pack(fill='x', pady=10, padx=60)

usuario = ctk.CTkEntry(frame_centro, placeholder_text="Usuario", height=40, justify="center")
usuario.pack(fill="x", padx=60, pady=5)

# Etiqueta y campo de entrada para contraseña
label_pass = ctk.CTkLabel(frame_centro, text="", font=ctk.CTkFont("Arial", 16), text_color="#FFFFFF", anchor='w')
label_pass.pack(fill='x', pady=5, padx=60)
label_pass.pack(pady=10)

passw = ctk.CTkEntry(frame_centro, placeholder_text="Contraseña", show="*", height=40, justify="center")
passw.pack(fill="x", padx=60, pady=0)
passw.bind("<Return>", lambda event: verificar_mi_usuario())

# Botón de inicio de sesión
iniciar_sesion = ctk.CTkButton(frame_centro, text="Iniciar Sesión", text_color="black", command=verificar_mi_usuario,
                               fg_color="#00DB9A")
iniciar_sesion.pack(pady=55)


def ventana2():
    # Función para cerrar la ventana secundaria (aplicación principal)
    def on_closing_secondary():
        if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
            try:
                ventana2.quit()  # Detén el bucle principal
                ventana2.destroy()  # Destruye la ventana de forma segura
                #ventana.deiconify()  # Muestra la ventana de login nuevamente
            except Exception as e:
                print(f"Error al cerrar la ventana secundaria: {e}")

    # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def mostrar_contenido1():
        def actualizar_tiempo():
            hora_fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            label_time.configure(text=hora_fecha_actual)
            label_time.after(1000, actualizar_tiempo)

        label_time = ctk.CTkLabel(frame_principal, font=("times", 15), corner_radius=10)
        label_time.place(relx=0.99, rely=0.02, anchor='e')

        actualizar_tiempo()

        # FRAME BOTONES SUPERIORES
        frame_botones = ctk.CTkFrame(frame_principal, height=20, width=600, fg_color='transparent', corner_radius=10)
        frame_botones.place(relx=0, rely=0.04)
        frame_botones.pack_propagate(False)

        # FRAME DE CONTENNIDO DE BOTONES SUPERIORES
        frame_contenido = ctk.CTkFrame(frame_principal, fg_color="transparent", height=535, width=600,
                                       corner_radius=10)  # cambiar color a #2b2b2b transparent
        frame_contenido.place(relx=0, rely=0.08)
        frame_contenido.pack_propagate(False)

        def contenido_uno():
            limpiar_frame(frame_contenido)

            def validar_numero(valor):
                # Verifica si el valor es vacío (para permitir borrar) o si es un número entero válido
                return valor == "" or valor.isdigit()

            entry_var = ctk.StringVar()
            entry_var1 = ctk.StringVar()
            entry_var2 = ctk.StringVar()
            entry_var3 = ctk.StringVar()

            cod_bar_label = ctk.CTkLabel(frame_contenido, text="Código de barras")
            cod_bar_label.place(relx=0.05, rely=0.05)
            cod_bar_entry = ctk.CTkEntry(frame_contenido, textvariable=entry_var, width=200, height=15)
            cod_bar_entry.place(relx=0.05, rely=0.1)

            cod_interno_label = ctk.CTkLabel(frame_contenido, text="Código interno")
            cod_interno_label.place(relx=0.466, rely=0.05)
            cod_interno_entry = ctk.CTkEntry(frame_contenido, textvariable=entry_var1, width=140, height=15)
            cod_interno_entry.place(relx=0.466, rely=0.1)

            descrip_label = ctk.CTkLabel(frame_contenido, text="Descripción")
            descrip_label.place(relx=0.05, rely=0.2)
            descrip_entry = ctk.CTkEntry(frame_contenido, width=350, height=15)
            descrip_entry.place(relx=0.05, rely=0.25)

            precio_compra_label = ctk.CTkLabel(frame_contenido, text="Precio Unitario")
            precio_compra_label.place(relx=0.716, rely=0.2)
            precio_compra_entry = ctk.CTkEntry(frame_contenido, textvariable=entry_var2, width=120, height=15)
            precio_compra_entry.place(relx=0.716, rely=0.25)

            unds_label = ctk.CTkLabel(frame_contenido, text="Unidades")
            unds_label.place(relx=0.78, rely=0.05)
            unds_entry = ctk.CTkEntry(frame_contenido, textvariable=entry_var3, width=85, height=15)
            unds_entry.place(relx=0.78, rely=0.1)

            frame_tabla = ctk.CTkFrame(frame_contenido, width=600, height=266, fg_color="transparent", corner_radius=10)
            frame_tabla.place(relx=0, rely=0.5)
            frame_tabla.pack_propagate(False)

            tree = ttk.Treeview(frame_tabla, style="Treeview",
                                columns=["Columna 1", "Columna 2", "Columna 3", "Columna 4", "Columna 5"],
                                show='headings', height=10)
            scrollbar_y = ttk.Scrollbar(frame_tabla, orient=tk.VERTICAL, command=tree.yview)
            tree.configure(yscrollcommand=scrollbar_y.set)
            style = ttk.Style()
            style.configure("Treeview",
                            background="#2b2b2b",
                            foreground="white",
                            rowheight=25,
                            fieldbackground="#2b2b2b")
            style.map('Treeview',
                      background=[('selected', '#1f538d')])
            tree.grid(row=0, column=0, sticky="nswe")
            scrollbar_y.grid(row=0, column=1, sticky="ns")

            tree.heading("Columna 1", text="Código interno")
            tree.heading("Columna 2", text="Código de barras")
            tree.heading("Columna 3", text="Descripción")
            tree.heading("Columna 4", text="Precio")
            tree.heading("Columna 5", text="Unidades")

            tree.column("Columna 1", width=100)
            tree.column("Columna 2", width=140)
            tree.column("Columna 3", width=190)
            tree.column("Columna 4", width=90)
            tree.column("Columna 5", width=60)

            tabla_registro = []
            tabla = []

            validacion = ventana2.register(validar_numero)
            cod_bar_entry.configure(validate="key", validatecommand=(validacion, "%P"))
            cod_interno_entry.configure(validate="key", validatecommand=(validacion, "%P"))
            precio_compra_entry.configure(validate="key", validatecommand=(validacion, "%P"))
            unds_entry.configure(validate="key", validatecommand=(validacion, "%P"))

            def agregar_datos():
                codigo_interno = cod_interno_entry.get()
                codigo_barr = cod_bar_entry.get()
                descripcion = descrip_entry.get()
                precio = precio_compra_entry.get()
                unidades = unds_entry.get()

                if codigo_barr and codigo_interno and descripcion and precio and unidades:
                    try:
                        cursor.execute('SELECT cod_interno, cod_bar FROM productos')
                        fila = cursor.fetchall()
                        cod_bar_veri = int(codigo_barr)
                        cod_int_veri = int(codigo_interno)
                        existe = False

                        for tupla in fila:
                            if cod_int_veri == tupla[0] or cod_bar_veri == tupla[1]:
                                existe = True
                                break

                        if existe:
                            messagebox.showerror("Error", "Código interno o Código de barras ya está registrado.")
                        else:
                            tupla = (codigo_interno, codigo_barr, descripcion, precio, unidades)
                            tupla = tuple(int(elemento) if elemento.isdigit() else elemento for elemento in tupla)
                            tabla.append(tupla)
                            tabla_registro.append(tupla)
                            df = pd.DataFrame(tabla)
                            cod_interno_entry.delete(0, "end")
                            cod_bar_entry.delete(0, "end")
                            descrip_entry.delete(0, "end")
                            precio_compra_entry.delete(0, "end")
                            unds_entry.delete(0, "end")

                            for _, row in df.iterrows():
                                tree.insert("", tk.END, values=list(row))

                            tabla.clear()
                    except ValueError:
                        messagebox.showerror("Error", "Los valores numéricos no son válidos")
                else:
                    messagebox.showerror("Error", "Complete todos los campos")

            def borrar_fila_seleccionada(tree):
                # Obtener la fila seleccionada
                fila_seleccionada = tree.selection()

                if fila_seleccionada:
                    # Borrar la fila seleccionada
                    for fila in fila_seleccionada:
                        temp = tree.item(fila, "values")
                        temp = tuple(int(elemento) if elemento.isdigit() else elemento for elemento in temp)
                        if temp in tabla_registro:
                            tabla_registro.remove(temp)
                        tree.delete(fila)
                else:
                    messagebox.showinfo("Información", "Seleccione una fila para borrar")

            def insert_datos():
                if not tree.get_children():
                    messagebox.showerror("Error", "No hay datos para registrar.")
                else:
                    try:
                        cursor.executemany(
                            '''INSERT INTO productos (cod_interno, cod_bar, descripcion, precio, unidades) VALUES (?, ?, ?, ?, ?)''',
                            tabla_registro)
                        conexion.commit()
                        for item in tree.get_children():
                            tree.delete(item)
                        tabla_registro.clear()
                        messagebox.showinfo("Éxito", "Datos registrados correctamente")
                    except sqlite3.Error as e:
                        messagebox.showerror("Error", f"Error al registrar datos: {e}")

            boton_aceptar = ctk.CTkButton(frame_contenido, text="Aceptar", command=agregar_datos, text_color="black",
                                          fg_color="#00DB9A", width=100, height=25)
            boton_aceptar.place(relx=0.05, rely=0.4)

            boton_borrar = ctk.CTkButton(frame_contenido, text="Borrar", command=lambda: borrar_fila_seleccionada(tree),
                                         text_color="black", fg_color="#00DB9A", width=100, height=25)
            boton_borrar.place(relx=0.25, rely=0.4)

            boton_registrar = ctk.CTkButton(frame_contenido, text="Registrar", command=insert_datos, text_color="black",
                                            fg_color="#00DB9A", width=100, height=25)
            boton_registrar.place(relx=0.7, rely=0.4)

            destacar_btn(btn1)

        # //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        def contenido_dos():
            limpiar_frame(frame_contenido)
            global fila_seleccionada
            fila_seleccionada = None

            def validar_numero(valor):
                # Verifica si el valor es vacío (para permitir borrar) o si es un número entero válido
                return valor == "" or valor.isdigit()

            entry_var = ctk.StringVar()
            entry_var1 = ctk.StringVar()
            entry_var2 = ctk.StringVar()
            entry_var3 = ctk.StringVar()

            cod_bar_label = ctk.CTkLabel(frame_contenido, text="Código de barras")
            cod_bar_label.place(relx=0.05, rely=0.55)
            cod_bar_entry = ctk.CTkEntry(frame_contenido, textvariable=entry_var, width=200, height=15)
            cod_bar_entry.place(relx=0.05, rely=0.6)

            cod_interno_label = ctk.CTkLabel(frame_contenido, text="Código interno")
            cod_interno_label.place(relx=0.466, rely=0.55)
            cod_interno_entry = ctk.CTkEntry(frame_contenido, textvariable=entry_var1, width=140, height=15)
            cod_interno_entry.place(relx=0.466, rely=0.6)

            descrip_label = ctk.CTkLabel(frame_contenido, text="Descripción")
            descrip_label.place(relx=0.05, rely=0.7)
            descrip_entry = ctk.CTkEntry(frame_contenido, width=350, height=15)
            descrip_entry.place(relx=0.05, rely=0.75)

            precio_compra_label = ctk.CTkLabel(frame_contenido, text="Precio Unitario")
            precio_compra_label.place(relx=0.716, rely=0.7)
            precio_compra_entry = ctk.CTkEntry(frame_contenido, textvariable=entry_var2, width=120, height=15)
            precio_compra_entry.place(relx=0.716, rely=0.75)

            unds_label = ctk.CTkLabel(frame_contenido, text="Unidades")
            unds_label.place(relx=0.78, rely=0.55)
            unds_entry = ctk.CTkEntry(frame_contenido, textvariable=entry_var3, width=85, height=15)
            unds_entry.place(relx=0.78, rely=0.6)

            validacion = ventana2.register(validar_numero)
            cod_bar_entry.configure(validate="key", validatecommand=(validacion, "%P"))
            cod_interno_entry.configure(validate="key", validatecommand=(validacion, "%P"))
            precio_compra_entry.configure(validate="key", validatecommand=(validacion, "%P"))
            unds_entry.configure(validate="key", validatecommand=(validacion, "%P"))

            def realizar_busqueda():
                opcion = selector.get()
                dato = busqueda_entry.get()

                # Limpiar el TreeView antes de mostrar nuevos resultados
                for item in tree.get_children():
                    tree.delete(item)

                if opcion == "Código Interno":
                    if dato:
                        try:
                            dato = int(dato)
                            cursor.execute('SELECT cod_interno FROM productos')
                            codigos = [cod[0] for cod in cursor.fetchall()]

                            if dato in codigos:
                                query = "SELECT * FROM productos WHERE cod_interno = ?"
                                cursor.execute(query, (dato,))
                                fila_datos = cursor.fetchone()
                                busqueda_entry.delete(0, "end")
                                tree.insert("", tk.END, values=list(fila_datos))
                            else:
                                messagebox.showerror("Error", "Código interno no existe")
                        except ValueError:
                            messagebox.showerror("Error", "El código debe ser un número entero")
                    else:
                        messagebox.showerror("Error", "Ingrese un código")

                elif opcion == "Código de Barras":
                    if dato:
                        try:
                            dato = int(dato)
                            cursor.execute('SELECT cod_bar FROM productos')
                            codigos = [cod[0] for cod in cursor.fetchall()]

                            if dato in codigos:
                                query = "SELECT * FROM productos WHERE cod_bar = ?"
                                cursor.execute(query, (dato,))
                                fila_datos = cursor.fetchone()
                                busqueda_entry.delete(0, "end")
                                tree.insert("", tk.END, values=list(fila_datos))
                            else:
                                messagebox.showerror("Error", "Código de barras no existe")
                        except ValueError:
                            messagebox.showerror("Error", "El código debe ser un número entero")
                    else:
                        messagebox.showerror("Error", "Ingrese un código")
                else:
                    messagebox.showerror("Error", "Seleccione un tipo de búsqueda")

            def seleccion(opcion):
                if opcion == "Código Interno" or opcion == "Código de Barras":
                    validacion = ventana2.register(validar_numero)
                    busqueda_entry.configure(validate="key", validatecommand=(validacion, "%P"))
                else:
                    busqueda_entry.configure(validate="none")

            def borrar_fila(tree):
                fila_select = tree.selection()
                if fila_select:
                    tree.delete(fila_select)
                    limpiar_campos()
                else:
                    messagebox.showinfo("Información", "Seleccione una fila para borrar")

            def pasar_datos(evento):
                global fila_seleccionada
                fila = tree.identify_row(evento.y)
                if not fila:
                    return  # No se seleccionó ninguna fila

                # Obtener todos los valores de la fila seleccionada
                valores = tree.item(fila, "values")

                # Limpiar y llenar todos los campos
                cod_interno_entry.delete(0, "end")
                cod_interno_entry.insert(0, valores[0])

                cod_bar_entry.delete(0, "end")
                cod_bar_entry.insert(0, valores[1])

                descrip_entry.delete(0, "end")
                descrip_entry.insert(0, valores[2])

                precio_compra_entry.delete(0, "end")
                precio_compra_entry.insert(0, valores[3])

                unds_entry.delete(0, "end")
                unds_entry.insert(0, valores[4])

                # Guardar el ID de la fila seleccionada para actualización
                fila_seleccionada = fila

            def actualizar_datos():
                global fila_seleccionada
                if not fila_seleccionada:
                    messagebox.showerror("Error", "No hay ningún registro seleccionado para actualizar")
                    return

                # Obtener los valores actualizados
                cod_interno = cod_interno_entry.get()
                cod_barras = cod_bar_entry.get()
                descripcion = descrip_entry.get()
                precio = precio_compra_entry.get()
                unidades = unds_entry.get()

                # Validar que todos los campos estén completos
                if not (cod_interno and cod_barras and descripcion and precio and unidades):
                    messagebox.showerror("Error", "Todos los campos son obligatorios")
                    return

                # Actualizar en la base de datos
                try:
                    cursor.execute('''
                        UPDATE productos 
                        SET cod_bar = ?, descripcion = ?, precio = ?, unidades = ? 
                        WHERE cod_interno = ?
                    ''', (cod_barras, descripcion, precio, unidades, cod_interno))
                    conexion.commit()

                    # Actualizar en el TreeView
                    tree.item(fila_seleccionada, values=(cod_interno, cod_barras, descripcion, precio, unidades))

                    messagebox.showinfo("Éxito", "Registro actualizado correctamente")

                    # Limpiar campos después de actualizar
                    limpiar_campos()
                except sqlite3.Error as e:
                    messagebox.showerror("Error", f"Error al actualizar el registro: {e}")

            def limpiar_campos():
                cod_interno_entry.delete(0, "end")
                cod_bar_entry.delete(0, "end")
                descrip_entry.delete(0, "end")
                precio_compra_entry.delete(0, "end")
                unds_entry.delete(0, "end")
                global fila_seleccionada
                fila_seleccionada = None

            selector = ctk.CTkComboBox(frame_contenido, values=["Código Interno", "Código de Barras"], height=15,
                                       command=seleccion)
            selector.set("Seleccione")
            selector.place(relx=0.05, rely=0.1)

            busqueda_entry = ctk.CTkEntry(frame_contenido, width=220, height=15)
            busqueda_entry.place(relx=0.37, rely=0.1)

            btn_busqueda = ctk.CTkButton(frame_contenido, text="Buscar", width=50, height=15, command=realizar_busqueda)
            btn_busqueda.place(relx=0.825, rely=0.1)

            btn_aceptar = ctk.CTkButton(frame_contenido, text="Aceptar", width=50, height=15, command=actualizar_datos)
            btn_aceptar.place(relx=0.825, rely=0.45)

            btn_borrar = ctk.CTkButton(frame_contenido, text="Borrar", width=60, height=15,
                                       command=lambda: borrar_fila(tree))
            btn_borrar.place(relx=0.7, rely=0.45)

            btn_limpiar = ctk.CTkButton(frame_contenido, text="Limpiar", width=60, height=15, command=limpiar_campos)
            btn_limpiar.place(relx=0.575, rely=0.45)

            tree = ttk.Treeview(frame_contenido, style="Treeview",
                                columns=["Columna 1", "Columna 2", "Columna 3", "Columna 4", "Columna 5"],
                                show='headings', height=5)
            tree.place(relx=0, rely=0.2)

            tree.heading("Columna 1", text="Código interno")
            tree.heading("Columna 2", text="Código de barras")
            tree.heading("Columna 3", text="Descripción")
            tree.heading("Columna 4", text="Precio")
            tree.heading("Columna 5", text="Unidades")

            tree.column("Columna 1", width=100)
            tree.column("Columna 2", width=150)
            tree.column("Columna 3", width=200)
            tree.column("Columna 4", width=90)
            tree.column("Columna 5", width=60)
            tree.bind("<Double-1>", pasar_datos)

            destacar_btn(btn2)
        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////
        def contenido_tres():
            limpiar_frame(frame_contenido)
            global fila_seleccionada
            fila_seleccionada = None
            #frame_contenido.configure(bg_color="gray")

            def validar_numero(valor):
                # Verifica si el valor es vacío (para permitir borrar) o si es un número entero válido
                return valor == "" or valor.isdigit()

            def seleccion(opcion):
                if opcion == "Código Interno" or opcion == "Código de Barras":
                    validacion = ventana2.register(validar_numero)
                    busqueda_entry.configure(validate="key", validatecommand=(validacion, "%P"))
                else:
                    busqueda_entry.configure(validate="none")

            def borrar_fila(tree):
                fila_select = tree.selection()
                if fila_select:
                    tree.delete(fila_select)
                else:
                    messagebox.showinfo("Información", "Seleccione una fila para borrar")


            def realizar_busqueda():
                opcion = selector.get()
                dato = busqueda_entry.get()

                # Limpiar el TreeView antes de mostrar nuevos resultados
                for item in tree.get_children():
                    tree.delete(item)

                if opcion == "Código Interno":
                    if dato:
                        try:
                            dato = int(dato)
                            cursor.execute('SELECT cod_interno FROM productos')
                            codigos = [cod[0] for cod in cursor.fetchall()]

                            if dato in codigos:
                                query = "SELECT * FROM productos WHERE cod_interno = ?"
                                cursor.execute(query, (dato,))
                                fila_datos = cursor.fetchone()
                                busqueda_entry.delete(0, "end")
                                tree.insert("", tk.END, values=list(fila_datos))
                            else:
                                messagebox.showerror("Error", "Código interno no existe")
                        except ValueError:
                            messagebox.showerror("Error", "El código debe ser un número entero")
                    else:
                        messagebox.showerror("Error", "Ingrese un código")

                elif opcion == "Código de Barras":
                    if dato:
                        try:
                            dato = int(dato)
                            cursor.execute('SELECT cod_bar FROM productos')
                            codigos = [cod[0] for cod in cursor.fetchall()]

                            if dato in codigos:
                                query = "SELECT * FROM productos WHERE cod_bar = ?"
                                cursor.execute(query, (dato,))
                                fila_datos = cursor.fetchone()
                                busqueda_entry.delete(0, "end")
                                tree.insert("", tk.END, values=list(fila_datos))
                            else:
                                messagebox.showerror("Error", "Código de barras no existe")
                        except ValueError:
                            messagebox.showerror("Error", "El código debe ser un número entero")
                    else:
                        messagebox.showerror("Error", "Ingrese un código")
                else:
                    messagebox.showerror("Error", "Seleccione un tipo de búsqueda")

            def seleccion(opcion):
                if opcion == "Código Interno" or opcion == "Código de Barras":
                    validacion = ventana2.register(validar_numero)
                    busqueda_entry.configure(validate="key", validatecommand=(validacion, "%P"))
                else:
                    busqueda_entry.configure(validate="none")

            def confirmar_y_borrar(tree):
                try:
                    fila_select = tree.selection()
                    valores = tree.item(fila_select, "values")
                    valor = valores[0]
                    respuesta = messagebox.askyesno("Confirmación", "¿Está seguro de borrar producto?")

                    if respuesta and valor:
                        cursor.execute('''DELETE FROM productos WHERE cod_interno = ?''', (valor,))
                        conexion.commit()
                        tree.delete(fila_select)

                except IndexError:
                    messagebox.showerror("Error", "No hay datos para borrar")

            tree = ttk.Treeview(frame_contenido, style="Treeview",
                                columns=["Columna 1", "Columna 2", "Columna 3", "Columna 4", "Columna 5"],
                                show='headings', height=5)
            tree.place(relx=0, rely=0.2)

            tree.heading("Columna 1", text="Código interno")
            tree.heading("Columna 2", text="Código de barras")
            tree.heading("Columna 3", text="Descripción")
            tree.heading("Columna 4", text="Precio")
            tree.heading("Columna 5", text="Unidades")

            tree.column("Columna 1", width=100)
            tree.column("Columna 2", width=150)
            tree.column("Columna 3", width=200)
            tree.column("Columna 4", width=90)
            tree.column("Columna 5", width=60)

            selector = ctk.CTkComboBox(frame_contenido, values=["Código Interno", "Código de Barras"], height=15, command=seleccion)
            selector.set("Seleccione")


            selector.place(relx=0.05, rely=0.1)

            busqueda_entry = ctk.CTkEntry(frame_contenido, width=220, height=15)
            busqueda_entry.place(relx=0.37, rely=0.1)

            btn_busqueda = ctk.CTkButton(frame_contenido, text="Buscar", width=50, height=15, command=realizar_busqueda)
            btn_busqueda.place(relx=0.825, rely=0.1)

            btn_borrar = ctk.CTkButton(frame_contenido, text="Borrar", width=50, height=15, command= lambda :confirmar_y_borrar(tree))
            btn_borrar.place(relx=0.825, rely=0.45)




            destacar_btn(btn3)
        #///////////////////////////////////////////////////////////////////////////////////////////////////////////////
        def destacar_btn(boton1):
            if boton_seleccionado2[0]:
                boton_seleccionado2[0].configure(fg_color='#006B4D', text_color='white')
            boton_seleccionado2[0] = boton1
            boton1.configure(fg_color='#00DB9A', text_color='black')
            frame_contenido.configure(fg_color="transparent")

        def limpiar_frame(frame):
            for widget in frame.winfo_children():
                widget.destroy()

        boton_seleccionado2 = [None]

        btn1 = ctk.CTkButton(frame_botones, text="Registro Nuevo", command=contenido_uno, text_color="white",
                             fg_color="#006B4D")
        btn1.pack(side="left", padx=15)
        btn2 = ctk.CTkButton(frame_botones, text="Editar Registro", command=contenido_dos, text_color="white",
                             fg_color="#006B4D")
        btn2.pack(side="left", padx=5)

        btn3 = ctk.CTkButton(frame_botones, text="Borrar Registro", command=contenido_tres, text_color="white",
                             fg_color="#006B4D")
        btn3.pack(side="left", padx=15)
        destacar_boton(boton1)

    # /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def mostrar_contenido2():
        limpiar_frame(frame_principal)
        label = ctk.CTkLabel(frame_principal, text="¡Este es el contenido del Menú 2!", font=("Arial", 16))
        label.pack(pady=20)
        destacar_boton(boton2)

    def mostrar_contenido3():
        limpiar_frame(frame_principal)
        label = ctk.CTkLabel(frame_principal, text="¡Este es el contenido del Menú 3!", font=("Arial", 16))
        label.pack(pady=20)
        destacar_boton(boton3)

    def destacar_boton(boton):
        # Restablece el color del botón previamente seleccionado
        if boton_seleccionado[0]:
            boton_seleccionado[0].configure(fg_color="#006B4D", text_color="white")
        # Configura el botón actual como seleccionado
        boton_seleccionado[0] = boton
        boton.configure(fg_color='#00DB9A', text_color='black')  # Cambia el color del botón activo

    def limpiar_frame(frame):
        for widget in frame.winfo_children():
            widget.destroy()

    boton_seleccionado = [None]

    def salir():
        usuario.delete(0, "end")
        passw.delete(0, "end")
        ventana.deiconify()
        ventana2.quit()  # Detén el bucle principal
        ventana2.destroy()


    # Configuración inicial
    ctk.set_appearance_mode("dark")

    # Ventana principal
    ventana2 = ctk.CTk()
    ventana2.title("Ventana Principal Del Programa")
    h_v, w_v = (600, 800)
    w_p, h_p = (ventana2.winfo_screenwidth(), ventana2.winfo_screenheight())
    pos_x = (w_p // 2) - (w_v // 2)
    pos_y = (h_p // 2) - (h_v // 2)
    ventana2.geometry(f"{w_v}x{h_v}+{pos_x}+{pos_y}")
    ventana2.resizable(width=False, height=False)
    ventana2.protocol("WM_DELETE_WINDOW", on_closing_secondary)

    # Frame lateral
    frame_lateral = ctk.CTkFrame(ventana2, width=200, corner_radius=10)
    frame_lateral.pack(side="left", fill="y", padx=10, pady=10)

    # Botones del menú
    # Variable para rastrear el botón activo
    boton1 = ctk.CTkButton(frame_lateral, text="Registro", command=mostrar_contenido1, text_color="white",
                           fg_color="#006B4D")
    boton1.pack(pady=10, padx=10, fill="x")

    boton2 = ctk.CTkButton(frame_lateral, text="Menú 2", command=mostrar_contenido2, text_color="white",
                           fg_color="#006B4D")
    boton2.pack(pady=10, padx=10, fill="x")

    boton3 = ctk.CTkButton(frame_lateral, text="Menú 3", command=mostrar_contenido3, text_color="white",
                           fg_color="#006B4D")
    boton3.pack(pady=10, padx=10, fill="x")

    btn_salir = ctk.CTkButton(frame_lateral, text="Cerrar Sesión", command=salir, text_color="white", fg_color="#006B4D")
    btn_salir.pack(pady=10, padx=10, fill="x", side="bottom")

    label = ctk.CTkLabel(frame_lateral, text = f"Usuario: {usuario.get()}" , text_color="gray")
    label.pack(pady=10, padx=10, fill="x", side="bottom")
    # Frame principal
    frame_principal = ctk.CTkFrame(ventana2, corner_radius=10, bg_color="transparent")
    frame_principal.pack(side="right", expand=True, fill="both", padx=10, pady=10)
    frame_principal.pack_propagate(False)

    # Mostrar el contenido inicial (Registro)
    mostrar_contenido1()

    ventana2.mainloop()


# Iniciar la aplicación
ventana.mainloop()

# Cerrar la conexión a la base de datos al finalizar
if conexion:
    conexion.close()