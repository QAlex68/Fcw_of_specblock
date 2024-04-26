from pack_animals import PackAnimals
from pets import Pets
from functions import get_valid_date


class DataAnimal(PackAnimals, Pets):
    def __init__(self):
        super().__init__()
        if self.type_animals == "Вьючные животные":
            self.kind_animal = self.choose_pack_type()
        else:
            self.kind_animal = self.choose_pet_type()
        self.name = input("Введите кличку животного: ")
        self.birthday = get_valid_date()
        self.commands = input("Введите команды, которые выполняет животное (через запятую или пробел): ").split(", ")
