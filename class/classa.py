class Flower:
    def __init__(self, name, color, petals):
       self.name = name
       self.color = color
       self.petals = petals

    def func(self):
        return self.color
        print(self.name)

yellow = Flower("rose", "pink", "thin")
print(yellow.func())


