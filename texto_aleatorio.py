def texto_aleatorio():
    texto=raw_input("Dime cualquier cosa")
    todo="a"or"e"or"i"or"o"or"u"    
    for cont in range(0,len(texto),1):
        if texto[cont]==todo:
                print texto       
texto_aleatorio()                   
