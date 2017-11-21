def contador_vocales():
    palabra=raw_input("Dime una palabra corazon")
    sumaa=0
    sumae=0
    sumai=0
    sumao=0
    sumau=0
    for cont in range (0,len(palabra),1):
        if palabra[cont]=="a":
            sumaa=sumaa+1
        if palabra[cont]=="e":
            sumae=sumae+1
        if palabra[cont]=="i":
            sumai=sumai+1
        if palabra[cont]=="o":
            sumao=sumao+1
        if palabra[cont]=="u":
            sumau=sumau+1
    print " En la palabra ",palabra," hay ",sumaa," aes "
    print " En la palabra ",palabra," hay ",sumae," ees "
    print " En la palabra ",palabra," hay ",sumai," ies "
    print " En la palabra ",palabra," hay ",sumao," oes "
    print " En la palabra ",palabra," hay ",sumau," ues "
contador_vocales()
        
        



