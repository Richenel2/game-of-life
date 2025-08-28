class Cellule:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.etat = 0
    def __str__(self):
        return "O" if self.etat == 1 else "X"
    def __repr__(self):
        return "O" if self.etat == 1 else "X"