import random

print(" Devine le nombre entre 0 et 20")
x = random.randint(0, 20)
essais = 0

try:
    n = int(input(" Entre un nombre : "))
    while n != x:
        essais += 1
        if n < x:
            print("(Trop petit, essaie un nombre plus grand")
        elif n > x:
            print(" Trop grand, essaie un nombre plus petit")
        n = int(input("Essaye encore : "))

    essais += 1 
    print(f" Félicitations ,Tu as trouvé le nombre {x} en {essais} essais.")

except ValueError:
    print(" Erreur , entrer un nombre entre 0 et 20.")