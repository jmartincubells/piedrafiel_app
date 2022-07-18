# El pc que se vaya a usar debe tener sqlite3 para que funcione y la librería tkinter para python
# Elaborado por Camilo Andrés Barragán Gómez
from tkinter import ttk #Importar el ttk
from tkinter import * #Importar todo de tkiner
import tkinter as tk #Es para los menús
import sqlite3 #Importar la base de datos

class Usuarios: #Crear el objeto usuarios
    #Definir ventana de la aplicación
    def __init__(self, window): #Define la inicialización de la ventana
        self.wind = window #Variable de la ventana de la aplicación
        self.wind.title("Usuarios") #Título de la ventana de la aplicación
        window.config(bg = "old lace") #Color de fondo
        #Cuadro de registro
        Frame = LabelFrame(self.wind,text = "Registre un nuevo usuario", fg = "blue") #Label de mensaje para registrar usuarios
        Frame.grid(row = 0, column = 0, columnspan = 1, pady = 20) #row=Fila,columna=columna de texto, columspan= columna de relleno, pady=espacio entre elementos
        #Registrar usuarios
        #Ingresar el nombre
        Label(Frame, text = "Nombres: ").grid(row = 1, column = 0) #Cuadro donde escribirán los nombres de los estudiantes
        self.nombres = Entry(Frame) #Espacio donde escriben el nombre
        self.nombres.focus() #Lleva el cursos directamente a donde está el primer espacio que es el de nombres
        self.nombres.grid(row = 1, column = 1) #Lugar donde se ubicará el nombre a escribir
        #Ingresar el apellido
        Label(Frame, text = "Apellidos: ").grid(row = 2, column = 0) #Cuadro donde escribirán los apellidos del estudiante
        self.apellidos=Entry(Frame) #Cuadro donde escriben los apellidos del estudiante
        self.apellidos.grid(row = 2, column = 1) #Lugar donde se ubicará el apellido a escribir
        #Ingresar la Edad
        Label(Frame, text = "Edad: ").grid(row = 3,column = 0) #Cuadro donde se escribirá la edad del estudiante
        self.edad = Entry(Frame) #Entrada de texto
        self.edad.grid(row = 3, column = 1) #Posición
        #Ingresar código
        Label(Frame, text = "Código: ").grid(row = 4, column = 0) #Cuadro donde se escribirá el código del estudiante
        self.codigo = Entry(Frame) # Cuadro donde escribirá la edad del estudiante
        self.codigo.grid(row = 4, column = 1) #lugar donde se ubicará la edad a escribir
        #Ingresar programa académico
        Label(Frame, text = "Programa académico: ").grid(row = 5, column = 0) #Cuadro donde se escribirá el programa académico del estudiante
        self.programa = tk.StringVar(Frame) #Variable de control tipo cadena y lo guarda
        self.programa.set('-----------------') #Tipo select
        programas = ("Ingeniería Industrial", "Ingeniería de Software","Finanzas y Comercio Exterior", "Negocios Internacionales") #Opciones
        self.MenuPrograma = tk.OptionMenu(Frame, self.programa, *programas).grid(row = 5, column = 1) #Posición
        #Ingresar estado civil
        Label(Frame, text = "Estado civil: ").grid(row = 6, column = 0) #Cuadro donde se escribirá el estado civil del estudiante
        self.estado = tk.StringVar(Frame) #Variable de control tipo cadena y lo guarda
        self.estado.set('-----------------') #Tipo select
        estados = ("Casado(a)", "En relación", "Soltero(a)", "Viudo(a)") #Opciones
        self.MenuEstado = tk.OptionMenu(Frame, self.estado, *estados).grid(row = 6, column = 1) #Posición
        #Ingresar localidad
        Label(Frame, text = "Localidad: ").grid(row = 7, column = 0) #Cuadro donde se escribirá la localidad del estudiante
        self.localidad = tk.StringVar(Frame) #Variable de control tipo cadena y lo guarda
        self.localidad.set('-----------------') #Tipo select
        localidades = ("Antonio Nariño", "Chapinero", "Ciudad Bolívar", "Engativá", "Fontibón", "Fuera de Bogotá", "Kennedy", "Los Mártires", "Puente Aranda", "San Cristóbal", "Suba", "Usaquén") #Opciones
        self.MenuLocalidad = tk.OptionMenu(Frame, self.localidad, *localidades).grid(row = 7, column = 1) #Posición
        #Ingresar Horas en redes
        Label(Frame, text = "Horas en redes sociales: ").grid(row = 8, column = 0) #Cuadro donde se escribirá la cantidad de horas en redes sociales
        self.redes = Entry(Frame) #Entrada de texto
        self.redes.grid(row = 8, column = 1) #Posición
        #Ingresar horas en lectura
        Label(Frame, text = "Horas dedicadas a la lectura: ").grid(row = 9, column = 0) #Cuadro donde se escribirá las horas de lectura
        self.lectura = Entry(Frame) #Entrada de texto
        self.lectura.grid(row = 9, column = 1) #Posición
        #Ingresar tiempo trayecto
        Label(Frame, text = "Horas Universidad-Casa: ").grid(row = 10, column = 0) #Cuadro donde se escribirá el tiempo de trayecto
        self.trayecto = tk.StringVar(Frame) #Variable de control tipo cadena y lo guarda
        self.trayecto.set('-----------------') #Tipo select
        trayectos = (0.17, 0.33, 0.5, 0.67, 0.83, 1, 2) #Opciones
        self.MenuTrayecto = tk.OptionMenu(Frame, self.trayecto, *trayectos).grid(row = 10, column = 1) #Posición
        #Ingresar mascota
        Label(Frame, text = "¿Tiene mascota?: ").grid(row = 11, column = 0) #Cuadro donde se escribirá si tiene mascota o no
        self.mascota = tk.StringVar(Frame) #Variable de control tipo cadena y lo guarda
        self.mascota.set('-----------------') #Tipo select
        mascotas = ("Sí", "No") #Opciones
        self.MenuTrayecto = tk.OptionMenu(Frame, self.mascota, *mascotas).grid(row = 11, column = 1) #Posición
        #Botón para agregar a los estudiantes
        ttk.Button(Frame, text = "Guardar estudiante", command=self.AgregarEstudiantes).grid(row = 21, columnspan = 2, sticky = W+E) #Ubicación del botón guardar estudiante
        self.mensaje = Label(text = "", fg = "red") #Lugar donde se ubicará el espacio de los mensajes y el color
        self.mensaje.grid(row=2, column=0, columnspan=1, sticky=W+E) #Características del mensaje
        #Crear tabla
        self.tree = ttk.Treeview(height = 31 , columns =("#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#10", "#11")) #Tabla donde se verán los datos guardados, aquí se ve la creación
        self.tree.grid(row = 9, column = 0) #Ubicación de la tabla
        self.tree.heading("#0", text = "Nombre") #Ubicación de la columna nombres en la tabla
        self.tree.column("#0", width = 120) #Tamaño de la columna nombres
        self.tree.heading("#1", text = "Apellido") #Ubicación de la columna apellidos en la tabla
        self.tree.column("#1", width = 120) #Tamaño de la columna apellido
        self.tree.heading("#2", text = "Edad") #Ubicación de la columna edad en la tabla
        self.tree.column("#2", width = 40) #Tamaño de la columna edad
        self.tree.heading("#3", text = "Código") #Ubicación de la columna código en la tabla
        self.tree.column("#3", width = 65) #Tamaño de la columna código
        self.tree.heading("#4", text = "Programa") #Ubicación de la columna programa en la tabla
        self.tree.column("#4", width = 160) #Tamaño de la columna programa
        self.tree.heading("#5", text = "Estado") #Ubicación de la columna estado en la tabla
        self.tree.column("#5", width = 65) #Tamaño de la columna estado
        self.tree.heading("#6", text = "Localidad") #Ubicación de la columna localidad en la tabla
        self.tree.column("#6", width = 100) #Tamaño de la columna localidad
        self.tree.heading("#7", text = "Redes") #Ubicación de la columna redes en la tabla
        self.tree.column("#7", width = 50) #Tamaño de la columna redes
        self.tree.heading("#8", text = "Lectura") #Ubicación de la columna lectura en la tabla
        self.tree.column("#8", width = 50) #Tamaño de la columna lectura
        self.tree.heading("#9", text = "Trayecto") #Ubicación de la columna trayecto en la tabla
        self.tree.column("#9", width = 60) #Tamaño de la columna trayecto
        self.tree.heading("#10", text = "Mascota") #Ubicación de la columna mascota en la tabla
        self.tree.column("#10", width = 60) #Tamaño de la columna mascota
        #Crear botón de editar y de eliminar
        ttk.Button(Frame, text = "Eliminar estudiante", command = self.EliminarEstudiante).grid(row = 22, column=0, columnspan = 2, sticky= W+E) #Botón para eliminar usuarios
        ttk.Button(Frame, text = "Editar estudiante", command = self.EditarEstudiantes).grid(row = 23, column=0, columnspan = 2, sticky= W+E) #Botón para editar usuarios
        ttk.Button(Frame, text = "Actualizar lista", command = self.ActualizarLista).grid(row = 24, column=0, columnspan = 2, sticky = W+E) #Botón actualizar lista
        ttk.Button(Frame, text = "Promedios", command = self.Promedios).grid(row = 1, column = 4, columnspan = 2, sticky = W+E) #Botoón promedios
        Label(Frame, text = "El promedio está en la terminal").grid(row = 2, column = 4, columnspan = 2, sticky = W+E) #label de mensaje
        ttk.Button(Frame, text = "Buscar por código", command = self.Buscar).grid(row = 3, column = 4, columnspan = 2, sticky = W+E) #Botón de buscar por código
        Label(Frame, text = "El estudiante se mostrará en la terminal").grid(row = 4, column = 4, columnspan = 2, sticky = W+E) #Label de mensaje
        self.ObtenenerUsuarios()
        #Conectar base de datos
    DbName="databaseee.db" #Nombre de la base de datos
    def RunQuests(self, quests, parameters=()): #Conexión de una función a la base de datos, propiedades, preguntas y parámetros si los hay
        with sqlite3.connect(self.DbName) as conn: #conecta la base de datos y la asigna un nombre corto de la acción
            Cursor = conn.cursor() #Muestra en qué posición de la base de datos está
            Result = Cursor.execute(quests, parameters) #Ejecuta cada pregunta del programa para guardarlo en la base de datos
            conn.commit() #Guardar las preguntas
        return Result #Regresa la información
    #Nueva función de obtener los datos
    def ObtenenerUsuarios(self): #Obtener los usuarios
        Records = self.tree.get_children() #Mostrar datos de la tabla
        for element in Records: #ciclo para limpiarla en caso de que tenga información
            self.tree.delete(element) #comando delete
        quests = "SELECT * FROM Usuarios ORDER BY nombres ASC" #Esto es de SQL para consultar los datos
        DbRows = self.RunQuests(quests) #hacer que las filas vayan aumentando atuomáticamente
        for row in DbRows: #Rellenar los datos
            self.tree.insert("", 0, text = row[1], values = (row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])) #Espacios para ingresar los nuevos datos
    def Validacion(self): #Definir función para validar que el usuario llene todos los espacios
        return len(self.nombres.get())!=0 and len(self.apellidos.get())!=0 and len(self.edad.get())!=0 and len(self.codigo.get())!=0 and len(self.programa.get())!=0 and len(self.estado.get())!=0 and len(self.localidad.get())!=0 and len(self.redes.get())!=0 and len(self.lectura.get())!=0 and len(self.trayecto.get())!=0 and len(self.mascota.get())!=0 #Validación de que los datos no estén vacíos, si es distinto de 0 significa que el usuario ha ingresado algo
    def AgregarEstudiantes(self): #Definir función para que agregue los nuevos estudiantes a la base de datos
        if self.Validacion(): #Ejecuta la función validación y si es true permite el guardado
            quests = "INSERT into Usuarios VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            parameters = (self.nombres.get(), self.apellidos.get(), self.edad.get(), self.codigo.get(), self.programa.get(), self.estado.get(), self.localidad.get(), self.redes.get(), self.lectura.get(), self.trayecto.get(), self.mascota.get()) #Parámetros de entrada de estudiantes
            self.RunQuests(quests, parameters) #Correr la base de datos
            self.mensaje["text"] = "El estudiante {} {} ha sido agregado".format(self.nombres.get(), self.apellidos.get()) #Mensaje de que sí agregó el estudiante
            self.nombres.delete(0,END) #Reinicia el espacio de nombres
            self.apellidos.delete(0,END) #Reinicia el espacio de apellidos
            self.edad.delete(0,END) #Reinicia el espacio de edad
            self.codigo.delete(0,END) #Reinicia el espacio de código
            self.programa.set("-----------------") #Reinicia el espacio de programa académico
            self.estado.set("-----------------") #Reinicia el espacio de estado civil
            self.localidad.set("-----------------") #Reinicia el espacio de localidad
            self.redes.delete(0,END) #Reinicia el espacio de horas en redes
            self.lectura.delete(0,END) #Reinicia el espacio de horas de lectura
            self.trayecto.set("-----------------") #Reinicia el espacio de trayecto
            self.mascota.set("-----------------") #Reinicia el espacio de mascota
        else: #Acción por si no es verdadero
            self.mensaje["text"] = "Todos los datos son requeridos" #Impresión de lo que sea falso
        self.ObtenenerUsuarios() #Muestra la información de usuarios
    def ActualizarLista(self): #Definir función para que agregue los nuevos productos a la base de datos
        if self.Validacion(): #Ejecuta la función validación y si es true permite el guardado
            quests = "INSERT into Productos VALUES(NULL, ?, ?)" #Lo coloco para que actualice la tabla
            parameters = (self.nombres.get(), self.apellidos.get()) #Lo coloco para que actualice la tabla
            self.RunQuests(quests, parameters) #Correr la base de datos
            self.mensaje["text"] = "El estudiante {} ha sido agregado".format(self.nombres.get()) #Mensaje de que sí agregó el usuario
            self.nombres.delete(0,END) #Reinicia el espacio de nombres
            self.apellidos.delete(0,END) #Reinicia el espacio de apellidos
        else: #Acción por si no es verdadero
            self.mensaje["text"] = "" #Impresión de lo que sea falso
        self.ObtenenerUsuarios() #Muestra la información de usuarios
    def EliminarEstudiante(self): #Función para eliminar usuarios
        self.mensaje["text"] = "" #Reinicia el mensaje
        try:
            self.tree.item(self.tree.selection())["text"][0] #Intenta que si hay algo seleccionado deje que funcione el eliminar estudiante
        except IndexError as e:
            self.mensaje["text"] = "Por favor seleccione el estudiante que desea eliminar" #Mensaje por si no selecciona estudiante para borrar
            return #Regresa a valor de no tener algo seleccionado
        self.mensaje["text"] = "" #Reinicia el mensaje
        nombres = self.tree.item(self.tree.selection())["text"] #Le da el valor a nombres de lo que haya seleccionado
        quests = "DELETE FROM Usuarios WHERE nombres = ?" #Busca en la base de datos el usuario con el parámetro de nombres
        self.RunQuests(quests, (nombres, )) #Elimina el usuario que se encuentra en nombres
        self.mensaje["text"] = "El estudiante {} ha sido eliminado de la faz de la Tierra satisfactoriamente".format(nombres) #Mensaje de que borró el estudiante seleccionado
        self.ObtenenerUsuarios #Muestra los usuarios actualizados en la tabla
    def EditarEstudiantes(self):
        self.mensaje["text"] = "" #Reinicia el mensaje
        try:
            self.tree.item(self.tree.selection())["text"][0] #Intenta que si hay algo seleccionado deje que funcione el eliminar estudiante
        except IndexError as e:
            self.mensaje["text"] = "Por favor seleccione el estudiante que desea editar" #Mensaje por si no selecciona estudiante para borrar
            return #Regresa a valor de no tener algo seleccionado
        nombres = self.tree.item(self.tree.selection())["text"] #Texto que va a tomar de la DB
        OldApellidos = self.tree.item(self.tree.selection())["values"][0] #Valor que va a tomar de la DB
        OldEdad = self.tree.item(self.tree.selection())["values"][1] #Valor que va a tomar de la DB
        OldCodigo = self.tree.item(self.tree.selection())["values"][2] #Valor que va a tomar de la DB
        OldPrograma = self.tree.item(self.tree.selection())["values"][3] #Valor que va a tomar de la DB
        OldEstado = self.tree.item(self.tree.selection())["values"][4] #Valor que va a tomar de la DB
        OldLocalidad = self.tree.item(self.tree.selection())["values"][5] #Valor que va a tomar de la DB
        OldRedes = self.tree.item(self.tree.selection())["values"][6] #Valor que va a tomar de la DB
        OldLectura = self.tree.item(self.tree.selection())["values"][7] #Valor que va a tomar de la DB
        OldTrayecto = self.tree.item(self.tree.selection())["values"][8] #Valor que va a tomar de la DB
        OldMascota = self.tree.item(self.tree.selection())["values"][9] #Valor que va a tomar de la DB
        self.editwind = Toplevel() #Abrir nueva ventana
        self.editwind.tittle = "Editar estudiante" #Nombre de la nueva ventana
        #Antiguos nombres
        Label(self.editwind, text = "Antiguos nombres").grid(row = 0, column = 1)
        Entry(self.editwind, textvariable = StringVar(self.editwind, value = nombres), state = "readonly").grid(row = 0, column = 2)
        #Nuevos nombres
        Label(self.editwind, text = "Nuevos nombres").grid(row = 1, column = 1)
        NuevosNombres = Entry(self.editwind)
        NuevosNombres.grid(row = 1, column = 2)
        #Antiguos apellidos
        Label(self.editwind, text = "Antiguos apellidos").grid(row = 2, column = 1)
        Entry(self.editwind, textvariable = StringVar(self.editwind, value = OldApellidos), state = "readonly").grid(row = 2, column = 2)
        #Nuevos apellidos
        Label(self.editwind, text = "Nuevos apellidos").grid(row = 3, column = 1)
        NuevosApellidos = Entry(self.editwind)
        NuevosApellidos.grid(row = 3, column = 2)
        #Antigua edad
        Label(self.editwind, text = "Antigua edad").grid(row = 4, column = 1)
        Entry(self.editwind, textvariable = StringVar(self.editwind, value = OldEdad), state = "readonly").grid(row = 4, column = 2)
        #Nueva edad
        Label(self.editwind, text = "Nueva edad").grid(row = 5, column = 1)
        NuevoEdad = Entry(self.editwind)
        NuevoEdad.grid(row = 5, column = 2)
        #Antiguo código
        Label(self.editwind, text = "Antiguo código").grid(row = 6, column = 1)
        Entry(self.editwind, textvariable = StringVar(self.editwind, value = OldCodigo), state = "readonly").grid(row = 6, column = 2)
        #Nuevo código
        Label(self.editwind, text = "Nuevo código").grid(row = 7, column = 1)
        NuevoCodigo = Entry(self.editwind)
        NuevoCodigo.grid(row = 7, column = 2)
        #Antiguo programa
        Label(self.editwind, text = "Antiguo programa").grid(row = 8, column = 1)
        Entry(self.editwind, textvariable = StringVar(self.editwind, value = OldPrograma), state = "readonly").grid(row = 8, column = 2)
        #Nuevo programa
        Label(self.editwind, text = "Nuevo programa académico").grid(row = 9, column = 1)
        self.NuevoPrograma = tk.StringVar(self.editwind) #Variable de control tipo cadena y lo guarda
        self.NuevoPrograma.set('-----------------') #
        NuevoProgramas = ("Ingeniería Industrial", "Ingeniería de Software","Finanzas y Comercio Exterior", "Negocios Internacionales")
        self.MenuNuevoPrograma = tk.OptionMenu(self.editwind, self.NuevoPrograma, *NuevoProgramas).grid(row = 9, column = 2)
        #Antiguo estado
        Label(self.editwind, text = "Antiguo estado civil").grid(row = 10, column = 1)
        Entry(self.editwind, textvariable = StringVar(self.editwind, value = OldEstado), state = "readonly").grid(row = 10, column = 2)
        #Nuevo estado
        Label(self.editwind, text = "Nuevo estado civil").grid(row = 11, column = 1)
        self.NuevoEstado = tk.StringVar(self.editwind) #Variable de control tipo cadena y lo guarda
        self.NuevoEstado.set('-----------------') #
        NuevoEstados = ("Casado(a)", "En relación", "Soltero(a)", "Viudo(a)")
        self.MenuNuevoEstados = tk.OptionMenu(self.editwind, self.NuevoEstado, *NuevoEstados).grid(row = 11, column = 2)
        #Antigua localidad
        Label(self.editwind, text = "Antigua localidad").grid(row = 12, column = 1)
        Entry(self.editwind, textvariable = StringVar(self.editwind, value = OldLocalidad), state = "readonly").grid(row = 12, column = 2)
        #Nueva localidad
        Label(self.editwind, text = "Nueva localidad").grid(row = 13, column = 1)
        self.NuevoLocalidad = tk.StringVar(self.editwind) #Variable de control tipo cadena y lo guarda
        self.NuevoLocalidad.set('-----------------') #
        NuevoLocalidades = ("Antonio Nariño", "Chapinero", "Ciudad Bolívar", "Engativá", "Fontibón", "Fuera de Bogotá", "Kennedy", "Los Mártires", "Puente Aranda", "San Cristóbal", "Suba", "Usaquén")
        self.MenuNuevoLocalidad = tk.OptionMenu(self.editwind, self.NuevoLocalidad, *NuevoLocalidades).grid(row = 13, column = 2)
        #Antiguo redes
        Label(self.editwind, text = "Antiguo tiempo en redes").grid(row = 14, column = 1)
        Entry(self.editwind, textvariable = StringVar(self.editwind, value= OldRedes), state = "readonly").grid(row = 14, column = 2)
        #Nuevo redes
        Label(self.editwind, text = "Nuevo tiempo en redes").grid(row = 15, column = 1)
        self.NuevoRedes = tk.StringVar(self.editwind) #Variable de control tipo cadena y lo guarda
        self.NuevoRedes.set('-----------------') #
        NuevoHRedes = (1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 17)
        self.MenuNuevoRedes = tk.OptionMenu(self.editwind, self.NuevoRedes, *NuevoHRedes).grid(row = 15, column = 2)
        #Antiguo lectura
        Label(self.editwind, text = "Antiguo tiempo de lectura").grid(row = 16, column = 1)
        Entry(self.editwind, textvariable = StringVar(self.editwind, value= OldLectura), state = "readonly").grid(row = 16, column = 2)
        #Nuevo lectura
        Label(self.editwind, text = "Nuevo tiempo de lectura").grid(row = 17, column = 1)
        self.NuevoLectura = tk.StringVar(self.editwind) #Variable de control tipo cadena y lo guarda
        self.NuevoLectura.set('-----------------') #
        NuevoLecturas = (0, 1, 2, 3, 4, 5)
        self.MenuNuevoLectura = tk.OptionMenu(self.editwind, self.NuevoLectura, *NuevoLecturas).grid(row = 17, column = 2)
        #Antiguo trayecto
        Label(self.editwind, text = "Antiguo tiempo de trayecto").grid(row = 18, column = 1)
        Entry(self.editwind, textvariable = StringVar(self.editwind, value= OldTrayecto), state = "readonly").grid(row = 18, column = 2)
        #Nuevo trayecto
        Label(self.editwind, text = "Nuevo tiempo de trayecto").grid(row = 19, column = 1)
        self.NuevoTrayecto = tk.StringVar(self.editwind) #Variable de control tipo cadena y lo guarda
        self.NuevoTrayecto.set('-----------------') #
        NuevoTrayectos = (0.17, 0.33, 0.5, 0.67, 0.83, 1, 2)
        self.MenuNuevoTrayectos = tk.OptionMenu(self.editwind, self.NuevoTrayecto, *NuevoTrayectos).grid(row = 19, column = 2)
        #Antiguo mascota
        Label(self.editwind, text = "Antiguo mascota").grid(row = 20, column = 1)
        Entry(self.editwind, textvariable = StringVar(self.editwind, value= OldMascota), state = "readonly").grid(row = 20, column = 2)
        #Nuevo mascota
        Label(self.editwind, text = "Nuevo mascota").grid(row = 21, column = 1)
        self.NuevoMascota = tk.StringVar(self.editwind) #Variable de control tipo cadena y lo guarda
        self.NuevoMascota.set('-----------------') #
        NuevoMascotas = ("Sí", "No")
        self.MenuNuevoMascota = tk.OptionMenu(self.editwind, self.NuevoMascota, *NuevoMascotas).grid(row = 21, column = 2)
        Button(self.editwind, text = "Actualizar datos", command = lambda: self.DatosGuardados(NuevosNombres.get(), nombres, NuevosApellidos.get(), OldApellidos, NuevoEdad.get(), OldEdad, NuevoCodigo.get(), OldCodigo, self.NuevoPrograma.get(), OldPrograma, self.NuevoEstado.get(), OldEstado, self.NuevoLocalidad.get(), OldLocalidad, self.NuevoRedes.get(), OldRedes, self.NuevoLectura.get(), OldLectura, self.NuevoTrayecto.get(), OldTrayecto, self.NuevoMascota.get(), OldMascota)).grid(row = 22, column = 2, sticky = W) #Lambda que va a cambiar los valores que queremos editar
    def DatosGuardados(self, NuevosNombres, Nombres, NuevosApellidos, OldApellidos, NuevoEdad, OldEdad,  NuevoCodigo, OldCodigo, NuevoPrograma, OldPrograma, NuevoEstado, OldEstado, NuevoLocalidad, OldLocalidad, NuevoRedes, OldRedes, NuevoLectura, OldLectura, NuevoTrayecto, OldTrayecto, NuevoMascota, OldMascota): #Datos que va a toamr la DB para poderlos editar
        quests = "UPDATE Usuarios SET nombres = ?, apellidos = ?, edad = ?, codigo = ?, programa = ?, estado = ?, localidad = ?, redes = ?, lectura = ?, trayecto = ?, mascota = ? WHERE nombres = ? AND apellidos = ? AND edad = ? AND codigo = ? AND programa = ? AND estado = ? AND localidad = ? AND redes = ? AND lectura = ? AND trayecto = ? AND mascota = ?" #Sentencia SQL
        parameters = (NuevosNombres, NuevosApellidos, NuevoEdad, NuevoCodigo, NuevoPrograma, NuevoEstado, NuevoLocalidad, NuevoRedes, NuevoLectura, NuevoTrayecto, NuevoMascota, Nombres, OldApellidos, OldEdad, OldCodigo, OldPrograma, OldEstado, OldLocalidad, OldRedes, OldLectura, OldTrayecto, OldMascota) #Parámetros que va a tomar
        self.RunQuests(quests, parameters)
        self.editwind.destroy()
        self.mensaje["text"] = "El usuario {} ha sido actualizado".format(NuevosNombres)
        self.ObtenenerUsuarios
    def Promedios(self, parameters = ()): #Función de promedios
        with sqlite3.connect(self.DbName) as conn: #Conexión a la base de datos
            cursor = conn.cursor() #Asignar variable
            cursor.execute("SELECT AVG(Redes) FROM Usuarios;") #Sentencia SQL
            tiempoRedes = cursor.fetchall() #Asignar variable
            print("El promedio de tiempo en redes de todos los estudiantes es: ", tiempoRedes) #Imprimir variable
            cursor.execute("SELECT AVG(Lectura) FROM Usuarios;") #Sentencia SQL
            tiempoLectura = cursor.fetchall() #Asignar variable
            print("El promedio de tiempo de lectura de todos los estudiantes es:", tiempoLectura) #Imprimir variable
    def Buscar(self, parameters = ()): #Función de buscar estudiantes por código
        with sqlite3.connect(self.DbName) as conn: #Conexión a la base de datos
            cursor = conn.cursor() #Asignar variable
            cursor.execute #Sentencia SQL
            Codigo = int(input("Por favor introduzca el código: ")) #Asignar variable
            cursor.execute("SELECT * FROM Usuarios where Codigo=%d;" %Codigo)  #Sentencia SQL
            codigos = cursor.execute("SELECT * FROM Usuarios where Codigo=%d;" %Codigo) #Imprimir variable
            if codigos: #Condicional de encontrarlo
                cedulaEstudiante = cursor.fetchall()
                for i in cedulaEstudiante: #Ciclo para recorrer la lista y dar la información del estudiante
                    print(i) #Imprimir lo que va encontrando en la lista
                    print("El primer número que sale es el ID de la DB") #Mensaje
            else: #Condición falsa
                print("Código no encontrado y no se mostrará nada") #Mensaje
if __name__=="__main__": #Comprobar que funcione la aplicación, la ventana
            window=Tk()
            application=Usuarios(window)
            window.mainloop()