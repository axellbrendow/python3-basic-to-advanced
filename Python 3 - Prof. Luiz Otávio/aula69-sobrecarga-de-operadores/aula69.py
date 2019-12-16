class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"

    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y

        return Retangulo(novo_x, novo_y)

    def __lt__(self, other):
        a1 = self.area()
        a2 = other.area()

        return a1 < a2

    def __gt__(self, other):
        a1 = self.area()
        a2 = other.area()

        return a1 > a2

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1 + r2

print(r3)
print(r3 > r1)
print(r3 < r1)
print(r3 == r1)
print(r2 == r1)
