class Cellule:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.etat = 0
    def __str__(self):
        return "1" if self.etat == 1 else "0"
    def __repr__(self):
        return "1" if self.etat == 1 else "0"