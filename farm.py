class animals:

    def __init__(self, fed, weight):
        self.weight = weight
        self.fed = fed


class birds(animals):
    def __init__(self, name, fed, weight, eggs):
        super().__init__(fed, weight)
        self.fed = fed
        self.eggs = eggs
        self.name = name


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


class mimmals(animals):
    def __init__(self, name, fed, weight):
        super().__init__(fed, weight)
        self.fed = fed
        self.name = name


class cow_and_goat(mimmals):
    def __index__(self, name, fed, weight, milk):
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


goat_roga = goat("Рога", "покормили", 70, 6)
goat_roga.data_goat()
goat_roga.say_word()
goat_roga.get_milk_goat()

goat_koputa = goat("Копыта", "покормили", 60, 4)
goat_koputa.data_goat()
goat_koputa.say_word()
goat_koputa.get_milk_goat()


class sheep(mimmals):
    def __init__(self, name, fed, weight, wool):
        super().__init__(name, fed, weight)
        self.wool = wool

    def data_sheep(self):
        description = ("Овцы - " + self.name + " весит: " + str(self.weight) + " кг " + "и его " + self.fed)
        print(description)

    def wool_getting(self):
        milk_1 = ("Собранная шерсть " + " козы " + self.name + " : " + str(self.wool) + " литров")
        print(milk_1)

    def say_word(self):
        word = "Ме-е-е"
        print(word)


sheep1 = ("Барашек", "покормили", 90, 5)
sheep1.data_sheep()
sheep1.wool_getting()
sheep1.say_word()

sheep2 = ("Кудрявый", "покормили", 84, 5)
sheep2.data_sheep()
sheep2.wool_getting()
sheep2.say_word()