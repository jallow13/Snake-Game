class Animal:
    def __init__(self):
        self.name = "Animal"
        self.num_ey = 2
    def breathe(self):
        print("breathing")


class Fish(Animal):
    def __init__(self):
        super().__init__()
    def swim(self):
        print("swimming")



fish = Fish()
n=fish.num_ey
print(n)

