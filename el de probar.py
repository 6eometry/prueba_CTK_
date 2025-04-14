import customtkinter as ctk

def iniciar_sesion():
    # Cambiar a la ventana principal
    ventana_inicio.pack_forget()
    ventana_principal.pack()

def cerrar_sesion():
    # Cambiar de vuelta a la ventana de inicio de sesión
    ventana_principal.pack_forget()
    ventana_inicio.pack()

# Configuración de la ventana principal
ventana = ctk.CTk()
ventana.geometry("400x300")
ventana.title("Ejemplo sin clases")

# Ventana de inicio de sesión
ventana_inicio = ctk.CTkFrame(ventana)
ventana_inicio.pack(fill="both", expand=True)

label_inicio = ctk.CTkLabel(ventana_inicio, text="Inicio de Sesión")
label_inicio.pack(pady=10)

boton_inicio = ctk.CTkButton(ventana_inicio, text="Iniciar Sesión", command=iniciar_sesion)
boton_inicio.pack(pady=10)

# Ventana principal
ventana_principal = ctk.CTkFrame(ventana)
label_principal = ctk.CTkLabel(ventana_principal, text="Ventana Principal")
label_principal.pack(pady=10)

boton_cerrar = ctk.CTkButton(ventana_principal, text="Cerrar Sesión", command=cerrar_sesion)
boton_cerrar.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()