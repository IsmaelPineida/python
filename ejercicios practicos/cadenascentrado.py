#vamos a hacer algunas cosas con la cadena de string
texto = "esto es un texto de prueba"
#conprovar si la cadena empiesa con algua palabra en especifico
print("la cadena empieza con: ", texto.startswith("esto"))
#para comprobar si temina en una palabra en especifico
print("la cadena empieza con: ", texto.endswith("prueba"))
#convermimos la cadena en minuscula para ver
print("la cadena empieza con: ", texto.lower().endswith("Prueba".lower()))
#------------------------------------------------#
#alinear el texto
#centrado con un numoer de caracteres
print(texto.center(80,'-'))
#sirve para ver la longitud de la cadena
longitudcadena=len(texto)
print(longitudcadena)
#agregamos la longitud de la cadena y sumamos 37 para que se centre a 60 pixeles
print(texto.center(longitudcadena+37,'-'))
#agregar textos por la derecha y por la isquierda
print(texto.ljust(80,'-'))
#centrar textos a la derecha
print(texto.rjust(80,'0'))
#eliminar espacios en blanco
texto = "   Esta cadena tiene espacios      en blanco y         simbolo     s raros *-/*-+`1`~~~~~~/.,<>><>"
print(texto)
print("Cadena ya corregida sin espacios----")
print(texto.strip())
#sustituir texto
print(texto.replace('-',"hola"))