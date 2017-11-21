def ecuacion():
    import math
    a=input("Dame la a")
    b=input("Dame la b")
    c=input("Dame la c")
    a1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
    a2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
    if (b**2-4*a*c)>0:
        print "Tiene dos soluciones", a1, "y", a2 
    if (b**2-4*a*c)<0:
        print "no existe"
    if (b**2-4*a*c)==0:
        print "Tiene una solucion", a1
ecuacion()
