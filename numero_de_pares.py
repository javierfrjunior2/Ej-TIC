def numero_de_pares():
    pares=0
    numero=input("Dime cualquier numero")
    while numero>0:
        if (numero%10)%2==0:
            pares=pares+1
        numero=numero/10
    print "El numero tiene",pares,"pares"
numero_de_pares()
