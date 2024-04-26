import csv
import os
from counter import Counter
from data_animal import DataAnimal
from functions import (search_animal_by_id, print_all_animals, write_to_file, add_new_commands,
                       sort_animals_by_birthday, delete_animal)


def user_action(animal_registry, number_of_animals):  # Главное меню
    while True:
        print(
            f'\nРеестр животных приветствует  Вас!! (всего животных в реестре - {number_of_animals}!)\n1 - Просмотр '
            f'всех | 2 - Добавить | 3 - Редактировать | 4 - Удалить | 5 - Обучить новым командам | 6 - Список по '
            f'ДР | 0 - Выйти из приложения\n')
        user_choice = input('Введите команду: ')
        if user_choice == '1':
            print_all_animals(animal_registry)
        elif user_choice == '2':
            add_animal(animal_registry)
            number_of_animals = number_of_animals + 1
        elif user_choice == '3':
            edit_animal(animal_registry)
        elif user_choice == '4':
            delete_animal(animal_registry)
            number_of_animals = number_of_animals - 1
        elif user_choice == '5':
            add_new_commands(animal_registry)
        elif user_choice == '6':
            sort_animals_by_birthday(animal_registry)
        elif user_choice == '0':
            print('Гуд бай!')
            break
        else:
            print('Некорректный выбор действия! Повторите!')
            print()
            continue


def add_animal(file_name):  # Добавление записи
    new_animal = DataAnimal()
    write_to_file(new_animal, file_name)


def edit_animal(file_name):  # Редактирование записи
    animal_id = input("Введите ID животного для редактирования: ")
    if not search_animal_by_id(file_name, animal_id):
        return
    temp_file_name = 'temp_registry.csv'
    print(f"Введите новые данные для записи {animal_id}!")
    with open(file_name, 'r', newline='', encoding='utf-8') as file, \
            open(temp_file_name, 'w', newline='', encoding='utf-8') as temp_file:
        reader = csv.reader(file, delimiter=';')
        writer = csv.writer(temp_file, delimiter=';')
        for row in reader:
            if row[0] == animal_id:
                animal = DataAnimal()
                row[1] = animal.type_animals
                row[2] = animal.kind_animal
                row[3] = animal.name
                row[4] = animal.birthday
                row[5] = ", ".join(animal.commands)
            writer.writerow(row)
    os.remove(file_name)  # Заменяем исходный файл временным
    os.rename(temp_file_name, file_name)
    print(f"Запись с ID {animal_id} отредактирована!")


if __name__ == "__main__":
    filename = 'registry.csv'
    counter = Counter(filename)
    num_rows = counter.count_rows()
    user_action(filename, num_rows)
