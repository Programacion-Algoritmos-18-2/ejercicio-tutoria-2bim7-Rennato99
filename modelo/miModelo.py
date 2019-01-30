class Persona:

	# Constructor
	def __init__(self, nombre="", apellido="", edad=""):

		self.setNombre(nombre)
		self.setApellido(apellido)
		self.setEdad(edad)

	# Metodos set
	def setNombre(self, nombre):
		self.nombre = nombre

	def setApellido(self, apellido):
		self.apellido = apellido

	def setEdad(self, edad):
		self.edad = int(edad)

	# Metodos get
	def getNombre(self):
		return self.nombre

	def getApellido(self):
		return self.apellido

	def getEdad(self):
		return self.edad

	# Metodo que representa el objeto
	def __str__(self):
		return ("%s - %s - %s"%(self.getNombre(), self.getApellido(), self.getEdad()))

	def __repr__(self):
		return self.__str__()

# Creamos la clase operaciones
class Operaciones(object):

    # Constructor
    def __init__(self):
        pass

    # Función merge_sort
    def merge_sort(self, lista):
        """
            Lo primero que se ve en el psudocódigo es un if que
            comprueba la longitud de la lista. Si es menor que 2, 1 o 0, se devuelve la lista.
            ¿Por que? Ya esta ordenada.
        """
        if len(lista) < 2:
            return lista
        # De lo contrario, se divide en 2
        else:
            middle = len(lista) // 2
            right = merge_sort(lista[:middle])
            left = merge_sort(lista[middle:])
            return merge(right, left)

    # Función merge
    def merge(self, lista1, lista2):
        """
            merge se encargara de intercalar los elementos de las dos
            divisiones.
        """
        i, j = 0, 0 # Variables de incremento
        result = [] # Lista de resultado

        # Intercalar ordenadamente
        while(i < len(lista1) and j < len(lista2)):
            if (lista1[i] < lista2[j]):
                result.append(lista1[i])
                i += 1
            else:
                result.append(lista2[j])
                j += 1
        # Agregamos los resultados a la lista
        result += lista1[i:]
        result += lista2[j:]

        # Retornamos el resultados
        return result
