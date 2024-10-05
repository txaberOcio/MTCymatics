import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def cambiar_color(boton):
    if boton.cget('bg') == 'gray':
        boton.config(bg='green')
    else:
        boton.config(bg='gray')

def crear_boton_cuadrado(canal_frame, texto):
    boton = tk.Button(canal_frame, text=texto, bg='gray', fg='white', font=('Arial', 10), width=8, height=4)
    boton.config(command=lambda b=boton: cambiar_color(b))
    return boton

def crear_ventana_pantalla_completa():
    print('Creando ventana...')  # Verificación
    ventana = tk.Tk()
    ventana.attributes('-fullscreen', True)
    ventana.title('Mesa de Sonido')

    # Cargar la imagen
    imagen = Image.open("/ProyectosVisual/MTCymatics/Assets/3.png")
    
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Crear marco principal
    marco_principal = tk.Frame(ventana, bg='light gray')
    marco_principal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Añadir el botón azul con imagen de fondo
    boton_azul = tk.Button(marco_principal, image=imagen_tk, bg='blue', fg='white', font=('Arial', 10), width=217, height=213)
    boton_azul.image = imagen_tk  # Guardar una referencia de la imagen
    boton_azul.pack(anchor='nw')

    # Añadir deslizadores de volumen y botones
    for i in range(8):  # Simulando 8 canales
        canal_frame = tk.Frame(marco_principal, bg='lightgray', bd=2, relief=tk.RAISED)
        canal_frame.pack(side=tk.LEFT, padx=10, pady=10)

        label = tk.Label(canal_frame, text=f'Canal {i+1}', bg='lightgray', fg='black', font=('Arial', 12))
        label.pack(pady=5)

        slider = ttk.Scale(canal_frame, from_=0, to=100, orient=tk.VERTICAL)
        slider.set(50)  # Valor inicial
        slider.pack(pady=5)

        boton_mute = tk.Button(canal_frame, text='Mute', bg='gray', fg='white', font=('Arial', 10))
        boton_mute.pack(pady=5)

        boton_solo = tk.Button(canal_frame, text='Solo', bg='darkgray', fg='white', font=('Arial', 10))
        boton_solo.pack(pady=5)

        boton_rec = tk.Button(canal_frame, text='Rec', bg='dimgray', fg='white', font=('Arial', 10))
        boton_rec.pack(pady=5)

        # Añadir botones cuadrados
        for j in range(2):  # Añadiendo 3 botones cuadrados por canal
            boton_cuadrado = crear_boton_cuadrado(canal_frame, f'Btn {j+1}')
            boton_cuadrado.pack(pady=5)

    # Botón para salir
    boton_salir = tk.Button(ventana, text='Salir', command=ventana.destroy, bg='gray', fg='white', font=('Arial', 12))
    boton_salir.pack(pady=20)

    print('Iniciando bucle principal...')  # Verificación
    ventana.mainloop()

crear_ventana_pantalla_completa()
