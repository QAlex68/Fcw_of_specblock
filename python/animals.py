class Animals:
    def __init__(self):
        self.type_animals = self.choose_animal_type()

    def choose_animal_type(self):
        while True:
            choose = input("Выберите тип животного ('1 - Вьючные животные' или '2 - Домашние животные'): ")
            if choose in ["1", "2"]:
                if choose == "1":
                    animal_type = "Вьючные животные"
                else:
                    animal_type = "Домашние животные"
                return animal_type
            else:
                print("Повторите выбор - '1 - Вьючные животные' или '2 - Домашние животные'")
