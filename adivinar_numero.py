# Adivinar_el_numero.
import random
print("+------------------------------------+")
print("|---------ADIVINA-EL NUMERO----------|")
print("+------------------------------------+\n")

#input
n = int(input("Adivina un número del 1 al 50: "))

#process
rand = random.randint(1,50)

while n != rand:
    if n < rand:
        print("Fallaste, intenta ingresar un número más grande")  
    else:
        print("Fallaste, intenta ingresar un número más pequeño")  
         
    print("")
    n = int(input("Vuelva a ingresar un número del 1 al 50: "))
else:
    print("")
    print("Acertaste, el número es correcto")