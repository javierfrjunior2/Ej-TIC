def numeros():
    primero=input("Dime un numero")
    segundo=input("Dimero otro numero")
    if (primero%2==0 and segundo%2==0):
        print ("Ambos números son pares")
    if (primero%2!=0 and segundo%2!=0):
        print ("Ambos números son impares")
    if ((primero%2!=0 and segundo%2==0) or (primero%2==0 and segundo%2!=0)):
        print ("Uno es par y el otro es impar")
numeros()
  
    
