import random
import time
from model.cellule import Cellule
class Grille:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.grille = [[Cellule(x, y) for x in range(largeur)] for y in range(hauteur)]
        self.state = self.grille.copy()

    def getCellule(self, x, y):
        return self.grille[y][x]
    
    def setCellule(self, x, y, cellule):
        self.grille[y][x] = cellule

    def generateWithUserInput(self, inputString):
        lines = inputString.split("/")
        for y in range(self.hauteur):
            for x in range(self.largeur):
                self.grille[y][x].etat = int(lines[y][x])
        
    def generateRandom(self, numberOfAliveCells=None):
        if numberOfAliveCells is None:
            numberOfAliveCells = self.largeur * self.hauteur // 2

        for _ in range(numberOfAliveCells):
            x = random.randint(0, self.largeur - 1)
            y = random.randint(0, self.hauteur - 1)
            while self.grille[y][x].etat == 1:
                x = random.randint(0, self.largeur - 1)
                y = random.randint(0, self.hauteur - 1)
            self.grille[y][x].etat = 1
        self.state = self.grille.copy()

    def getNumberOfAliveNeighbours(self, x, y):
        aliveNeighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x + i < 0 or x + i >= self.largeur or y + j < 0 or y + j >= self.hauteur:
                    continue
                if self.state[y + j][x + i].etat == 1:
                    aliveNeighbours += 1
        return aliveNeighbours

    
    def setNextLife(self):
        for y in range(self.hauteur):
            for x in range(self.largeur):
                aliveNeighbours = self.getNumberOfAliveNeighbours(x, y)
                if self.state[y][x].etat == 1 and (aliveNeighbours == 2 or aliveNeighbours == 3):
                    self.grille[y][x].etat = 1
                elif self.state[y][x].etat == 0 and aliveNeighbours == 3:
                    self.grille[y][x].etat = 1
                else:
                    self.grille[y][x].etat = 0
        self.state = self.grille.copy()

    def display(self):
        for y in range(self.hauteur):
            for x in range(self.largeur):
                if self.grille[y][x].etat == 1:
                    print("1", end="")
                else:
                    print("0", end="")
            print()
    