a =[1,2,3,4,5,6,7,8,9,10]
frace="hola soy una frace"
vocales =["a","e","i","o","u"]
vocales_encontradas=0
for item in a:
    print(item)
    

lsita_de_compra=["leche","arroz","jamon"]
for item in lsita_de_compra:
    print(f"Hoy vou a comprar {lsita_de_compra}")

for letra in frace:
    if letra in vocales:
        print("He encontrado una '{}'".format(letra))
        vocales_encontradas+=1
        
        
print(f"he ecnotrado: {vocales_encontradas} vocales")  