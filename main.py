import random
import time
from prettytable.colortable import ColorTable, Theme
from colorama import init, Fore, Back, Style

init(autoreset=True)


class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.lvl = 1
        self.exp = 0

    def create_hero(name, rasa, profesion):
        hp = 10
        damage = 10
        name = name
        if rasa == rasa_list[0]:
            hp += 10
            damage += 14
        elif rasa == rasa_list[1]:
            hp += 12
            damage += 13
        elif rasa == rasa_list[2]:
            hp += 13
            damage += 11
        elif rasa == rasa_list[3]:
            hp += 15
            damage += 12
        else:
            print('Я такого не знаю')
            print(exit)
            exit()
        if profesion == profesion_list[0]:
            hp += 35
            damage += 20
        elif profesion == profesion_list[1]:
            hp += 30
            damage += 30
        elif profesion == profesion_list[2]:
            hp += 40
            damage += 15
        elif profesion == profesion_list[3]:
            hp += 35
            damage += 25
        else:
            print('Я такого не знаю')
            print(exit)
            exit()
        return Player(name, hp, damage)

    def attack(self, victim):
        max_exp = self.lvl * 100
        rand = random.choices(crit, weights=[7, 2, 1])
        r = ''.join(rand)
        if r == 'удар':
            victim.hp -= self.damage
        elif r == 'crit':
            v = self.damage + self.damage
            victim.hp -= v
            print(f'{Fore.RED}CRIT X2')
        elif r == 'упс':
            print(f'{Fore.WHITE}упс')
        if victim.hp <= 0:
            self.exp += victim.exp_drop
            print(f'{victim.name} повержен! {Fore.GREEN}+{victim.exp_drop}')
            if self.exp >= max_exp:
                self.lvl_up(max_exp)
            thing = random.randrange(0, 3)
            if thing == 0:  # выпадение оружия
                weapon = Weapon.create_weapon()
                weapon.print_characteristic()
                # print(f'У сэра {hero.name} в данный момент {hero.damage} урона ', end='\n\n')
                wpn_in_inventory = input('Добавить это оружие в инвентарь? (да\нет) ')
                if wpn_in_inventory == 'да':
                    backpack.inventory['оружие'].append(weapon)
                elif wpn_in_inventory == 'нет':
                    print(f'{Fore.RED}ТЕБЕ ЧТО СТАТЫ НЕ ПОНРАВИЛСЬ?!?!?! ')
                else:
                    print(f'{Fore.RED}Будь внимателен (в следующий раз натравлю на тебя хиличурла)')
            elif thing == 1:
                armor = Armor.create_armor()
                armor.print_characteristic()
                arm_in_inventory = input('Добавить эту броню в инвентарь? (да\нет) ')
                if arm_in_inventory == 'да':
                    backpack.inventory['броня'].append(armor)
                elif arm_in_inventory == 'нет':
                    print('Ну и ладно ')
                else:
                    print('Повнимательней ')
            elif thing == 2:
                food = Food.create_food()
                food.print_characteristic()
                food_in_inventory = input('Добавить эту еду в инвентарь? (да\нет) ')
                if food_in_inventory == 'да':
                    backpack.inventory['кушалка'].append(food)
                elif food_in_inventory == 'нет':
                    print(f'{Fore.RED}ну и ладно. ')
                else:
                    print(f'{Fore.RED}Будь внимателен ')
            else:
                print('Вам ничего не выпало')
            return True  # победа(True)

        elif victim.hp > 0:
            print(f'У {victim.name} осталось {Fore.RED}{victim.hp}')
            return False  # недопобеда(False)

    def lvl_up(self, max_exp):
        self.exp -= max_exp
        self.lvl += 1
        self.damage += self.lvl * 2
        self.hp += self.lvl * 4
        print(f'{Fore.GREEN}ПОДНЯТИЕ УРОВНЯ!!! {self.lvl}')
        time.sleep(3)


class Inventory:
    def __init__(self):
        self.inventory = {'оружие': [], 'броня': [], 'кушалка': []}
        self.eqip_wpn = None
        self.eqip_arm = None

    def show_weapon_inventory(self):
        # создание таблиц
        color_theme = Theme(default_color='35', vertical_color='35', horizontal_color='35', junction_color='35')
        wpn_tabl = ColorTable(theme=color_theme)
        # создание списков характеристик
        wpn_type_list, wpn_rare_list, wpn_damage_list = [], [], []
        # заполнение списков хар.
        for weapon in self.inventory['оружие']:
            wpn_type_list.append(weapon.wpn_type)
            wpn_rare_list.append(weapon.wpn_rare)
            wpn_damage_list.append(weapon.damage)
        # заполнение таблиц
        wpn_tabl.add_column('Тип', wpn_type_list)
        wpn_tabl.add_column('Редкость', wpn_rare_list)
        wpn_tabl.add_column('Урон', wpn_damage_list)
        wpn_tabl.add_autoindex('№')
        print('Оружие', wpn_tabl, sep='\n')

    def show_armor_inventory(self):
        color_theme = Theme(default_color='35', vertical_color='35', horizontal_color='35', junction_color='35')
        arm_tabl = ColorTable(theme=color_theme)
        arm_type_list, arm_rare_list, arm_hp_list = [], [], []
        for armor in self.inventory['броня']:
            arm_type_list.append(armor.arm_type)
            arm_rare_list.append(armor.arm_rare)
            arm_hp_list.append(armor.hp)
        arm_tabl.add_column('Тип', arm_type_list)
        arm_tabl.add_column('Редкость', arm_rare_list)
        arm_tabl.add_column('Броня', arm_hp_list)
        arm_tabl.add_autoindex('№')
        print('Броня', arm_tabl, sep='\n')

    def show_food_inventory(self):
        color_theme = Theme(default_color='35', vertical_color='35', horizontal_color='35', junction_color='35')
        food_tabl = ColorTable(theme=color_theme)
        food_type_list, food_rare_list, food_hp_list = [], [], []
        for food in self.inventory['кушалка']:
            food_type_list.append(food.food_type)
            food_rare_list.append(food.food_rare)
            food_hp_list.append(food.hp)
        food_tabl.add_column('Тип', food_type_list)
        food_tabl.add_column('Редкость', food_rare_list)
        food_tabl.add_column('ХП', food_hp_list)
        food_tabl.add_autoindex('№')
        print('Кушалка', food_tabl, sep='\n')

    def change_wpn(self):  # сменя оружия без изменения урона игрока
        wpn_choise = int(input('Введите индекс оружия')) - 1
        while wpn_choise >= len(self.inventory['оружие']):
            print('Ты ввел не правильно, исправляйся!!!')
            wpn_choise = int(input('Введите индекс оружия')) - 1
        else:
            return self.inventory['оружие'][wpn_choise]

    def change_arm(self):  # сменя брони без изменения хп игрока
        arm_choise = int(input('Введите индекс брони')) - 1
        while arm_choise >= len(self.inventory['броня']):
            print('Ты ввел не правильно, исправляйся!!!')
            arm_choise = int(input('Введите индекс брони')) - 1
        else:
            return self.inventory['броня'][arm_choise]

    def change_food(self):
        food_choise = int(input('Введите индекс еды')) - 1
        while food_choise >= len(self.inventory['кушалка']):
            print('Ты ввел не правильно, исправляйся!!!')
            food_choise = int(input('Введите индекс еды')) - 1
        else:
            return food_choise

    def damage_bonus(self):  # изменение урона игрока
        if self.eqip_wpn is None:  # ни разу не было оружия
            self.eqip_wpn = self.change_wpn()
            hero.damage += self.eqip_wpn.damage
            print(f'У вас появилось новое оружие - {self.eqip_wpn.wpn_type}')
        else:  # смена оружия
            old_eqip_wpn = self.eqip_wpn
            new_eqip_wpn = self.change_wpn()
            self.eqip_wpn = new_eqip_wpn
            hero.damage = hero.damage - old_eqip_wpn.damage + new_eqip_wpn.damage
            print(f'Вы поменяли оружие на {self.eqip_wpn.wpn_type}')

    def hp_bonus(self):
        if self.eqip_arm is None:
            self.eqip_arm = self.change_arm()
            hero.hp += self.eqip_arm.hp
            print(f'Вы надели свои первые доспехи - {self.eqip_arm.arm_type}')
        else:  # смена брони
            old_eqip_arm = self.eqip_arm
            new_eqip_arm = self.change_arm()
            self.eqip_arm = new_eqip_arm
            hero.hp = hero.hp - old_eqip_arm.hp + new_eqip_arm.hp
            print(f'Вы поменяли свою броню на - {self.eqip_arm.arm_type}')

    def food_hp_bonus(self):
        food_index = self.change_food()
        create_food = self.inventory['кушалка'][food_index]
        hero.hp += create_food.hp
        print(f"Вы съели - {self.inventory['кушалка'][food_index].food_type}")
        del self.inventory['кушалка'][food_index]

    def choose_item(self):
        # открываем инвент если хотяб бы в 1-ом списке что то есть
        if len(self.inventory['оружие']) > 0 or len(self.inventory['броня']) > 0 or len(self.inventory['кушалка']) > 0:
            answer = input('Хочешь ли ты открыть инвентарь? (да\нет)')
            if answer == 'да':
                if len(self.inventory['оружие']) > 0 and len(self.inventory['броня']) > 0 and len(
                        self.inventory['кушалка']) > 0:
                    self.show_weapon_inventory()
                    self.show_armor_inventory()
                    self.show_food_inventory()
                    wpn_answer = input('Хочешь ли ты взять\поменять оружие? (да\нет)')
                    arm_answer = input('Хочешь ли ты одеть\поменять броню? (да\нет)')
                    food_answer = input('Хочешь ли ты покушать? (да\нет)')
                    if wpn_answer == 'да' and arm_answer == 'да' and food_answer == 'да':
                        self.damage_bonus()
                        self.hp_bonus()
                        self.food_hp_bonus()
                    elif wpn_answer == 'да' and arm_answer == 'нет' and food_answer == 'нет':
                        self.damage_bonus()
                    elif wpn_answer == 'нет' and arm_answer == 'да' and food_answer == 'нет':
                        self.hp_bonus()
                    elif wpn_answer == 'нет' and arm_answer == 'нет' and food_answer == 'да':
                        self.food_hp_bonus()
                    elif wpn_answer == 'да' and arm_answer == 'да' and food_answer == 'нет':
                        self.damage_bonus()
                        self.hp_bonus()
                    elif wpn_answer == 'да' and arm_answer == 'нет' and food_answer == 'да':
                        self.damage_bonus()
                        self.food_hp_bonus()
                    elif wpn_answer == 'нет' and arm_answer == 'да' and food_answer == 'да':
                        self.hp_bonus()
                        self.food_hp_bonus()

                elif len(self.inventory['оружие']) > 0 and len(self.inventory['броня']) > 0:
                    self.show_weapon_inventory()
                    self.show_armor_inventory()
                    wpn_answer = input('Хочешь ли ты взять\поменять оружие? (да\нет)')
                    arm_answer = input('Хочешь ли ты одеть\поменять броню? (да\нет)')
                    if wpn_answer == 'да' and arm_answer == 'да':
                        self.damage_bonus()
                        self.hp_bonus()

                elif len(self.inventory['оружие']) > 0 and len(self.inventory['кушалка']) > 0:
                    self.show_weapon_inventory()
                    self.show_food_inventory()
                    wpn_answer = input('Хочешь ли ты взять\поменять оружие? (да\нет)')
                    food_answer = input('Хочешь ли ты поесть? (да\нет)')
                    if wpn_answer == 'да' and food_answer == 'да':
                        self.damage_bonus()
                        self.food_hp_bonus()

                elif len(self.inventory['броня']) > 0 and len(self.inventory['кушалка']) > 0:
                    self.show_armor_inventory()
                    self.show_food_inventory()
                    arm_answer = input('Хочешь ли ты одеть\поменять броню? (да\нет)')
                    food_answer = input('Хочешь ли ты поесть? (да\нет)')
                    if arm_answer == 'да' and food_answer == 'да':
                        self.hp_bonus()
                        self.food_hp_bonus()

                elif len(self.inventory['оружие']) > 0:
                    self.show_weapon_inventory()
                    wpn_answer = input('Хочешь ли ты взять\поменять оружие? (да\нет)')
                    if wpn_answer == 'да':
                        self.damage_bonus()
                elif len(self.inventory['броня']) > 0:
                    self.show_armor_inventory()
                    arm_answer = input('Хочешь ли ты одеть\поменять броню? (да\нет)')
                    if arm_answer == 'да':
                        self.hp_bonus()
                elif len(self.inventory['кушалка']) > 0:
                    self.show_food_inventory()
                    food_answer = input('Хочешь ли ты поесть? (да\нет)')
                    if food_answer == 'да':
                        self.food_hp_bonus()


class Weapon:  # оружие
    def __init__(self, wpn_type, wpn_rare, damage):
        self.wpn_type = wpn_type
        self.wpn_rare = wpn_rare
        self.damage = damage

    def create_weapon():
        damage = 0
        wpn_type = weapon_name[random.randrange(0, 3)]
        wpn_rare = random.choices(list(rare.keys()), weights=[4, 3, 2, 1])
        if wpn_rare[0] == 1:
            damage += 20
        elif wpn_rare[0] == 2:
            damage += 33
        elif wpn_rare[0] == 3:
            damage += 46
        elif wpn_rare[0] == 4:
            damage += 60
        return Weapon(wpn_type, rare[wpn_rare[0]], damage)

    def print_characteristic(self):
        print(f'Вам выпало новое оружие: {self.wpn_type} - {self.wpn_rare} - {Fore.BLUE}{self.damage}')


class Armor:
    def __init__(self, arm_type, arm_rare, hp):
        self.arm_type = arm_type
        self.arm_rare = arm_rare
        self.hp = hp

    def create_armor():
        hp = 0
        arm_type = armor_type_list[random.randrange(0, 3)]
        arm_rare = random.choices(list(rare.keys()), weights=[4, 3, 2, 1])
        if arm_rare[0] == 1:
            hp += 20
        elif arm_rare[0] == 2:
            hp += 33
        elif arm_rare[0] == 3:
            hp += 46
        elif arm_rare[0] == 4:
            hp += 60
        return Armor(arm_type, rare[arm_rare[0]], hp)

    def print_characteristic(self):
        print(f'Вам выпала новая броня: {self.arm_type} - {self.arm_rare} - {Fore.RED}{self.hp}')


class Food:
    def __init__(self, food_type, food_rare, hp):
        self.food_type = food_type
        self.food_rare = food_rare
        self.hp = hp

    def create_food():
        hp = 0
        food_type = food_type_list[random.randrange(0, 3)]
        food_rare = random.choices(list(rare.keys()), weights=[4, 3, 2, 1])
        if food_rare[0] == 1:
            hp += 20
        elif food_rare[0] == 2:
            hp += 33
        elif food_rare[0] == 3:
            hp += 46
        elif food_rare[0] == 4:
            hp += 60
        return Food(food_type, rare[food_rare[0]], hp)

    def print_characteristic(self):
        print(f'Вам выпала новая еда: {self.food_type} - {self.food_rare} - {Fore.RED}{self.hp}')


class Enemy:
    def __init__(self, name, hp, damage, exp_drop):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.exp_drop = exp_drop

    def create_enemy():
        rnd_name = random.choice(enemy_name)
        if rnd_name == enemy_name[0]:
            hp_enemy = 50
            exp_drop = 20
        elif rnd_name == enemy_name[1]:
            hp_enemy = 30
            exp_drop = 10
        elif rnd_name == enemy_name[2]:
            hp_enemy = 80
            exp_drop = 30
        damage_enemy = random.randrange(20, 50)
        return Enemy(rnd_name, hp_enemy, damage_enemy, exp_drop)

    def enemy_attack(self, hero):
        hero.hp -= self.damage
        if hero.hp <= 0:
            print('Ты повержен!!!')
            print(exit)
            exit()
        elif hero.hp > 0:
            print(f'У тебя осталось {Fore.RED}{hero.hp}')


def fight_choice(enemy):
    a = input('Хочешь  сражаться? (да\нет) ')
    backpack.choose_item()
    if a == 'да':
        result = hero.attack(enemy)
        if not result:
            enemy.enemy_attack(hero)
            fight_choice(enemy)
    elif a == 'нет':
        ran = random.randint(0, 1)
        if ran == 0:
            print('Побег не удался :(')
            time.sleep(3)
            enemy.enemy_attack(hero)
            fight_choice(enemy)
        elif ran == 1:
            print('Вы сбежали')
            time.sleep(2)
    else:
        print(f'{Fore.RED}ТАК, будь внимателен!!!')
        time.sleep(2)
        fight_choice(enemy)


def open_choice():  # сундук
    a = input('Хочешь  открыть? (да\нет) ')
    b = random.randint(1, 5)
    if a == 'да' and b <= 4:
        c = random.randint(1, 3)
        if c == 1:
            weapon = Weapon.create_weapon()
            weapon.print_characteristic()
            wpn_in_inventory = input('Добавить это оружие в инвентарь? (да\нет) ')
            if wpn_in_inventory == 'да':
                backpack.inventory['оружие'].append(weapon)
            elif wpn_in_inventory == 'нет':
                print(f'{Fore.RED}ТЕБЕ ЧТО СТАТЫ НЕ ПОНРАВИЛСЬ?!?!?! ')
            else:
                print(f'{Fore.RED}Будь внимателен (в следующий раз натравлю на тебя хиличурла)')
        elif c == 2:
            armor = Armor.create_armor()
            armor.print_characteristic()
            arm_in_inventory = input('Добавить эту броню в инвентарь? (да\нет) ')
            if arm_in_inventory == 'да':
                backpack.inventory['броня'].append(armor)
            elif arm_in_inventory == 'нет':
                print(f'{Fore.WHITE}Ну и ладно ')
            else:
                print(f'{Fore.RED}Повнимательней ')
        else:
            food = Food.create_food()
            food.print_characteristic()
            food_in_inventory = input('Добавить эту броню в инвентарь? (да\нет) ')
            if food_in_inventory == 'да':
                backpack.inventory['кушалка'].append(food)
            elif food_in_inventory == 'нет':
                print(f'{Fore.WHITE}Ну и ладно ')
            else:
                print(f'{Fore.RED}Повнимательней ')

    elif a == 'да' and b == 5:
        print(f'{Fore.RED}НЕПОВЕЗЛО:(')
        hero.hp -= 5
        print(f'У сэра {Fore.CYAN}{hero.name} {Fore.RESET}осталось {Fore.RED}{hero.hp} {Fore.RESET}хп')
    else:
        print(f'{Fore.RED}Вы упустили свое счастье!!!')
        time.sleep(2)


crit = ['удар', 'crit', 'упс']
weapon_name = ['Меч', 'Лук', 'Книгу']
rare = {1: f'{Fore.WHITE}Обычный', 2: f'{Fore.BLUE}Редкий', 3: f'{Fore.MAGENTA}Эпический',
        4: f'{Fore.YELLOW}Легендарный'}
armor_type_list = ['Шлем', 'Нагрудник', 'Ботинки']
food_type_list = ['Искушение Адепта', 'Креветочные печенья сакуры', 'Мондштадтские оладушки']
rasa_list = ['эльф', 'гном', 'гоблин', 'дворф']
profesion_list = ['лучник', 'бард', 'воин', 'волшебник']
enemy_name = ['Слайм', 'Крыса', 'Хиличурл']
name_hero = input('Введите имя: ')
my_rasa = input(f'Выберите расу: {rasa_list} ').lower()
my_profesion = input(f'Выберите профессию: {profesion_list} ').lower()
hero = Player.create_hero(name_hero, my_rasa, my_profesion)
backpack = Inventory()
while True:
    opa = random.randint(2, 3)
    if opa == 1:
        print('Вы никого не нашли(радуйтесь)')
        time.sleep(2)
    elif opa == 2:
        enemy = Enemy.create_enemy()
        print(f'Тебе встретился {Fore.RED}{enemy.name}')
        print(f'хп {Fore.RED}{enemy.hp}{Fore.RESET}, урон {Fore.BLUE}{enemy.damage}')
        print(
            f'У сэра {Fore.CYAN}{hero.name} {Fore.RESET}осталось {Fore.RED}{hero.hp} {Fore.RESET}хп и {Fore.BLUE}{hero.damage} {Fore.RESET}урона ')
        fight_choice(enemy)
    else:
        print(f'Вы нашли {Fore.YELLOW}сундук')
        open_choice()
