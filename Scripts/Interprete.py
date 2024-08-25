
import re

# Código que ejecuta el lenguaje Serpientela

try:
	nombre_archivo = input("Ingrese el nombre del archivo: ")

	print("\nSerpientela es Python en español. Disfrutalo ^_^")
	print("Nuestra url para más información: https://github.com/Bredalis/Serpientela\n")

	contenido_archivo = open(nombre_archivo).read()

	sentencias = {
	    "imprimir": "print", "retornar": "return",
	    "funcion": "def", "si": "if", "pero_si": "elif",
	    "sino": "else", "mientras": "while", "para": "for",
	    "en": "in", "rango": "range", "entrada": "input",
	    "y": "and", "oh": "or", "no": "not", "lista": "list",
	    "dicc": "dict", "agregar": "append", "borrar_ultimo": "pop",
	    "ordenar": "sort", "romper": "break", "continua": "continue",
	    "importar": "import", "de": "from", "abrir": "open", "leer": "read",
	    "escribir": "write", "entero": "int", "flotante": "float", "caracter": "str",
	    "booleano": "bool", "Verdadero": "True", "Falso": "False", "conjunto": "set"
	}

	def reemplazar_fuera_de_cadenas(match):
		texto = match.group(0)
		if texto.startswith(('"', "'")):
		    return texto  # No modificar si es una cadena de texto
		
		for clave, valor in sentencias.items():
		    texto = texto.replace(clave, valor)
		
		return texto

    # Expresión regular para encontrar cadenas de texto y bloques de código
	patron = r'("[^"]*"|\'[^\']*\'|[^"\']+)'
	contenido_traducido = re.sub(patron, reemplazar_fuera_de_cadenas, contenido_archivo)

	exec(contenido_traducido)

finally:
	print("\nPrograma finalizado")