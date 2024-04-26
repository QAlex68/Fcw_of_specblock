from animals import Animals


class PackAnimals(Animals):
    def __init__(self):
        super().__init__()
        self.type_pack = None

    def choose_pack_type(self):
        while True:
            choose = input("Выберите вид животного ('1 - Лошади', '2 - Верблюды', '3 - Ослы'): ")
            if choose in ["1", "2", "3"]:
                if choose == "1":
                    self.type_pack = "Лошади"
                elif choose == "2":
                    self.type_pack = "Верблюды"
                else:
                    self.type_pack = "Ослы"
                return self.type_pack
            else:
                print("Повторите выбор - '1 - Лошади', '2 - Верблюды', '3 - Ослы'")
