import time
import random

# --- БАЗА ДАННЫХ ИГРЫ (СЛОВАРИ И КОРТЕЖИ) ---

# Словарь артефактов и предметов: ключ - название, значение - описание
ITEMS_DB = {
    "болты": "Обычные железные болты. Кидаются в аномалии, чтобы проверить путь.",
    "аптечка": "Стандартная армейская аптечка. Восстанавливает здоровье.",
    "артефакт 'Медуза'": "Радиоактивный артефакт. Воняет болотом, но ценится у торговцев.",
    "артефакт 'Каменный цветок'": "Защищает от пуль. Тяжелый, но полезный.",
    "ПМ": "Пистолет Макарова. Надежный друг сталкера."
}

# Кортеж с начальными характеристиками игрока (Имя, Здоровье)
PLAYER_STATS = ("Новичок", 100)

# Словарь с координатами локаций (для вида)
LOCATIONS_COORDS = {
    "Кордон": (100, 200),
    "Свалка": (150, 300)
}


# --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---

def print_slow(text):
    """Печатает текст медленно для атмосферы"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()


def show_inventory(inventory):
    """Выводит текущий рюкзак (список)"""
    if not inventory:
        print("Ваш рюкзак пуст.")
    else:
        print(f"В рюкзаке: {', '.join(inventory)}")


def check_health(health):
    """Проверяет здоровье игрока"""
    if health <= 0:
        print_slow("Вы потеряли сознание... Зона забрала еще одного сталкера.")
        return False
    return True


# --- УРОВЕНЬ 1: КОРДОН ---

def level_1(player_name, inventory, health):
    print("\n" + "=" * 40)
    print_slow(f"ЛОКАЦИЯ 1: КОРДОН. (Координаты: {LOCATIONS_COORDS['Кордон']})")
    print("=" * 40)
    print_slow(f"Привет, {player_name}. Ты очнулся у костра на Кордоне.")
    print_slow("Твоя задача - добраться до Свалки. Но путь преграждает аномалия и слепой пес.")
    print_slow("Осмотрись и найди, чем можно защититься.")

    # Множество для отслеживания выполненных задач
    tasks_done = set()

    while True:
        print("\nДействия: осмотреться | взять [предмет] | рюкзак | кинуть болт | атаковать пса | идти на Свалку")
        command = input("\nВведите команду: ").lower().strip()

        if command == "осмотреться":
            if "болты" not in inventory:
                print_slow("Вы видите: валяется мешок с болтами, рядом лежит аптечка. Впереди аномалия.")
            else:
                print_slow("Вы видите: аномалия впереди. Пес рычит из кустов.")

        elif command.startswith("взять "):
            item = command.split(" ", 1)[1]
            if item == "болты" and "болты" not in inventory:
                inventory.append("болты")
                print_slow("Вы взяли болты. Теперь можно проверить аномалию.")
            elif item == "аптечка" and "аптечка" not in inventory:
                inventory.append("аптечка")
                print_slow("Вы взяли аптечку.")
            else:
                print("Здесь нет такого предмета или вы его уже взяли.")

        elif command == "рюкзак":
            show_inventory(inventory)

        elif command == "кинуть болт":
            if "болты" in inventory:
                print_slow("Вы кинули болт. Аномалия 'Электра' вспыхнула и разрядилась! Путь свободен.")
                tasks_done.add("аномалия_обезврежена")
            else:
                print_slow("У вас нет болтов! Без них вы рискуете попасть в аномалию.")

        elif command == "атаковать пса":
            if "ПМ" in inventory:
                print_slow("Вы выстрелили из ПМ. Слепой пес с визгом убежал!")
                tasks_done.add("пес_побежден")
            else:
                print_slow("У вас нет оружия! Пес укусил вас!")
                health -= 30
                print(f"Ваше здоровье: {health}")
                if not check_health(health):
                    return None  # Игра проиграна

        elif command == "идти на свалку":
            if "аномалия_обезврежена" in tasks_done and "пес_побежден" in tasks_done:
                print_slow("Вы успешно миновали Кордон и идете дальше...")
                break
            else:
                print_slow("Нельзя идти дальше! Сначала разберитесь с аномалией и псом.")

        else:
            print("Я не понимаю эту команду.")

    return health


# --- УРОВЕНЬ 2: СВАЛКА ---

def level_2(player_name, inventory, health):
    print("\n" + "=" * 40)
    print_slow(f"ЛОКАЦИЯ 2: СВАЛКА. (Координаты: {LOCATIONS_COORDS['Свалка']})")
    print("=" * 40)
    print_slow("Вы на Свалке. Здесь куча металлолома и бродячие собаки.")
    print_slow("Впереди бункер, но вход завален. Рядом сидит раненый сталкер.")
    print_slow("Он просит помочь, обещая взамен кое-что ценное.")

    while True:
        print("\nДействия: осмотреться | рюкзак | помочь сталкеру | использовать аптечку | войти в бункер")
        command = input("\nВведите команду: ").lower().strip()

        if command == "осмотреться":
            if "артефакт 'Медуза'" not in inventory:
                print_slow("Вы видите: раненого сталкера, кучу хлама. Кажется, в хламе что-то блестит.")
            else:
                print_slow("Вы видите: раненого сталкера, бункер.")

        elif command == "рюкзак":
            show_inventory(inventory)

        elif command == "помочь сталкеру":
            if "артефакт 'Медуза'" not in inventory:
                print_slow("Вы перевязали сталкера. В благодарность он отдал вам артефакт 'Медуза'!")
                inventory.append("артефакт 'Медуза'")
            else:
                print_slow("Сталкер уже в порядке. Он говорит, что в бункере есть хороший хабар.")

        elif command == "использовать аптечку":
            if "аптечка" in inventory:
                print_slow("Вы использовали аптечку. Здоровье восстановлено!")
                health = 100
                inventory.remove("аптечка")
                print(f"Ваше здоровье: {health}")
            else:
                print_slow("У вас нет аптечки.")

        elif command == "войти в бункер":
            if "артефакт 'Медуза'" in inventory:
                print_slow("Вы продали артефакт торговцу на Свалке за хорошие деньги и купили снаряжение.")
                print_slow(f"Поздравляю, {player_name}! Вы успешно закрепились на Свалке. Игра пройдена!")
                return True
            else:
                print_slow("Торговец не пускает вас в бункер без артефакта или денег. Сначала помогите сталкеру.")

        else:
            print("Я не понимаю эту команду.")


# --- ГЛАВНАЯ ФУНКЦИЯ ЗАПУСКА ---

def main():
    print_slow("Добро пожаловать в Зону Отчуждения, сталкер!")
    player_name = input("Введите ваше имя (позывной): ")

    # Создаем список (рюкзак)
    inventory = ["ПМ"]  # У сталкера изначально есть пистолет
    health = PLAYER_STATS[1]  # Берем здоровье из кортежа

    print_slow(f"Итак, {player_name}, ваше приключение начинается...")
    print_slow(f"Ваш начальный инвентарь: {', '.join(inventory)}")

    # Запуск уровней
    health_after_lvl1 = level_1(player_name, inventory, health)

    if health_after_lvl1 is not None:
        victory = level_2(player_name, inventory, health_after_lvl1)
        if victory:
            print_slow("\nУдачной охоты, сталкер! (Игра завершена)")
    else:
        print_slow("\nGAME OVER")


# Точка входа в программу
if __name__ == "__main__":
    main()