#bibliotecas necesarias: pip install psycopg2, pip install tkinter

from tkinter import *
import psycopg2

#Creo la ventana
windows = Tk()
windows.title("Formulario")
windows.geometry("400x600")
windows.resizable(0,0)

#funcion extra para mas estetica en los widget's entry
def borrado_entry(entry):
    entry.widget.delete(0,END)

#funcion para guardar el estudiante en la base de datos
def guardar_estudiante(nombre,edad,turno):

    conn = psycopg2.connect(dbname="postgres",
        user="postgres",
        password="12345",
        host="localhost")
    
    cursor = conn.cursor()

    query_insert = """INSERT INTO students VALUES(%s,%s,%s)"""
    cursor.execute(query_insert,(nombre,edad,turno))

    conn.commit()
    conn.close()

    mostrar_estudiantes()

#funcion para recuperar los datos de la tabla mediante una consulta
def mostrar_estudiantes():

    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="12345",
        host="localhost")
    cursor = conn.cursor()

    query_datos = """SELECT * FROM students"""
    cursor.execute(query_datos)

    #creo un widget Listbox para mostrar los datos de la tabla consultada
    lista = cursor.fetchall()
    panel = Listbox(windows,width=25,height=20)
    panel.place(x=70, y= 240)

    for i in lista:
        panel.insert(END,i)

    conn.commit()
    conn.close()
    


#todo el codigo para la interfaz
aviso1 = Label(windows, text="FORMULARIO DE NUEVO USUARIO", font="Arial 12")
aviso1.pack(anchor="center")

aviso2 = Label(windows, text="Ingrese sus datos", font="Arial 11")
aviso2.place(x=130,y=25)

nombre = Label(windows, text="Nombre:", font="Arial 12")
nombre.place(x=50,y=70)
entrada_nombre = Entry(windows)
entrada_nombre.bind("<FocusIn>",borrado_entry)
entrada_nombre.place(x=150, y=74)

edad = Label(windows, text="Edad:", font="Arial 12")
edad.place(x=50,y=100)
entrada_edad = Entry(windows)
entrada_edad.bind("<FocusIn>",borrado_entry)
entrada_edad.place(x=150, y=104)

turno = Label(windows, text="Turno:", font="Arial 12")
turno.place(x=50,y=130)
entrada_turno = Entry(windows)
entrada_turno.bind("<FocusIn>",borrado_entry)
entrada_turno.insert(0,"matutino/vespertino")
entrada_turno.place(x=150,y=134)

bonton_guardar = Button(windows,text="GUARDAR", font="Arial 12", command=lambda:guardar_estudiante(
    entrada_nombre.get(),
    entrada_edad.get(),
    entrada_turno.get()
))
bonton_guardar.place(x=140, y= 170)

registrados = Label(windows, text="Alumnos ya Registrados", font="Arial 11")
registrados.place(x=110, y= 210)

mostrar_estudiantes()

windows.mainloop()