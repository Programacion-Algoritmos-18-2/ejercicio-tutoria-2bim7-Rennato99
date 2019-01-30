# Importamos las clases necesarios
from archivo.miArchivo import *
from modelo.miModelo import *


# Instanciamos los objetos de las clases que vamos a necesitar
archivo = MiArchivo(nombre="data/archivo-datos-combinacion.txt")
operaciones = Operaciones()

# Obtenemos una lista con cada linea del archivo
lista = archivo.obtener_informacion()

# Creamos una nueva lista para guardar las Personas
listaPersonas = []

lista = [linea.split(";") for linea in lista]	 # Dividimos cada linea en otra lista

# Recorremos la lista y creamos los objetos Persona
for elemento in lista:

    persona = Persona(elemento[0], elemento[1], elemento[2])
    listaPersonas.append(persona)


# Creamos una lista para extraer las edades de las personas
listaEdades = []
for persona in listaPersonas:
    print(persona)
    listaEdades.append(persona.getEdad())


# Obtenemos la lista de edades ordenada
listaEdadesOrdenada = operaciones.merge_sort(listaEdades)

# Imprimimos la lista ordenada
print("\nLa lista de edades ordenada es: ",listaEdadesOrdenada)
