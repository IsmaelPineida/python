#como declarar una lista
a=[]
#como agregar por codigo a una lista
a.append(1)
#como quitar la ultima posicion de una lista 
a.pop
#como medir el tamanio de una lista 
len(a)
#imprimir una lista
#print(a)
#consutalr si hay un elemento en la lista
1 in a 
#------------------------------------------------------#
lista_compra=[]
input_usuario=None
print("programa lista de compras")
while True:
    input_usuario=input("¿Que desas comprar ([Q] para salir:)")
    if input_usuario=="Q":
        break
    elif input_usuario in lista_compra:
        print(f"{input_usuario} ya esta en la lista")
    else:
        if input("Seguro que quieres aniadir {} a la lista de compra[S/N]".format(input_usuario))=="S":
            lista_compra.append(input_usuario)
            print("Prducto agregado con exito")

print("la lista de la compra es:")
print(lista_compra)