from model.grille import Grille
import time

print("Start Game")
print("\n")
print("-" * 20)

grille = Grille(5,5)
print("Enter the generation: ")
print("Example: 11100/10100/01000/00000/00000")
print("1 for alive cell and 0 for dead cell")
print("Leave empty to generate a random generation")
print("Enter a number to generate a random generation with that number of alive cells")
gen = input()
if gen.isnumeric() or gen == "":
    grille.generateRandom(int(gen))
else:
    grille.generateWithUserInput(gen)
grille.display()

print("-" * 20)
i = int(input("Enter the number of iterations: "))

for _ in range(i):
    grille.setNextLife()
    grille.display()
    print("-" * 20)
    time.sleep(1)