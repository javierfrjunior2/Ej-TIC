def triangulo_rec():
    x=input("Dime un lado")
    y=input("Dime otro lado")
    z=input("Dime otro lado")
    if ((x*x)+(y*y)==(z*z)) or ((y*y)+(z*z)==(x*x)) or ((x*x)+(z*z)==(y*y)):
        print "Es un triangulo rectangulo"
    else:
        print "No es un triángulo rectangulo"
triangulo_rec()
