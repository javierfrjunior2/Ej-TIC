def contador_vocales():
    palabra=raw_input("Dime una palabra corazon")
    suma=[0,0,0,0,0]
    for cont in range (0,len(palabra),1):
        if palabra[cont]=="a":
            suma[0]=suma[0]+1
        if palabra[cont]=="e":
            suma[1]=suma[1]+1
        if palabra[cont]=="i":
            suma[2]=suma[2]+1
        if palabra[cont]=="o":
            suma[3]=suma[3]+1
        if palabra[cont]=="u":
            suma[4]=suma[4]+1
    print " En la palabra ",palabra," hay ",suma[0]," aes "
    print " En la palabra ",palabra," hay ",suma[1]," ees "
    print " En la palabra ",palabra," hay ",suma[2]," ies "
    print " En la palabra ",palabra," hay ",suma[3]," oes "
    print " En la palabra ",palabra," hay ",suma[4]," ues "
contador_vocales()
