
class Player:

    def __init__(self, cakes):
        "constructor"

    def firstmove(self, cakes):
        return cakes > 2 and cakes % 4 != 2

    def move(self, cakes, last):
        return 3 if cakes % 4 < 3 else 1
