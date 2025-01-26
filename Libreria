from math import atan2, cos, sin, sqrt


def multiplicacionC(a,b):
    parteReal = (a[0]*b[0])- (a[1]*b[1])
    parteImaginaria = (a[0]*b[1])+(a[1]*b[0])
    return (parteReal, parteImaginaria)

def sumaC(a,b):
    parteReal = a[0]+b[0]
    parteImaginaria = a[1]+b[1]
    return (parteReal, parteImaginaria)

def divisionC(a,b):
    parteReal = ((a[0]*b[0]) + (a[1]*b[1])) / ((b[0]**2)+(b[1]**2))
    parteImaginaria = ((b[0] * a[1]) - (a[0] * b[1])) / ((b[0] ** 2) + (b[1] ** 2))
    return (parteReal, parteImaginaria)

def moduloC(a,b):
    return sqrt((a**2) + (b**2))

def conjugadoC(a,b):
    return (a,b*-1)

def polaresC(a,b):
    p=moduloC(a,b)
    fase=atan2(b,a)
    return(p,fase)

def cartesianasC(a,b):
    x=a*cos(b)
    y=a*sin(b)
    return(x,y)

def prettyPrintingC(a):
    if a[1]>0:
        print(round(a[0],3),"+",round(a[1],3),"i")
    else:
        print(round(a[0],3),round(a[1],3),"i")


def main():
    prettyPrintingC(multiplicacionC((4,2),(1,0)))
    print(moduloC(3,4))
    prettyPrintingC(polaresC(2,0))
    prettyPrintingC(cartesianasC(4.472,0.464))
main()
