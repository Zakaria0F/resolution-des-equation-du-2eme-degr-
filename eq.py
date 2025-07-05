import math
print("ax**2+bx+c")
print("entrer valeur de a , 'an doit etre differente de 0' ")

try:
    a = int(input())
    if a == 0:
        print("Error: 'a' cannot be zero.")
    else:
        print("entrer valeur de b ")
        b= int(input())
        print ("entrer la valeur de c")
        c= int(input())
        delta=b*b-4*a*c
        if delta <0 :
            print ("l'equation n'a pas de solution")
        elif delta==0:
            print ("la solution est : ")
            print (  -b/(2*a))
        elif delta > 0:
            print (" la premier solution est")
            print ((-b - math.sqrt(delta))/(2*a) )
            print (" la deuxieme solution est")
            print ((-b + math.sqrt(delta))/(2*a))
except ValueError:
    print("Invalid input. Please enter integer values for a, b, and c.")