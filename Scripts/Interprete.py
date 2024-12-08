
import re

def cargar_archivo(nombre_archivo):
    """
    Carga el contenido de un archivo dado.
    """
    try:
        with open(nombre_archivo, "r") as archivo:
            return archivo.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        exit(1)

def traducir_a_python(codigo_serpientela, palabras_clave):
    """
    Traduce el código en Serpientela a Python.
    """
    def reemplazar_fuera_de_cadenas(match):
        texto = match.group(0)
        if texto.startswith(('"', "'")):
            return texto  # No modificar si es una cadena de texto

        for clave, valor in palabras_clave.items():
            texto = re.sub(rf'\b{clave}\b', valor, texto) # Reemplazo preciso
        return texto

    # Patrón para encontrar cadenas de texto y bloques de código
    patron = r'("[^"]*"|\'[^\']*\'|[^"\']+)'
    return re.sub(patron, reemplazar_fuera_de_cadenas, codigo_serpientela)

def ejecutar_codigo(codigo_python):
    """
    Ejecuta el código Python traducido.
    """
    try:
        exec(codigo_python)
    except Exception as e:
        print(f"Error al ejecutar el código traducido: {e}")

def main():
    print("\nSerpientela es Python en español. Disfrútalo ^_^")
    print("Nuestra URL para más información: https://github.com/Bredalis/Serpientela\n")

    # Solicitar el nombre del archivo
    nombre_archivo = input("Ingrese el nombre del archivo (con extensión .se): ")
    codigo_serpientela = cargar_archivo(nombre_archivo)

    # Diccionario de palabras clave de Serpientela a Python
    palabras_clave = {
        "imprimir": "print", "retornar": "return", "funcion": "def",
        "si": "if", "pero_si": "elif", "sino": "else", "mientras": "while",
        "para": "for", "en": "in", "rango": "range", "entrada": "input",
        "y": "and", "oh": "or", "no": "not", "lista": "list",
        "dicc": "dict", "agregar": "append", "borrar_ultimo": "pop",
        "ordenar": "sort", "romper": "break", "continua": "continue",
        "importar": "import", "de": "from", "abrir": "open", "leer": "read",
        "escribir": "write", "entero": "int", "flotante": "float",
        "caracter": "str", "booleano": "bool", "Verdadero": "True",
        "Falso": "False", "conjunto": "set"
    }

    # Traducir el código de Serpientela a Python
    codigo_python = traducir_a_python(codigo_serpientela, palabras_clave)  

    # Ejecutar el código Python traducido
    print("\n--- Resultado de Serpientela ---\n")
    ejecutar_codigo(codigo_python)
    print("\n--- Programa finalizado ---")

if __name__ == "__main__":
    main()