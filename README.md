# Serpientela 🐍
<a href="https://www.python.org" target="_blank">
  <img src="https://img.shields.io/badge/Python-52BE80">
</a>

<br><br>

<img src="https://i.pinimg.com/236x/73/49/99/7349997a4d07fbb97180c9a526fb88ff.jpg">

**Serpientela** es un lenguaje de programación inspirado en Python, diseñado especialmente para hispanohablantes 
que desean aprender a programar en su idioma nativo. Con Serpientela, puedes escribir código en español utilizando 
una sintaxis intuitiva y accesible, lo que facilita la comprensión y el aprendizaje de conceptos de programación.

## Tabla de Contenidos 

1. Introducción
2. Características
3. Instalación
4. Configuración del estilo de Serpientela
5. Uso
6. Ejemplos
7. Referencia de Sintaxis
8. Contribuciones
9. Licencia

## Introducción 🌟

Serpientela está diseñado para ser un punto de partida sencillo para quienes están empezando en el mundo de la programación. 
Al traducir las palabras clave de Python al español, Serpientela ofrece una manera amigable de aprender los conceptos fundamentales 
de la programación sin la barrera del idioma.

## Características ✨

- **Sintaxis en Español**: Utiliza palabras en español para comandos y estructuras de control.
- **Fácil Aprendizaje**: Ideal para principiantes que no están familiarizados con el inglés técnico.
- **Compatible con Python**: Se basa en Python, por lo que muchas de las funcionalidades y estructuras son similares.

## Instalación 💻

Para usar Serpientela, necesitas tener Python instalado en tu sistema. Sigue estos pasos para instalar y configurar el entorno:

1. **Descarga Serpientela**:
   Clona el repositorio o descarga el archivo ZIP desde [GitHub](https://github.com/Bredalis/Serpientela).

   ```bash
   git clone https://github.com/Bredalis/Serpientela.git
   ```
   
2. **Configuración del Entorno**:
   Asegúrate de tener Python 3.x instalado. Puedes verificar la versión con:

   ```bash
   python --version
   ```
   
## Configuración del Estilo 🎨

Para poder ver las sentencias en colores distintivos, puede configurar un archivo .sublime-sintax en (Packages/User)

1. Crea el archivo de la siguiente manera, para configurar los colores en Sublime Text

   Ve a Tools > Developer > New Syntax....
   <br> Guarda el archivo en la carpeta de paquetes de Sublime (Packages/User/Serpientela.sublime-syntax)

2. Contenido del archivo:
  
  ```bash
   Sublime Text

   %YAML 1.2
   ---
   name: Serpientela
   file_extensions: [se]
   scope: source.serpientela

   contexts:
     main:
       - match: \b(imprimir|retornar|funcion|si|pero_si|sino|mientras|para|en|rango|entrada|y|o|no|lista|dicc|agregar|borrar_ultimo|ordenar|romper|continua|importar|de|abrir|leer|escribir|conjunto)\b
         scope: keyword.control.serpientela

       - match: \b(entero|flotante|caracter|booleano)\b
         scope: storage.type.serpientela

       - match: \b(y|o|no|Verdadero|Falso)\b
         scope: keyword.operator.logical.serpientela

       - match: '"'
         push: string

       - match: '#.*'
         scope: comment.line.number-sign.serpientela

       - match: \b[a-zA-Z_][a-zA-Z0-9_]*\b(?=\()
         scope: entity.name.function.serpientela
         push: function_parameters

       - match: \b[a-zA-Z_][a-zA-Z0-9_]*\b
         scope: variable.serpientela

       - match: '[=|>|<|\+|\-|\*|\/|%|&|\||\^|!|~]'
         scope: keyword.operator.serpientela

       - match: \b\d+(\.\d+)?\b
         scope: constant.numeric.serpientela

     function_parameters:
       - meta_scope: entity.name.function.serpientela
       - match: '\('
         pop: true

     string:
       - meta_scope: string.quoted.double.serpientela
       - match: '"'
         pop: true
```

## Uso 🚀

Para ejecutar un archivo `.se` con Serpientela, sigue estos pasos:

1. **Escribe tu Código en Serpientela**:
   Crea un archivo con extensión `.se` y escribe tu código en español siguiendo la sintaxis de Python.

2. **Ejecuta el Archivo**:
   Usa el intérprete para ejecutar el archivo, te pedirá  el nombre del archivo con su extensión:

   ```bash
   python Interprete.py tu_archivo.se
   ```

## Ejemplos 📚

Aquí tienes algunos ejemplos básicos de cómo escribir y ejecutar código en Serpientela:

### Hola Mundo

```serpientela
imprimir("Hola, Mundo")
```

### Función con Parámetros

```serpientela
funcion saludar(nombre):
    imprimir("Hola, " + nombre)

saludar("Carlos")
```

### Condiciones y Bucles

```serpientela
si 5 > 3:
    imprimir("Cinco es mayor que tres")

para i en rango(5):
    imprimir(i)
```

## Referencia de Sintaxis 📝

### Palabras Clave

- `imprimir`: Muestra un mensaje en pantalla.
- `retornar`: Devuelve un valor desde una función.
- `funcion`: Define una función.
- `si`: Estructura condicional.
- `para`: Bucle de iteración.
- `en`: Usado en bucles y condiciones.
- `rango`: Genera una secuencia de números.

### Tipos de Datos

- `entero`: Tipo de dato para números enteros.
- `flotante`: Tipo de dato para números con decimales.
- `caracter`: Tipo de dato para cadenas de texto.
- `booleano`: Tipo de dato para valores de verdadero o falso.
- `lista`: Estructura de datos para listas.
- `dicc`: Estructura de datos para diccionarios.

### Operadores

- `+`, `-`, `*`, `/`: Operadores aritméticos.
- `y`, `o`, `no`: Operadores lógicos.
- `=`, `==`, `<`, `>`: Operadores de comparación.

## Contribuciones 🤝

Si deseas contribuir a Serpientela, por favor sigue estos pasos:

1. Fork el repositorio.
2. Crea una rama nueva (`git checkout -b mi-nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Envía un pull request (`git push origin mi-nueva-funcionalidad`).

**Sería de mucha ayuda si contribuyes para ayudar a aquellas personas que están iniciando a programar y ni 
siquiera saben algo de inglés, para que sea un poco más fácil su curva de aprendizaje, ya que Serpientela necesita algunos 
arreglos para sacar su máximo potencial y ayudar a los demás 😁**

<br>

## Licencia 📜

Este proyecto está licenciado bajo la Licencia 📜 <a href="https://github.com/Bredalis/Serpientela/blob/master/LICENSE" target="_blank">MIT License</a>.

<br>

## <img src="https://avatars.githubusercontent.com/u/111624948?s=400&u=cd081f79392220d8cd2a22f2a8d5d3b18814350a&v=4" width="50" height="50"> <img src="https://readme-typing-svg.demolab.com?font=Roboto+Slab&color=%23FFFFFF&size=35&center=true&vCenter=true&width=450&duration=1500&pause=1000&lines=Hola,+soy;Bredalis+Gautreaux!" width="auto" height="35"/>
[![Github](https://img.shields.io/github/followers/Bredalis?label=Follow&style=social)](https://github.com/Bredalis)
![GitHub Followers](https://img.shields.io/github/stars/bredalis?style=social)
<a href="https://www.linkedin.com/in/bredalis-gautreaux/" target="_blank">
  <img src="https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white">
</a>

😊 Soy una programadora con 3 años en este sector, me encanta crear y aprender constantemente. ¡Amo lo que hago! #nlp #ia 😊

## Mira mi perfil de GitHub:
[![Web](https://img.shields.io/badge/GitHub-Bredalis-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/bredalis)

