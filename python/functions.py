import csv
import os
from datetime import datetime


def get_valid_date():  # Проверка ввода даты на верный формат
    while True:
        date_str = input("Введите дату рождения (гггг-мм-дд): ")
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("Неправильный формат даты. Попробуйте еще раз.")


def print_all_animals(file_name):  # Вывод списка животных на консоль
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                print(
                    f"ID: {row[0]}, Тип: {row[1]}, Вид: {row[2]}, "
                    f"Кличка: {row[3]}, Дата рождения: {row[4]}, Выполняет команды: {row[5]}")
                print("-" * 120)
    else:
        print("Реестр пуст, сначала добавьте животных!")


def search_animal_by_id(file_name, note_id):  # Проверка существования животного с заданным ID
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[0] == note_id:
                    print(
                        f"ID: {row[0]}, Тип: {row[1]}, Вид: {row[2]}, "
                        f"Кличка: {row[3]}, Дата рождения: {row[4]}, Выполняет команды: {row[5]}")
                    print("-" * 120)
                    return True

            print(f"Животного с ID {note_id} не существует!")
            return False
    else:
        print("Реестр пуст, сначала добавьте животных!")
        return False


def delete_animal(file_name):  # Удаление записи
    animal_id = input("Введите ID животного для удаления: ")
    if not search_animal_by_id(file_name, animal_id):
        return
    temp_file_path = 'temp_registry.csv'
    with open(file_name, 'r', newline='', encoding='utf-8') as file, \
            open(temp_file_path, 'w', newline='', encoding='utf-8') as temp_file:
        reader = csv.reader(file, delimiter=';')
        writer = csv.writer(temp_file, delimiter=';')
        for row in reader:
            if row[0] != animal_id:
                writer.writerow(row)
    os.remove(file_name)
    os.rename(temp_file_path, file_name)
    print(f"Заметка с ID {animal_id} удалена!")


def add_new_commands(file_name):  # Редактирование поля команды
    animal_id = input("Введите ID животного для обучения: ")
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
                commands = input("Введите новый список команд (через запятую или пробел): ")
                row[5] = commands
            writer.writerow(row)
    os.remove(file_name)  # Заменяем исходный файл временным
    os.rename(temp_file_name, file_name)
    print(f"Список команд животного с ID {animal_id} отредактирован!")


def generate_unique_id(file_name):  # Генерация уникального ID
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        return 1
    else:
        with open(file_name, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            existing_ids = set(row[0] for row in reader)
            new_id = max(map(int, existing_ids)) + 1
    return new_id


def sort_animals_by_birthday(file_name):  # Сортировка по дате рождения
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            data = list(reader)
            sorted_data = sorted(data, key=lambda x: x[4])
            for row in sorted_data:
                print(
                    f"ID: {row[0]}, Тип: {row[1]}, Вид: {row[2]}, "
                    f"Кличка: {row[3]}, Дата рождения: {row[4]}, Выполняет команды: {row[5]}")
                print("-" * 120)
    else:
        print("Реестр пуст, сначала добавьте животных!")


def write_to_file(animal, filename):  # Запись нового животного в файл
    unique_id = generate_unique_id(filename)
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            [unique_id, animal.type_animals, animal.kind_animal, animal.name, animal.birthday,
             ", ".join(animal.commands)])
