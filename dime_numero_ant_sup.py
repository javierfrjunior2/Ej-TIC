def dime_numero_ant_post():
    numero=input("Dime un n�mero")
    for cont in range(numero-3,numero,1):
        print cont,
    for cont in range(numero+1,numero+4,1):
        print cont,
dime_numero_ant_post()        
