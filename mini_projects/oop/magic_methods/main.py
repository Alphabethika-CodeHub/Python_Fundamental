class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Operator Overloading Untuk + """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Operator Overloading Untuk - """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Operator Overloading Untuk * """
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        """Representasi String Untuk Debugging"""
        return f"Vector({self.x}, {self.y})"

    def __len__(self):
        """Mengembalikan 'panjang' Vector (Hanya Contoh)"""
        return 2

    def __getitem__(self, item):
        if item == 0 or item == 'x':
            return self.x
        elif item == 1 or item == 'y':
            return self.y
        else:
            raise IndexError("Indeks Vector Hanya 0/x Atau 1/y")

# Penggunaan
v1 = Vector(2,4)
v2 = Vector(1,3)

print(v1 + v2)
print(v1 - v2)
# print(v1 * v2)
print(v1 * 3)
print(len(v1))
print(v1[0], v1[1])
# print(v1[0], v1[1], v1[2])


