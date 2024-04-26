from animals import Animals


class Pets(Animals):
    def __init__(self):
        super().__init__()
        self.type_pets = None

    def choose_pet_type(self):
        while True:
            choose = input("Выберите тип животного ('1 - Собаки', '2 - Кошки' или '3 - Хомяки'): ")
            if choose in ["1", "2", "3"]:
                if choose == "1":
                    self.type_pack = "Собаки"
                elif choose == "2":
                    self.type_pack = "Кошки"
                else:
                    self.type_pack = "Хомяки"
                return self.type_pack
            else:
                print("Повторите выбор - '1 - Собаки', '2 - Кошки', '3 - Хомяки'")
