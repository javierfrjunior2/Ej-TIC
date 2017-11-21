def suma_cifras():
    suma=0
    numero=input("Dime un numero cualquiera")
    while numero>0:
        suma=suma+numero%10
        numero=numero/10
    print suma+numero
suma_cifras()
    
