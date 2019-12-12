class animals:

    def __init__(self, name, fed, weight):
        self.name = name
        self.weight = weight
        self.fed = fed
        weight_dict = {}

    def weight_(self, weight_dict=None):
        for key, value in weight_dict:
            key = self.name
            value = self.weight

    def compare_weight(self, other):
        total_weight = int(self.weight) + int(other.weight)
        print('Общий вес животных:', total_weight)
        if self.weight > other.weight:
            print('Больший вес у:', self.name)
        else:
            print('Больший вес у:', other.name)
        return total_weight


class birds(animals):
    def __init__(self, name, fed, weight, eggs):
        super().__init__(name, fed, weight)
        self.fed = fed
        self.eggs = eggs


class gooses(birds):

    def __init__(self, name, fed, weight, eggs):
        super().__init__(name, fed, weight, eggs)

    def data(self):
        description = ("Гусь - " + self.name + " весит: " + str(self.weight) + " кг " + "и его " + self.fed)
        print(description)

    def collected_eggs(self):
        eggs1 = ("Собранные яйца с: " + " гуся " + self.name + " : " + str(self.eggs))
        print(eggs1)

    def say_word(self):
        word = "Га-га"
        print(word)


grey = gooses("Серый", "покормили", 3, 4)
grey.data()
grey.say_word()
grey.collected_eggs()

white = gooses("Белый", "покормили", 2, 5)
white.data()
white.say_word()
white.collected_eggs()


class chicken(birds):

    def __init__(self, name, fed, weight, eggs):
        super().__init__(name, fed, weight, eggs)

    def data(self):
        description = ("Курица - " + self.name + " весит: " + str(self.weight) + " кг " + "и её " + self.fed)
        print(description)

    def collected_eggs(self):
        eggs1 = ("Собранные яйца с: " + ' курицы ' + self.name + " : " + str(self.eggs))
        print(eggs1)

    def say_word(self):
        word = "Ко-ко-ко"
        print(word)


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

    def __init__(self, name, fed, weight, eggs):
        super().__init__(name, fed, weight, eggs)

    def data(self):
        description = ("Утка - " + self.name + " весит: " + str(self.weight) + " кг " + "и его " + self.fed)
        print(description)

    def collected_eggs(self):
        eggs1 = ("Собранные яйца с: " + " утки " + self.name + " : " + str(self.eggs))
        print(eggs1)

    def say_word(self):
        word = "Кря-кря"
        print(word)


duck = ducks("'Кряква'", "покормили", 1, 3)
duck.data()
duck.say_word()
duck.collected_eggs()
print("----------------------------------------------------------------------")

class mimmals(animals):
    def __init__(self, name, fed, weight):
        super().__init__(name, fed, weight)
        self.fed = fed
        self.name = name


class cow_and_goat(mimmals):
    def __index__(self, name, fed, weight):
        super().__init__(self, name, fed)


class cow(cow_and_goat):
    def __init__(self, name, fed, weight, milk):
        super().__init__(name, fed, weight)
        self.milk = milk

    def data_cow(self):
        description = ("Корова - " + self.name + " весит: " + str(self.weight) + " кг " + "и его " + self.fed)
        print(description)

    def get_milk(self):
        milk_1 = ("Собранное молоко с " + " коровы " + self.name + " : " + str(self.milk) + " литров")
        print(milk_1)

    def say_word(self):
        word = "Муу-у"
        print(word)


cow = cow("Манька", "покормили", 400, 16)
cow.data_cow()
cow.say_word()
cow.get_milk()


class goat(cow_and_goat):

    def __init__(self, name, fed, weight, milk):
        super().__init__(name, fed, weight)
        self.milk = milk

    def data_goat(self):
        description = ("Коза - " + self.name + " весит: " + str(self.weight) + " кг " + "и его " + self.fed)
        print(description)

    def get_milk_goat(self):
        milk_1 = ("Собранное молоко с " + " козы " + self.name + " : " + str(self.milk) + " литров")
        print(milk_1)

    def say_word(self):
        word = "Ме-е-е"
        print(word)


goat_horn = goat("Рога", "покормили", 70, 6)
goat_horn.data_goat()
goat_horn.say_word()
goat_horn.get_milk_goat()


goat_hoof = goat("Копыта", "покормили", 60, 4)
goat_hoof.data_goat()
goat_hoof.say_word()
goat_hoof.get_milk_goat()
goat_horn.compare_weight(goat_hoof)
print("----------------------------------------------------------------------")


class sheep(mimmals):
    def __init__(self, name, fed, weight, woof):
        super().__init__(name, fed, weight)
        self.woof = woof

    def data_sheep(self):
        description = ("Овца - " + self.name + " весит: " + str(self.weight) + " кг " + "и его " + self.fed)
        print(description)

    def get_woof_sheep(self):
        milk_1 = ("Собранное шерсти с " + " овцы " + self.name + " : " + str(self.woof) + " литров")
        print(milk_1)

    def say_word(self):
        word = "Ме-е-е"
        print(word)


sheep_sheepy = sheep("Барашек", "покормили", 30, 1)
sheep_sheepy.data_sheep()
sheep_sheepy.get_woof_sheep()
sheep_sheepy.say_word()

sheep_waivy = sheep("Кудрявый", "покормили", 50, 1.5)
sheep_waivy.data_sheep()
sheep_waivy.get_woof_sheep()
sheep_waivy.say_word()
sheep_sheepy.compare_weight(sheep_waivy)

