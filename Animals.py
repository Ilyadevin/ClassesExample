class animals:
    fed = "Голодно"
    weight = 0

    def fedding(self):
        print(self.name + " животное сыто")


class goose(animals):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight



goose_grey = goose("Серый", 3)
goose_white = goose("Белый", 3.3)
goose_grey.fedding()
goose_white.fedding()

print(goose_grey.name, goose_grey.weight, "кг.")
print(goose_white.name, goose_white.weight, "кг.")

class weight:
    def __init__(self, weight_grey_goose, weight_goose_white):
       self.weight_goose_white = weight_goose_white
       self.weight_grey_goose = weight_grey_goose
       print(weight_grey_goose + weight_goose_white)


weight(3, 3)