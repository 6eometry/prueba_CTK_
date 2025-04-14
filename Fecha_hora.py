import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# Configurar apariencia de CustomTkinter
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Variables globales para mantener el estado
selected_item_id = None


def on_tree_select(event):
    global selected_item_id
    selected_items = tree.selection()

    if not selected_items:
        return

    # Obtener el primer elemento seleccionado
    selected_item_id = selected_items[0]
    item_values = tree.item(selected_item_id, "values")

    # Actualizar los campos del formulario
    var_id.set(item_values[0])
    var_nombre.set(item_values[1])
    var_edad.set(item_values[2])
    var_email.set(item_values[3])
    var_telefono.set(item_values[4])

    # Habilitar formulario
    toggle_form_state("normal")

    # Actualizar mensaje de estado
    status_label.configure(text=f"Editando registro ID: {item_values[0]}")


def save_changes():
    global selected_item_id
    if not selected_item_id:
        return

    # Obtener valores actualizados
    updated_values = (
        var_id.get(),
        var_nombre.get(),
        var_edad.get(),
        var_email.get(),
        var_telefono.get()
    )

    # Actualizar el elemento en el TreeView
    tree.item(selected_item_id, values=updated_values)

    # Actualizar mensaje de estado
    status_label.configure(text=f"Cambios guardados para ID: {var_id.get()}")


def clear_form():
    global selected_item_id
    # Limpiar campos
    var_id.set("")
    var_nombre.set("")
    var_edad.set("")
    var_email.set("")
    var_telefono.set("")

    # Deshabilitar formulario
    toggle_form_state("disabled")

    # Deseleccionar elemento del TreeView
    if selected_item_id:
        tree.selection_remove(tree.selection())
        selected_item_id = None

    # Actualizar mensaje de estado
    status_label.configure(text="Seleccione un elemento para editar")


def toggle_form_state(state):
    # Configurar estado de los campos
    nombre_entry.configure(state=state)
    edad_entry.configure(state=state)
    email_entry.configure(state=state)
    telefono_entry.configure(state=state)
    save_button.configure(state=state)


def load_sample_data():
    # Insertar 5 registros de ejemplo
    data = [
        ("1", "Juan Pérez", "28", "juan@ejemplo.com", "555-123-4567"),
        ("2", "María García", "34", "maria@ejemplo.com", "555-234-5678"),
        ("3", "Carlos López", "45", "carlos@ejemplo.com", "555-345-6789"),
        ("4", "Ana Martínez", "22", "ana@ejemplo.com", "555-456-7890"),
        ("5", "Roberto Sánchez", "39", "roberto@ejemplo.com", "555-567-8901")
    ]

    for item in data:
        tree.insert("", tk.END, values=item)


# Crear ventana principal
root = ctk.CTk()
root.title("Editor de Datos - CustomTkinter")
root.geometry("900x600")

# Configurar grid de la ventana principal
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

# Crear frame izquierdo para el TreeView
tree_frame = ctk.CTkFrame(root)
tree_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
tree_frame.grid_rowconfigure(0, weight=0)  # Para el título
tree_frame.grid_rowconfigure(1, weight=1)  # Para el TreeView

# Título del TreeView
tree_label = ctk.CTkLabel(tree_frame, text="Datos", font=ctk.CTkFont(size=16, weight="bold"))
tree_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Crear TreeView con estilo personalizado
style = ttk.Style()
style.configure("Treeview",
                background="#2b2b2b",
                foreground="white",
                rowheight=25,
                fieldbackground="#2b2b2b")
style.map('Treeview',
          background=[('selected', '#1f538d')])

# Frame para contener el TreeView y scrollbar
tree_container = ctk.CTkFrame(tree_frame)
tree_container.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")
tree_container.grid_rowconfigure(0, weight=1)
tree_container.grid_columnconfigure(0, weight=1)

# Crear TreeView
tree = ttk.Treeview(tree_container, style="Treeview")
tree.grid(row=0, column=0, sticky="nsew")

# Agregar scrollbar
scrollbar = ctk.CTkScrollbar(tree_container, command=tree.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
tree.configure(yscrollcommand=scrollbar.set)

# Configurar columnas del TreeView
tree["columns"] = ("ID", "Nombre", "Edad", "Email", "Teléfono")
tree.column("#0", width=0, stretch=tk.NO)  # Ocultar primera columna
tree.column("ID", anchor=tk.CENTER, width=50)
tree.column("Nombre", anchor=tk.W, width=150)
tree.column("Edad", anchor=tk.CENTER, width=50)
tree.column("Email", anchor=tk.W, width=200)
tree.column("Teléfono", anchor=tk.W, width=120)

# Configurar encabezados
tree.heading("#0", text="", anchor=tk.W)
tree.heading("ID", text="ID", anchor=tk.CENTER)
tree.heading("Nombre", text="Nombre", anchor=tk.W)
tree.heading("Edad", text="Edad", anchor=tk.CENTER)
tree.heading("Email", text="Email", anchor=tk.W)
tree.heading("Teléfono", text="Teléfono", anchor=tk.W)

# Vincular evento de selección
tree.bind("<<TreeviewSelect>>", on_tree_select)

# Crear frame derecho para el formulario de edición
edit_frame = ctk.CTkFrame(root)
edit_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

# Título del formulario
edit_label = ctk.CTkLabel(edit_frame, text="Editar Datos", font=ctk.CTkFont(size=16, weight="bold"))
edit_label.pack(anchor="w", padx=20, pady=20)

# Crear variables para los campos
var_id = tk.StringVar()
var_nombre = tk.StringVar()
var_edad = tk.StringVar()
var_email = tk.StringVar()
var_telefono = tk.StringVar()

# Crear formulario
form_frame = ctk.CTkFrame(edit_frame, fg_color="transparent")
form_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Campo ID (deshabilitado para edición)
id_label = ctk.CTkLabel(form_frame, text="ID:")
id_label.pack(anchor="w", padx=5, pady=(10, 0))
id_entry = ctk.CTkEntry(form_frame, textvariable=var_id, state="disabled", width=300)
id_entry.pack(anchor="w", padx=5, pady=(0, 10))

# Campo Nombre
nombre_label = ctk.CTkLabel(form_frame, text="Nombre:")
nombre_label.pack(anchor="w", padx=5, pady=(10, 0))
nombre_entry = ctk.CTkEntry(form_frame, textvariable=var_nombre, width=300)
nombre_entry.pack(anchor="w", padx=5, pady=(0, 10))

# Campo Edad
edad_label = ctk.CTkLabel(form_frame, text="Edad:")
edad_label.pack(anchor="w", padx=5, pady=(10, 0))
edad_entry = ctk.CTkEntry(form_frame, textvariable=var_edad, width=300)
edad_entry.pack(anchor="w", padx=5, pady=(0, 10))

# Campo Email
email_label = ctk.CTkLabel(form_frame, text="Email:")
email_label.pack(anchor="w", padx=5, pady=(10, 0))
email_entry = ctk.CTkEntry(form_frame, textvariable=var_email, width=300)
email_entry.pack(anchor="w", padx=5, pady=(0, 10))

# Campo Teléfono
telefono_label = ctk.CTkLabel(form_frame, text="Teléfono:")
telefono_label.pack(anchor="w", padx=5, pady=(10, 0))
telefono_entry = ctk.CTkEntry(form_frame, textvariable=var_telefono, width=300)
telefono_entry.pack(anchor="w", padx=5, pady=(0, 10))

# Botones
button_frame = ctk.CTkFrame(edit_frame, fg_color="transparent")
button_frame.pack(fill="x", padx=20, pady=20)

save_button = ctk.CTkButton(button_frame, text="Guardar Cambios", command=save_changes)
save_button.pack(side="left", padx=5)

clear_button = ctk.CTkButton(button_frame, text="Limpiar", command=clear_form, fg_color="#555555",
                             hover_color="#333333")
clear_button.pack(side="left", padx=5)

# Mensaje de estado
status_label = ctk.CTkLabel(edit_frame, text="Seleccione un elemento para editar", text_color="#888888")
status_label.pack(pady=10)

# Cargar datos de ejemplo
load_sample_data()

# Deshabilitar formulario inicialmente
toggle_form_state("disabled")

# Iniciar el bucle principal
root.mainloop()