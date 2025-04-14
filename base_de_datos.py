import customtkinter

# Configuración inicial
customtkinter.set_appearance_mode("System")  # Modo de apariencia
customtkinter.set_default_color_theme("blue")  # Tema de color

# Crear ventana principal
root = customtkinter.CTk()
root.geometry("400x300")
root.title("Búsqueda con ComboBox")


# Función para realizar la búsqueda
def realizar_busqueda():
    criterio = selector.get()
    dato = entrada_dato.get()

    if criterio == "Nombre":
        print(f"Buscando por Nombre: {dato}")
    elif criterio == "Código de Barras":
        print(f"Buscando por Código de Barras: {dato}")
    elif criterio == "Código Interno":
        print(f"Buscando por Código Interno: {dato}")
    else:
        print("Por favor, selecciona un criterio válido.")


# Crear ComboBox para seleccionar el criterio de búsqueda
selector = customtkinter.CTkComboBox(root,
                                     values=["Nombre",
                                             "Código de Barras",
                                             "Código Interno"])
selector.set("Seleccione un criterio")
selector.pack(pady=20)

# Crear entrada para llenar el dato de búsqueda
entrada_dato = customtkinter.CTkEntry(root, placeholder_text="Ingrese el dato de búsqueda aquí")
entrada_dato.pack(pady=20)

# Crear botón para realizar la búsqueda
boton_buscar = customtkinter.CTkButton(root, text="Buscar", command=realizar_busqueda)
boton_buscar.pack(pady=20)

# Ejecutar la app
root.mainloop()