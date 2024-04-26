# Итоговая контрольная работа по блоку специализация (Камаев Александр группа 5275-5276)


## Урок 2. Итоговая контрольная работа

 [< Перейти к коду >](https://github.com/QAlex68/Fcw_of_specblock/tree/main/python)

**Информация о проекте**

* Необходимо организовать систему учета для питомника в котором живут домашние и вьючные животные.

**Как сдавать проект**

Для сдачи проекта необходимо создать отдельный общедоступный репозиторий (Github, Gitlub или Bitbucket).
Разработку вести в этом репозитории, использовать пул реквесты на изменения. Программа должна запускаться и работать,
ошибок при выполнении программы быть не должно. Программа может использоваться в различных системах, поэтому необходимо
разработать класс в виде конструктора.

### Задание

1. Использование команды cat в Linux
   - Создать два текстовых файла: "Pets"(Домашние животные) и "Pack animals"(вьючные животные), используя команду `cat` в терминале Linux.
 В первом файле перечислить собак, кошек и хомяков. Во втором — лошадей, верблюдов и ослов.
   - Объединить содержимое этих двух файлов в один и просмотреть его содержимое.
   - Переименовать получившийся файл в "Human Friends".
Пример конечного вывода после команды “ls” :
Desktop Documents Downloads  HumanFriends.txt  Music  PackAnimals.txt  Pets.txt  Pictures  Videos

<details>
    <summary>Команды PowerShell 7 задача 1 (развернуть)</summary>

```shell
mkdir control_work
cd control_work
ll

cat > Pets.txt
Собаки
Кошки
Хомяки
'Ctrl+d'

cat > PackAnimals.txt
Лошади
Верблюды
Ослы
'Ctrl+d'

cat Pets.txt PackAnimals.txt > Animals.txt
cat Animals.txt
'Ctrl+d' 

mv Animals.txt HumanFriends.txt
ll
```
</details>

![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/01.png)

2. Создать директорию, переместить файл туда.

<details>
    <summary>Команды PowerShell 7 задача 2 (развернуть)</summary>

```shell
mkdir newdir
mv HumanFriends.txt newdir
cd newdir
ll
cd ..
cd ..
rm -r control_work
ll

```
</details>

![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/02.png)

3. Работа с MySQL в Linux. “Установить MySQL на вашу вычислительную машину ”
   - Подключить дополнительный репозиторий MySQL и установить один из пакетов из этого репозитория.

<details>
    <summary>Команды PowerShell 7 задача 3 (развернуть) для установки MySQL</summary>

```shell
wget -c https://dev.mysql.com/doc/refman/8.0/en/checking-gpg-signature.html
sudo apt-key add checking-gpg-signature.html
sudo add-apt-repository 'deb http://repo.mysql.com/apt/ubuntu/ bionic mysql-8.0'
sudo apt update
sudo apt install mysql-server

```
</details>

<details>
    <summary>Команды PowerShell 7 задача 3 (развернуть) у меня уже установлен, проверка статуса MySQL</summary>

```shell
sudo apt update
sudo apt install mysql-server
sudo service mysql status

```
</details>

![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/03.png)


4. Управление deb-пакетами
   - Установить и затем удалить deb-пакет, используя команду `dpkg`.
   
<details>
    <summary>Команды PowerShell 7 задача 3 (развернуть) установка Google Chrome</summary>

```shell
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo dpkg --purge google-chrome-stable

```
</details>

![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/04.png)

5. История команд в терминале Ubuntu
   - Сохранить и выложить историю ваших терминальных команд в Ubuntu.

![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/05.png)

6. Диаграмма классов
   - Создать диаграмму классов с родительским классом "Животные", и двумя подклассами: "Pets" и "Pack animals".
В составы классов которых в случае Pets войдут классы: собаки, кошки, хомяки, а в класс Pack animals войдут: Лошади, верблюды и ослы.
Каждый тип животных будет характеризоваться (например, имена, даты рождения, выполняемые команды и т.д)
Диаграмму можно нарисовать в любом редакторе, такими как Lucidchart, Draw.io, Microsoft Visio и других.

![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/06-diagram.png)

7.  Работа с MySQL (Задача выполняется в случае успешного выполнения задачи “Работа с MySQL в Linux. “Установить MySQL на вашу машину”).
  7.1. После создания диаграммы классов в 6 пункте, в 7 пункте база данных "Human Friends" должна быть структурирована в соответствии с этой диаграммой. Например, можно создать таблицы, которые будут соответствовать классам "Pets" и "Pack animals", и в этих таблицах будут поля, которые характеризуют каждый тип животных (например, имена, даты рождения, выполняемые команды и т.д.).
  7.2. В ранее подключенном MySQL создать базу данных с названием "Human Friends".
   - Создать таблицы, соответствующие иерархии из вашей диаграммы классов.

<details>
    <summary>Команды MySQL задача 7 (развернуть) создание таблиц</summary>

```sql
-- Создаем БД если нету
CREATE DATABASE IF NOT EXISTS human_friends;
USE human_friends;
-- Создание таблиц с иерархией из диаграммы
-- Животные тип
CREATE TABLE IF NOT EXISTS animals
(
	id INT AUTO_INCREMENT PRIMARY KEY,
	animal_type VARCHAR(30)
);
-- Домашние животные
CREATE TABLE IF NOT EXISTS pets
(
	id INT AUTO_INCREMENT PRIMARY KEY,
	animal_kind VARCHAR(30),
	animal_type_id INT DEFAULT 1,
	-- ON DELETE CASCADE ON UPDATE CASCADE - защита целостности связных данных потомков от удаления и изменения
	FOREIGN KEY (animal_type_id) REFERENCES animals (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Вьючные животные
CREATE TABLE IF NOT EXISTS pack_animals
(
	id INT AUTO_INCREMENT PRIMARY KEY,
	animal_kind VARCHAR(30),
	animal_type_id INT DEFAULT 2,
	FOREIGN KEY (animal_type_id) REFERENCES animals (id) ON DELETE CASCADE ON UPDATE CASCADE
);
-- Собаки
CREATE TABLE IF NOT EXISTS dogs 
(       
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(30), 
    commands VARCHAR(150),
    birthday DATE,
    animal_kind_id INT DEFAULT 1,
    Foreign KEY (animal_kind_id) REFERENCES pets (id) ON DELETE CASCADE ON UPDATE CASCADE
);
-- Кошки
CREATE TABLE IF NOT EXISTS cats 
(       
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(30), 
    commands VARCHAR(150),
    birthday DATE,
    animal_kind_id INT DEFAULT 2,
    Foreign KEY (animal_kind_id) REFERENCES pets (id) ON DELETE CASCADE ON UPDATE CASCADE
);
-- Хомяки
CREATE TABLE IF NOT EXISTS hamsters 
(       
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(30), 
    commands VARCHAR(150),
    birthday DATE,
    animal_kind_id INT DEFAULT 3,
    Foreign KEY (animal_kind_id) REFERENCES pets (id) ON DELETE CASCADE ON UPDATE CASCADE
);
-- Лошади
CREATE TABLE IF NOT EXISTS horses 
(       
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(30), 
    commands VARCHAR(150),
    birthday DATE,
    animal_kind_id INT DEFAULT 1,
    Foreign KEY (animal_kind_id) REFERENCES pack_animals (id) ON DELETE CASCADE ON UPDATE CASCADE
);
-- Верблюды 
CREATE TABLE IF NOT EXISTS camels 
(       
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(30), 
    commands VARCHAR(150),
    birthday DATE,
    animal_kind_id INT DEFAULT 2,
    Foreign KEY (animal_kind_id) REFERENCES pack_animals (id) ON DELETE CASCADE ON UPDATE CASCADE
);
-- Ослы
CREATE TABLE IF NOT EXISTS donkeys 
(       
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(30), 
    commands VARCHAR(150),
    birthday DATE,
    animal_kind_id INT DEFAULT 3,
    Foreign KEY (animal_kind_id) REFERENCES pack_animals (id) ON DELETE CASCADE ON UPDATE CASCADE
);

```
</details>

![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/71.png)
![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/73.png)

   - Заполнить таблицы данными о животных, их командах и датами рождения.

<details>
    <summary>Команды MySQL задача 7 (развернуть) заполнение таблиц</summary>

```sql
-- Заполнение баз
INSERT INTO animals (animal_type)
VALUES ('Домашние животные'), ('Вьючные животные');

SELECT * FROM animals;
-- Домашние животные
INSERT INTO pets (animal_kind)
VALUES ('Собаки'), ('Кошки'), ('Хомяки');
-- Вьючные животные
INSERT INTO pack_animals (animal_kind)
VALUES ('Лошади'), ('Верблюды'), ('Ослы');
-- Собаки
INSERT INTO dogs (name, birthday, commands)
VALUES ('Fido', '2020-01-01', 'Sit, Stay, Fetch'),
('Buddy', '2018-12-10', 'Sit, Paw, Bark'),
('Bella', '2019-11-11', 'Sit, Stay, Roll');
-- Кошки
INSERT INTO cats (name, birthday, commands)
VALUES ('Whiskers', '2019-05-15', 'Sit, Pounce'),
('Smudge', '2020-02-20', 'Sit, Pounce, Scratch'),
('Oliver', '2020-06-30', 'Meow, Scratch, Jump');
-- Хомяки
INSERT INTO hamsters (name, birthday, commands)
VALUES ('Hammy', '2021-03-10', 'Roll, Hide'),
('Peanut', '2021-08-01', 'Roll, Spin');
-- Лошади
INSERT INTO horses (name, birthday, commands)
VALUES ('Thunder', '2015-07-21', 'Trot, Canter, Gallop'),
('Storm', '2014-05-05', 'Trot, Canter'),
('Blaze', '2016-02-29', 'Trot, Jump, Gallop');
-- Верблюды
INSERT INTO camels (name, birthday, commands)
VALUES ('Sandy', '2016-11-03', 'Walk, Carry Load'),
('Dune', '2018-12-12', 'Walk, Sit'),
('Sahara', '2015-08-14', 'Walk, Run');
-- Ослы
INSERT INTO donkeys (name, birthday, commands)
VALUES ('Eeyore', '2017-09-18', 'Walk, Carry Load, Bray'),
('Burro', '2019-01-23', 'Walk, Bray, Kick');
-- Проверка заполнения
SELECT * FROM animals;
SELECT * FROM pets;
SELECT * FROM pack_animals;
SELECT * FROM dogs;
SELECT * FROM cats;
SELECT * FROM hamsters;
SELECT * FROM  horses;
SELECT * FROM  camels;
SELECT * FROM  donkeys;

```
</details>

![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/74.png)
![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/75.png)
![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/76.png)
![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/77.png)

   - Удалить записи о верблюдах и объединить таблицы лошадей и ослов.

<details>
    <summary>Команды MySQL задача 7-1 (развернуть) решение</summary>

```sql
-- Удалить записи о верблюдах и объединить таблицы лошадей и ослов.
DELETE FROM camels WHERE animal_kind_id = 2;
SELECT * FROM  camels;

CREATE TABLE IF NOT EXISTS horses_donkeys SELECT * FROM horses
UNION SELECT * FROM donkeys;

SELECT * FROM  horses_donkeys;

```
</details>

![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/78.png)

   - Создать новую таблицу для животных в возрасте от 1 до 3 лет и вычислить их возраст с точностью до месяца.

<details>
    <summary>Команды MySQL задача 7-2 (развернуть) решение</summary>

```sql
-- Создать новую таблицу для животных в возрасте от 1 до 3 лет и вычислить их возраст с точностью до месяца.
CREATE TEMPORARY TABLE all_animals
SELECT * FROM dogs
UNION SELECT * FROM cats
UNION SELECT * FROM hamsters
UNION SELECT * FROM horses
UNION SELECT * FROM camels
UNION SELECT * FROM donkeys;

CREATE TABLE IF NOT EXISTS young_animals
SELECT name, commands, birthday, animal_kind_id, TIMESTAMPDIFF(MONTH, birthday, CURDATE()) AS age_in_month
FROM all_animals
WHERE birthday BETWEEN ADDDATE(CURDATE(), INTERVAL -3 YEAR) AND ADDDATE(CURDATE(), INTERVAL -1 YEAR);

SELECT * FROM  young_animals;

```
</details>

![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/79.png)

   - Объединить все созданные таблицы в одну, сохраняя информацию о принадлежности к исходным таблицам.

<details>
    <summary>Команды MySQL задача 7-3 (развернуть) решение</summary>

```sql
-- Объединить все созданные таблицы в одну, сохраняя информацию о принадлежности к исходным таблицам.
SELECT dogs.name, dogs.commands, dogs.birthday, pets.animal_kind, animals.animal_type
FROM dogs
LEFT JOIN pets ON pets.id = dogs.animal_kind_id
LEFT JOIN animals ON animals.id=pets.animal_type_id
UNION
SELECT cats.name, cats.commands, cats.birthday, pets.animal_kind, animals.animal_type
FROM cats
LEFT JOIN pets ON pets.id = cats.animal_kind_id
LEFT JOIN animals ON animals.id=pets.animal_type_id
UNION
SELECT hamsters.name, hamsters.commands, hamsters.birthday, pets.animal_kind, animals.animal_type
FROM hamsters
LEFT JOIN pets ON pets.id = hamsters.animal_kind_id
LEFT JOIN animals ON animals.id=pets.animal_type_id
UNION
SELECT horses.name, horses.commands, horses.birthday, pack_animals.animal_kind, animals.animal_type
FROM horses
LEFT JOIN pack_animals ON pack_animals.id = horses.animal_kind_id
LEFT JOIN animals ON animals.id=pack_animals.animal_type_id
UNION
SELECT camels.name, camels.commands, camels.birthday, pack_animals.animal_kind, animals.animal_type
FROM camels
LEFT JOIN pack_animals ON pack_animals.id = camels.animal_kind_id
LEFT JOIN animals ON animals.id=pack_animals.animal_type_id
UNION
SELECT donkeys.name, donkeys.commands, donkeys.birthday, pack_animals.animal_kind, animals.animal_type
FROM donkeys
LEFT JOIN pack_animals ON pack_animals.id = donkeys.animal_kind_id
LEFT JOIN animals ON animals.id=pack_animals.animal_type_id;

```
</details>

![pictures for project](https://github.com/QAlex68/Fcw_of_specblock/blob/main/png/791.png)

8. . ООП и Java (можно любой язык)
   - Создать иерархию классов в Java, который будет повторять диаграмму классов созданную в задаче 6(Диаграмма классов).

9. Программа-реестр домашних животных
    - Написать программу на Java, которая будет имитировать реестр домашних животных. 
Должен быть реализован следующий функционал:
    
    9.1. Добавление нового животного
        - Реализовать функциональность для добавления новых животных в реестр.       
 Животное должно определяться в правильный класс (например, "собака", "кошка", "хомяк" и т.д.)
        
 
   9.2. Список команд животного
        - Вывести список команд, которые может выполнять добавленное животное (например, "сидеть", "лежать").
        
  9.3. Обучение новым командам
        - Добавить возможность обучать животных новым командам.

  9.4 Вывести список животных по дате рождения

  9.5. Навигация по меню
        - Реализовать консольный пользовательский интерфейс с меню для навигации между вышеуказанными функциями.

10. Счетчик животных
Создать механизм, который позволяет вывести на экран общее количество созданных животных любого типа (Как домашних, так и вьючных), то есть при создании каждого нового животного счетчик увеличивается на “1”. 


11. , 8. , 9., 10. - [< Перейти к коду >](https://github.com/QAlex68/Fcw_of_specblock/tree/main/python)
