numeros_de_usuario=[]
"""numero_introducido=int(input("Introduzca un numero en la lista: "))
numeros_de_usuario.append(numero_introducido)


while input("¿Desea introducir mas numeros? [S/N]")=="S":
    numero_introducido=int(input("Introduzca un numero en la lista: "))
    numeros_de_usuario.append(numero_introducido)"""
    
numero_introducido = input("Introduzca numeros por coma: ")
numeros_de_usuario=[int(numero)for numero in numero_introducido.split(",")]    

    

numero_pequenio = numeros_de_usuario[0]
numero_grande =numeros_de_usuario[0]

for numero in numeros_de_usuario[1:]:#filtrado de listas
    if numero_pequenio > numero:
        numero_pequenio = numero
    if numero_grande <numero:
        numero_grande=numero
        
        
print(f"Numero grande: {numero_grande}\nNumero pequenio: {numero_pequenio}")