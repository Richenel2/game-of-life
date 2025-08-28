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

    def generateRandom(self):
        for y in range(self.hauteur):
            for x in range(self.largeur):
                self.grille[y][x].etat = random.randint(0, 1)
    
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
                if self.state[y][x].etat == 1 and (aliveNeighbours < 2 or aliveNeighbours > 3):
                    self.grille[y][x].etat = 0
                elif self.state[y][x].etat == 0 and aliveNeighbours == 3:
                    self.grille[y][x].etat = 1
                else:
                    self.grille[y][x].etat = 0
        self.state = self.grille.copy()
    def display(self):
        for y in range(self.hauteur):
            for x in range(self.largeur):
                if self.grille[y][x].etat == 1:
                    print("O", end="")
                else:
                    print("X", end="")
            print()
        