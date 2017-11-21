def suma(num1,num2):
    resp=num1+num2
    return resp
def resta(num1,num2):
    resp1=num1-num2
    return resp1
def multiplicacion(num1,num2):
    resp2=num1*num2
    return resp2
def division(num1,num2):
    resp3=num1/num2
    return resp3

def menu_operacion():
    seguir="si"
    num1=input("Dime un numero")
    num2=input("Dime otro numero")
    while (seguir=="si"):
        print "Que deseas hacer con los números"
        print "1.Sumarlos"
        print "2.Restarlos"
        print "3.Multiplicarlos"
        print "4.Dividirlos"
        respuesta=input()
        if (respuesta==1):
            suma(num1,num2)
        if (respuesta==2):
            resta(num1,num2)
        if (respuesta==3):
            multiplicacion(num1,num2)
        if (respuesta==4):
            division(num1,num2)
        
        
menu_operacion()
