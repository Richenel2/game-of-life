from model.grille import Grille
import time
print("Start Game")
print("\n")
print("-" * 20)
grille = Grille(5, 5)
grille.generateRandom()
grille.display()
print("-" * 20)
i = int(input("Enter the number of iterations: "))
for _ in range(i):
    grille.setNextLife()
    grille.display()
    print("-" * 20)
    time.sleep(1)