import string
texo_usuario = input("Introduzca un texto")
espacios = 0
puntos = 0
comas = 0
for letra in texo_usuario:
    if letra == " ":
        espacios += 1
    elif letra == ".":
        puntos += 1
    elif letra == ",":
        comas += 1

print(f"Espacios: {espacios}, Puntos: {puntos}, Comas: {comas}")

# ejercicio 2
# ------------------------------------------------------------------#
texto_usuario = input("Introduzca un texto: ")
# lista de todas las letras
# print(string.ascii_uppercase)
letras_mayusculas = 0

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        letras_mayusculas += 1

print(f"Las mayusculas son {letras_mayusculas}")

# ejercicio 3
# ----------------------------------------------------#

numero = int(input("La tabla del: "))

for n in range(1, 11):
    if n % 2 == 0:
        print(f"{n}x{numero}={n*numero}")
