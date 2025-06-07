import random # importamos random

def generador_contraseña(cantidadNum, cantidadCarac, cantidadEspecial):
    numeros = ["0","1","2","3","4","5","6","7","8","9"] 
    caracteres= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"] 
    caracteres_mayusuclas = [elemento.upper() for elemento in caracteres]
    caracteres.extend(caracteres_mayusuclas)
    especiales = ["$","/","@","-","%","&",":",";","!"] 
    contraseña = [] # creamos una lista donde estará la contraseña
    for i in range(1, cantidadNum+1): # una ciclo que se repita las veces que se desea escoger la cantidad de numeros que solicita el usuario
        contraseña.append(random.choice(numeros)) # se elije un numero random de la lista y se agrega a la lista contraseña
    
    
    for i in range(1, cantidadCarac+1): # una ciclo que se repita las veces que se desea escoger la cantidad de caracteres que solicita el usuario
        contraseña.append(random.choice(caracteres))
        
        
    for i in range(1, cantidadEspecial+1): 
        contraseña.append(random.choice(especiales))
    
        

    random.shuffle(contraseña) 

    contraseña_real = "".join(contraseña)
    
    return contraseña_real
    
def programa():
    while True:
        while True:
            try:
                cantidad_num = int(input("Ingresa la cantidad de numeros que desea en su contraseña: ")) # decimos al usuario la cantidad de numeros en su contraseña
                break
            except ValueError:
                print("Ingresa solo valores númericos enteros")
        while True:
            try:
                cantidad_caracteres = int(input("Ingresa la cantidad de carácteres que desea en su contraseña: ")) 
                break
            except ValueError:
                print("Ingresa solo valores númericos enteros")
        while True:
            try:
                cantidad_especiales = int(input("Ingresa la cantidad de carácteres especiales que desea en su contraseña: ")) 
                break
            except ValueError:
                print("Ingresa solo valores númericos enteros")
        contraseña = generador_contraseña(cantidad_num, cantidad_caracteres, cantidad_especiales)
        print(f"La contraseña es {contraseña}")
        
        while True:
            try:
                option = int(input("\n¿Desea continuar?\n1.-Si\n2.-No\n"))
            except ValueError:
                print("Ingresa un valor númerico")
            if option == 1:
                break
            elif option ==2:
                return
            else:
                print("Ingresa un valor especifícado\n")
            
programa()
            
            





