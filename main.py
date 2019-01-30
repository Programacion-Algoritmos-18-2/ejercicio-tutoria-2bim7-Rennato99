# Importamos las clases necesarios
from archivo.miArchivo import *
from modelo.miModelo import *
from data import *

# Instanciamos los objetos de las clases que vamos a necesitar
archivo = MiArchivo(nombre="archivo-datos-combinacion.txt")
operaciones = Operaciones()

# Obtenemos una lista con cada linea del archivo
lista = archivo.obtener_informacion()

# Creamos una nueva lista para guardar las Personas
listaPersonas = []

# Recorremos la lista y creamos los objetos Persona
for i in lista:
    lista[i].split(";")

    for elemento in lista[i]:
        persona = Persona(elemento[0], elemento[1], elemento[2])
        listaPersonas.append(persona)


# Creamos una lista para extraer las edades de las personas
listaEdades = []
for persona in listaPersonas:
    listaEdades.append(persona.getEdad())


# Obtenemos la lista de edades ordenada
listaEdadesOrdenada = operaciones.merge_sort(listaEdades)
