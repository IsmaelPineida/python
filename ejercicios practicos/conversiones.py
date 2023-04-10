#conversor de farenheit a centigrados
print
def menu():
   print("1. farenheit a centigrados") 
   print("2. conversor de divisas de libras a euros") 
   print() 
   print("0. salir") 
   opcion =int(input("elija una opcion: \n"))
   return opcion

while True: 
    opcion =menu()
    if(opcion==1):
        fa=float(input("Ingrese los grados farenheit:\n"))
        conver=(fa-32)*5/9
        print(f"el resultado es {conver} grados centigrados")
    elif(opcion==2):
        li=float(input("ingrese la cantidad de libras\n"))
        di=float(input("ingrese el cambio\n"))
        res=li*di
        print(f"el resultado es {res} libras")
    elif (opcion==0):
        break
    else:
        print("ingrese una opcion del menu")
        print("opcion no encontrada")
    print("\n\n")

print("Salimos :D")

   
        
    
    