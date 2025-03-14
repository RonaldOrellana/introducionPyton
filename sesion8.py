# if una opcion 
#condicion true o false 

if 4==7 : 
    print(" es igual")

if 4 != 7 :
     print(" es diferente")

     # numero par, impar, negativo o positivo 

     respuesta = int(input("Ingrese el numero :"))
     

     if respuesta % 2 == 0 :
          print(" Es par")
     else:  
         print(" Es impar ")

     if respuesta < 0 :
          print(" negativo")
     else:  
          print(" Es positivo ")
     if respuesta == 0:
         print("El numero es cero")

print("_____________________________________________________")
respuesta1= " Es par" if respuesta % 2 == 0 else " Es impar"
respuesta2 = " Negativo" if respuesta < 0 else " positivo"
print (f"{respuesta1} , {respuesta2}")
      
      # definir el numero par 
      #def nombre ():

def Modulo (valor):
 valor = True if respuesta % 2 == 0 else False
 print (valor)
 return valor

 # las funciones son estructuras de codigos 
 #que se ejecutan mediante su llamado nombre()
 # funcion si es positivo 

def signo(valor):
     valor = True if respuesta < 0 else False
     print (valor)
     return valor


def detectarLetras(valor):
    if any(c.isalpha() for c in str(valor)):
        return True
    else: 
        print(False)
        return False
    
# any() es funcion que trae python
# si hay un elemento es true la funcion nos devolvera 
#true de lo contrario false 
# for c es una variable temporal 
# for dara las vueltas necesarias para termianael el numero 
#segun su caracteres 
#isalfhan nos indica si todos los caracteres son legras o numeros
valor = 4
Modulo(valor) 
signo(valor)

detectarLetras("43")

def ejecutar(): 
    pedirValor = int(input("Ingrese el numero"))
    if pedirValor == True: 
        ejecutar()
    else :
        #valor = True if respuesta < 0 else False 
        Mrespuesta =Modulo(pedirValor)
        #valor = True if respuesta % 2 == 0 else False 
        srespuesta =signo(pedirValor)
        #positivo y par 
    if Mrespuesta and srespuesta == True :
            print ("positivo y par")
    if Mrespuesta and srespuesta == False :
             print ("positivo y impar")
    

    ejecutar()

    # and multi´lica 1 x 1 =1 True 
 

