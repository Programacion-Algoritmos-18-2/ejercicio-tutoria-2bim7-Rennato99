import codecs
import sys

# Creamos la clase para poder leer el archivo
class MiArchivo:

	# Constructor
	def __init__(self, nombre, modo="r"):

		self.nombre = nombre
		self.modo = modo
		self.archivo = codecs.open(self.nombre, modo)

	# Metodo que lee la informacion y devuelve una lista de las lineas
	def obtener_informacion(self):
		return self.archivo.readlines()

	# Metodo para agregar informacion
	def agregar_informacion(self, informacion):
		if(self.modo == "r"): # Si el modo es r no dejara escribir
			print("Mode Error. Para poder agregar informacion a este archivo debe abrirlo en modo 'w' o 'a'")
			return
		# Si es 'a' o 'w' se puede escribir
		self.archivo.write("%s\n" % (informacion))

	# Metodo para cerrar el archivo
	def cerrar_archivo(self):
		self.archivo.close()
