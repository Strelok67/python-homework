# ==========================================
# ЗАДАНИЯ: ЦИКЛ FOR
# ==========================================

# 1. Выведите все числа от 1 до 10.
print("Задание 1 (for):")
for i in range(1, 11):
    print(i, end=" ")
print("\n" + "-"*20)

# 2. Выведите все чётные числа от 2 до 50.
print("Задание 2 (for):")
for i in range(2, 51, 2):
    print(i, end=" ")
print("\n" + "-"*20)

# 3. Выведите числа от 10 до 1 в порядке убывания.
print("Задание 3 (for):")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n" + "-"*20)

# 4. Дано число n. Найдите сумму всех чисел от 1 до n.
print("Задание 4 (for):")
n = int(input("Введите число n: "))
summa = 0
for i in range(1, n + 1):
    summa += i
print(f"Сумма от 1 до {n} = {summa}")
print("-"*20)

# 5. Дано число n. Найдите его факториал.
print("Задание 5 (for):")
n = int(input("Введите число n: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")
print("-"*20)

# 6. Дано число n. Выведите таблицу умножения на n от 1 до 10.
print("Задание 6 (for):")
n = int(input("Введите число n: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
print("-"*20)

# 7. Дан список чисел. Посчитайте, сколько в нём положительных чисел.
print("Задание 7 (for):")
numbers = [5, -2, 10, 0, -7, 3, 8]
positive_count = 0
for num in numbers:
    if num > 0:
        positive_count += 1
print(f"Список: {numbers}. Положительных чисел: {positive_count}")
print("-"*20)

# 8. Дана строка. Посчитайте, сколько в ней гласных букв.
print("Задание 8 (for):")
text = "Привет, как дела?"
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"Строка: '{text}'. Гласных букв: {count}")
print("-"*20)

# 9. Дан список чисел. Найдите наибольший элемент, не используя max().
print("Задание 9 (for):")
numbers = [4, 12, 7, 25, 9, 3]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Список: {numbers}. Максимальный элемент: {max_num}")
print("-"*20)

# 10. Выведите таблицу умножения от 1 до 9 в виде квадрата.
print("Задание 10 (for):")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:2}", end=" ")
    print()

print("\n\n" + "="*40 + "\n\n")


# ==========================================
# ЗАДАНИЯ: ЦИКЛ WHILE
# ==========================================

# 1. Выведите все числа от 1 до 10 с помощью while.
print("Задание 1 (while):")
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print("\n" + "-"*20)

# 2. Вводите числа, пока не будет введён 0. Выведите сумму введённых чисел.
print("Задание 2 (while):")
total_sum = 0
while True:
    num = int(input("Введите число (0 для выхода): "))
    if num == 0:
        break
    total_sum += num
print(f"Сумма: {total_sum}")
print("-"*20)

# 3. Дано натуральное число. Посчитайте количество его цифр.
print("Задание 3 (while):")
n = int(input("Введите натуральное число: "))
count = 0
temp_n = n
while temp_n > 0:
    temp_n //= 10
    count += 1
print(f"Количество цифр в {n}: {count}")
print("-"*20)

# 4. Дано натуральное число. Найдите сумму его цифр.
print("Задание 4 (while):")
n = int(input("Введите натуральное число: "))
sum_digits = 0
temp_n = n
while temp_n > 0:
    sum_digits += temp_n % 10
    temp_n //= 10
print(f"Сумма цифр числа {n}: {sum_digits}")
print("-"*20)

# 5. Дано натуральное число. Выведите его цифры в обратном порядке одним числом.
print("Задание 5 (while):")
n = int(input("Введите натуральное число: "))
reversed_n = 0
temp_n = n
while temp_n > 0:
    digit = temp_n % 10
    reversed_n = reversed_n * 10 + digit
    temp_n //= 10
print(f"Число наоборот: {reversed_n}")
print("-"*20)

# 6. Дано число n. Выведите все степени двойки, не превышающие n.
print("Задание 6 (while):")
n = int(input("Введите число n: "))
power = 1
while power <= n:
    print(power, end=" ")
    power *= 2
print("\n" + "-"*20)

# 7. Запрашивайте пароль, пока пользователь не введёт правильный.
print("Задание 7 (while):")
password = "12345"
while True:
    user_input = input("Введите пароль: ")
    if user_input == password:
        print("Доступ разрешен!")
        break
    else:
        print("Неверный пароль, попробуйте снова.")
print("-"*20)

# 8. Даны два натуральных числа. Найдите их наибольший общий делитель.
print("Задание 8 (while):")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
while b != 0:
    a, b = b, a % b
print(f"НОД: {a}")
print("-"*20)

# 9. Дано число n. Выведите все числа Фибоначчи, не превышающие n.
print("Задание 9 (while):")
n = int(input("Введите число n: "))
a, b = 0, 1
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
print("\n" + "-"*20)

# 10. Программа загадывает число от 1 до 100. Пользователь угадывает...
print("Задание 10 (while):")
import random
secret_number = random.randint(1, 100)
attempts = 0
print("Я загадал число от 1 до 100.")
while True:
    guess = int(input("Ваш вариант: "))
    attempts += 1
    if guess < secret_number:
        print("Больше")
    elif guess > secret_number:
        print("Меньше")
    else:
        print(f"Угадал! Количество попыток: {attempts}")
        break

print("\n\n" + "="*40 + "\n\n")


# ==========================================
# ЗАДАНИЯ: СЛОВАРИ
# ==========================================

# 1. Создайте словарь из трёх учеников и их оценок.
print("Задание 1 (словари):")
students = {"Иван": 5, "Мария": 4, "Петр": 3}
print(f"Оценка Марии: {students['Мария']}")
print("-"*20)

# 2. Дан словарь. Добавьте новую пару, измените значение, удалите ключ.
print("Задание 2 (словари):")
d = {"a": 1, "b": 2}
d["c"] = 3
d["a"] = 10
del d["b"]
print(d)
print("-"*20)

# 3. Дан словарь и ключ. Выведите значение, а если нет - "Нет такого ключа".
print("Задание 3 (словари):")
d = {"name": "Alice", "age": 20}
key = "name"
if key in d:
    print(d[key])
else:
    print("Нет такого ключа")
print("-"*20)

# 4. Дан словарь. Выведите отдельно все ключи, все значения и количество пар.
print("Задание 4 (словари):")
d = {"a": 1, "b": 2, "c": 3}
print(f"Ключи: {list(d.keys())}")
print(f"Значения: {list(d.values())}")
print(f"Количество пар: {len(d)}")
print("-"*20)

# 5. Дан словарь товаров и цен. Выведите каждый товар и цену с новой строки.
print("Задание 5 (словари):")
products = {"Хлеб": 50, "Молоко": 80, "Сыр": 300}
for item, price in products.items():
    print(f"{item}: {price} руб.")
print("-"*20)

# 6. Найти сумму всех цен и название самого дорогого товара.
print("Задание 6 (словари):")
products = {"Хлеб": 50, "Молоко": 80, "Сыр": 300}
total_price = sum(products.values())
most_expensive = max(products, key=products.get)
print(f"Общая сумма: {total_price}")
print(f"Самый дорогой товар: {most_expensive}")
print("-"*20)

# 7. Дана строка. Посчитайте, сколько раз встречается каждый символ.
print("Задание 7 (словари):")
text = "hello world"
char_counts = {}
for char in text:
    char_counts[char] = char_counts.get(char, 0) + 1
print(char_counts)
print("-"*20)

# 8. Дана строка из слов. Посчитайте, сколько раз встречается каждое слово, и выведите самое частое.
print("Задание 8 (словари):")
text = "яблоко банан яблоко апельсин банан яблоко"
words = text.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
most_frequent = max(word_counts, key=word_counts.get)
print(f"Слова: {word_counts}")
print(f"Самое частое слово: '{most_frequent}'")
print("-"*20)

# 9. Дан словарь. Создайте новый словарь, в котором ключи и значения поменяны местами.
print("Задание 9 (словари):")
d = {"a": 1, "b": 2, "c": 3}
reversed_dict = {value: key for key, value in d.items()}
print(reversed_dict)
print("-"*20)

# 10. Даны два списка одинаковой длины: страны и их столицы.
print("Задание 10 (словари):")
countries = ["Россия", "Франция", "Япония"]
capitals = ["Москва", "Париж", "Токио"]
country_capitals = dict(zip(countries, capitals))
user_country = input("Введите страну: ")
if user_country in country_capitals:
    print(f"Столица: {country_capitals[user_country]}")
else:
    print("Страна не найдена")