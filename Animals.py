class animals:

    def __init__(self, name, fed, weight, word):
        self.name = name
        self.weight = weight
        self.fed = fed
        self.weight_dict = {}
        self.word = word

    def weight_(self):
        key = self.name
        value = self.weight
        self.weight_dict[key] = value

    def compare_weight(self, other):
        total_weight = int(self.weight) + int(other.weight)
        print('Общий вес животных:', total_weight)
        if self.weight > other.weight:
            print('Больший вес у:', self.name)
        else:
            print('Больший вес у:', other.name)
        return total_weight

    def say_word(self):
        print(self.word)


class birds(animals):
    def __init__(self, name, fed, weight, eggs, word):
        super().__init__(name, fed, weight, word)
        self.fed = fed
        self.eggs = eggs

    def data(self):
        description = (self.name + " весит: " + str(self.weight) + " кг " + "и его " + self.fed)
        print(description)

    def collected_eggs(self):
        eggs1 = ("Собранные яйца с: " + self.name + " : " + str(self.eggs))
        print(eggs1)


print("----------------------------------------------------------------------")


class gooses(birds):

    def __init__(self, name, fed, weight, eggs, word="Га-га"):
        super().__init__(name, fed, weight, eggs, word)


grey = gooses("Серый", "покормили", 3, 4)
grey.data()
grey.say_word()
grey.collected_eggs()

white = gooses("Белый", "покормили", 2, 5)
white.data()
white.say_word()
white.collected_eggs()
print("----------------------------------------------------------------------")


class chicken(birds):

    def __init__(self, name, fed, weight, eggs, word="Ко-ко-ко"):
        super().__init__(name, fed, weight, eggs, word)


chicken1 = chicken("'Ко-ко'", "покормили", 1, 6)
chicken1.data()
chicken1.say_word()
chicken1.collected_eggs()

chicken2 = chicken("Кукареку", "покормили", 0.8, 7)
chicken2.data()
chicken2.say_word()
chicken2.collected_eggs()
chickens = chicken1 and chicken2
chickens.compare_weight(grey)
print("----------------------------------------------------------------------")


class ducks(birds):

    def __init__(self, name, fed, weight, eggs, word):
        super().__init__(name, fed, weight, eggs, word)


duck = ducks("'Кряква'", "покормили", 1, 3, "Кря-кря")
duck.data()
duck.say_word()
duck.collected_eggs()
print("----------------------------------------------------------------------")


class mimmals(animals):
    def __init__(self, name, fed, weight, word):
        super().__init__(name, fed, weight, word)


class cow_and_goat(mimmals):
    def __index__(self, name, fed, weight, word):
        super().__init__(self, name, fed, word)

    def data_cow_goat(self):
        description = (self.name + " весит: " + str(self.weight) + " кг " + "и его " + self.fed)
        print(description)

    def get_milk(self):
        milk_1 = ("Собранное молоко с " + self.name + " : " + str(self.milk) + " литров")
        print(milk_1)


class cow(cow_and_goat):
    def __init__(self, name, fed, weight, milk, word="Мууу"):
        super().__init__(name, fed, weight, word)
        self.milk = milk


cow = cow("Манька", "покормили", 400, 16)
cow.data_cow_goat()
cow.say_word()
cow.get_milk()
print("----------------------------------------------------------------------")


class goat(cow_and_goat):

    def __init__(self, name, fed, weight, milk, word="Ме-е-е"):
        super().__init__(name, fed, weight, word)
        self.milk = milk


goat_horn = goat("Рога", "покормили", 70, 6)
goat_horn.data_cow_goat()
goat_horn.say_word()
goat_horn.get_milk()


goat_hoof = goat("Копыта", "покормили", 60, 4)
goat_hoof.data_cow_goat()
goat_hoof.say_word()
goat_hoof.get_milk()
goat_horn.compare_weight(goat_hoof)
print("----------------------------------------------------------------------")


class sheep(mimmals):
    def __init__(self, name, fed, weight, woof, word="Ме-е-е"):
        super().__init__(name, fed, weight, word)
        self.woof = woof

    def data_sheep(self):
        description = (self.name + " весит: " + str(self.weight) + " кг " + "и его " + self.fed)
        print(description)

    def get_woof_sheep(self):
        milk_1 = ("Собранное шерсти с " + self.name + " : " + str(self.woof) + " литров")
        print(milk_1)


sheep_sheepy = sheep("Барашек", "покормили", 30, 1)
sheep_sheepy.data_sheep()
sheep_sheepy.get_woof_sheep()
sheep_sheepy.say_word()

sheep_waivy = sheep("Кудрявый", "покормили", 50, 1.5)
sheep_waivy.data_sheep()
sheep_waivy.get_woof_sheep()
sheep_waivy.say_word()
sheep_sheepy.compare_weight(sheep_waivy)
print("----------------------------------------------------------------------")
