import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Franco
apellido: Puricelli
---
Ejercicio: Parcial
---
Enunciado:

De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.
Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo mas ingresado (F o M)
Informe B- El porcentaje de mascotas hay por tipo (gato ,perro o exotico)
Informe C- El nombre de la mascota más pesada
Informe D- El sexo y nombre del gato más viejo
Informe E- El promedio de edad de todas las mascotas
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Repetir")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_repetir = customtkinter.CTkEntry(master=self)
        self.txt_repetir.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador = 0
        
        flag_peso = True
        flag_edad = True
        contador_fem = 0
        contador_masc = 0     
        contador_perros = 0
        contador_gatos = 0
        contador_exoticos = 0
        maximo_peso = 0
        sexo_mas_ingresado = ""
        nombre_max = ""
        edad_max = 0
        sexo_max = ""
        nombre__mas_viejo = ""
        acumulador_edad_perros = 0
        acumulador_edad_gatos = 0
        acumulador_edad_exoticos = 0

        while contador < 5 :
            nombre = prompt("mensaje","Ingrese nombre")

            tipo = prompt("mensaje","Ingrese tipo")
            while tipo != "gato" and tipo != "perro" and tipo != "exotico":
                tipo = prompt("mensaje","Reingrese tipo")
            
            peso = prompt("mensaje", "ingrese peso")
            peso = int(peso)
            while peso < 10 or peso > 80:
                peso = prompt("mensaje", "Reingrese peso")
                peso = int(peso)

            sexo = prompt("mensaje","Ingrese su sexo")
            while sexo != "masculino" and sexo != "femenino":
                sexo = prompt("mensaje","Reingrese su sexo")

            edad = prompt("mensaje","ingrese edad")
            edad = int(edad)
            while edad < 0:
                edad = prompt("mensaje","reingrese edad")
                edad = int(edad)


            if sexo == "masculino":
                contador_masc += 1
            else:
                contador_fem += 1


            if tipo == "perro":
                contador_perros += 1
                acumulador_edad_perros += edad
            elif tipo == "gato":
                contador_gatos += 1
                acumulador_edad_gatos += edad
                if edad > edad_max or flag_edad == True:
                    edad_max = edad
                    sexo_max = sexo
                    nombre__mas_viejo = nombre
                    flag_edad = False
            else:
                contador_exoticos += 1
                acumulador_edad_exoticos += edad

            if peso > maximo_peso or flag_peso == True:
                maximo_peso = peso
                nombre_max = nombre
                flag_peso = False

            contador += 1





        if contador_fem > contador_masc:
            sexo_mas_ingresado = "femenino"
        else:
            sexo_mas_ingresado = "masculino"

        total_mascotas = contador_perros + contador_gatos + contador_exoticos
        total_edad = acumulador_edad_exoticos + acumulador_edad_gatos + acumulador_edad_perros

        porcentaje_perros = (contador_perros *  100) / total_mascotas
        porcentaje_gatos = (contador_gatos * 100) / total_mascotas
        porcentaje_exoticos = (contador_exoticos * 100) / total_mascotas

        promedio_edad = total_edad / total_mascotas







        print(f"El sexo mas ingresado es: {sexo_mas_ingresado} \n Porcentajes: \n\t Perros: {porcentaje_perros} \t Gatos: {porcentaje_gatos} \t Exoticos: {porcentaje_exoticos} \n {nombre_max} es la mascota mas pesada ({maximo_peso} kilos) \n {nombre__mas_viejo} es el gato de genero {sexo_max} mas viejo ({edad_max} años) \n el promedio de edad de las mascotas es de: {promedio_edad} años ")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()