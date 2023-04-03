#funcion map
lista=[23,25,26,28,29,26,48,236,46,6]
print(list(map((lambda valor:valor*valor),lista)))
#funciones anonimas para realizar una vez en el codigo
#no se falta poner nombre a la funcion
#funcion filter vamos usar filtros 
print(list(filter((lambda valor:valor%2==0),lista)))
#con esta funcion sacamos los numeros que son pares

#funcion reduce
#nos va a devolver un valor
#importamos el modulo functools
import functools
print(str(functools.reduce((lambda x,resultado:x+resultado),lista)))
#hacemos que el valor de x sea el resultado de la suma de todos los datos de la lista 
#mostando asi el valor de toda la lista
