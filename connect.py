import paramiko
import tkinter as tk
from tkinter import PhotoImage


def conectar():
    # Configuración SSH
    host = "ec2-44-202-119-179.compute-1.amazonaws.com"
    username = "hadoop"
    key_path = "C:/Users/ROG/Downloads/llave-cluster.pem"


    word = entrada_consulta.get()

    if word == "redshirts":
        consulta = "SELECT * FROM redshirts_per_camera;"
    elif word == "persons":
        consulta = "SELECT * FROM persons_per_camera;"
    elif word == "backpacks":
        consulta = "SELECT * FROM backpacks_per_camera;"
    elif word == "cars":
        consulta = "SELECT * FROM cars_per_camera;"
    elif word == "bicycles":
        consulta = "SELECT * FROM bicycles_per_camera;"
    elif word == "dogs":
        consulta = "SELECT * FROM dogs_per_camera;"
    elif word == "cats":
        consulta = "SELECT * FROM cats_per_camera;"
    elif word == "blueshirts":
        consulta = "SELECT * FROM blueshirts_per_camera;"
    elif word == "blackshirts":
        consulta = "SELECT * FROM blackshirts_per_camera;"
    elif word == "redcars":
        consulta = "SELECT * FROM redcars_per_camera;"
    elif word == "bluecars":
        consulta = "SELECT * FROM bluecars_per_camera;"
    elif word == "altos":
        consulta = "SELECT * FROM altos_per_camera;"
    elif word == "pequenos":
        consulta = "SELECT * FROM pequenos_per_camera;"
    elif word == "blueshoes":
        consulta = "SELECT * FROM blueshoes_per_camera;"
    elif word == "redshoes":
        consulta = "SELECT * FROM redshoes_per_camera;"
    elif word == "blackshoes":
        consulta = "SELECT * FROM blackshoes_per_camera;"
    elif word == "bluepants":
        consulta = "SELECT * FROM bluepants_per_camera;"
    elif word == "redpants":
        consulta = "SELECT * FROM redpants_per_camera;"
    elif word == "blackpants":
        consulta = "SELECT * FROM blackpants_per_camera;"
    else:
        consulta = "SELECT 'Atributo no encontrado';"



    commands = f"""
    hive -e "{consulta}"
    """


    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=host, username=username, key_filename=key_path)
        print("¡Conexión exitosa!")

        # Ejecutar los comandos
        stdin, stdout, stderr = ssh.exec_command(commands)
        output = stdout.read().decode()
        errors = stderr.read().decode()

        if output:
            filas = output.strip().split('\n')
            datos = [fila.split('\t') for fila in filas]

            salida_formateada = ""
            for fila in datos:
                
                salida_formateada += "●\t"  
                salida_formateada += "\t".join(fila[:-1]) 
                salida_formateada += "\t➔ [ " + (fila[-1] if fila[-1] else "NULL") + " ]\n\n"  
            resultado_text.delete(1.0, tk.END)
            resultado_text.insert(tk.END, salida_formateada)
        else:
            resultado_text.insert(tk.END, "No se obtuvieron resultados.")
        
        if errors:
            print("Errores:\n", errors)

    except Exception as e:
        print(f"Error: {e}")
        resultado_text.insert(tk.END, f"Error al conectar: {e}")

    finally:
        ssh.close()


ventana = tk.Tk()
ventana.title("Conector a Hive")



frame_busqueda = tk.Frame(ventana)
frame_busqueda.pack(padx=10, pady=10)


logo_image = PhotoImage(file="hive_logo.png")


logo_image = logo_image.subsample(10, 10)  


logo_label = tk.Label(frame_busqueda, image=logo_image)
logo_label.pack(side="left")


entrada_consulta = tk.Entry(frame_busqueda, width=50)
entrada_consulta.pack(side="left", padx=10)


boton_buscar = tk.Button(ventana, text="Buscar", command=conectar)
boton_buscar.pack(padx=10, pady=10)


resultado_text = tk.Text(ventana, width=100, height=20)
resultado_text.pack(padx=10, pady=10)


ventana.mainloop()
