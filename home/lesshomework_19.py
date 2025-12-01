class Hero:
    def __init__(self, name, role, hp, damage):
        self.name = name
        self.role = role
        self.hp = hp
        self.damage = damage

    def get_info(self):
        return f'имя персонажа {self.name} здарове {self.hp} уорн{self.damage} {self.role}'

class Mage(Hero):
    def __init__(self, name, hp, damage, mana):
        super().__init__(name, hp, damage)
        self.mana = mana

    def get_info(self):
        return f'имя персонажа {self.name} здарове {self.hp} уорн{self.damage} мана {self.mana}'
class Marksman(Hero):
    def __init__(self, name, hp, damage, attak_speed):
        super().__init__(name, hp, damage)
        self.attak_speed = attak_speed
    def get_info(self):
        return f'имя персонажа {self.name} здарове {self.hp} уорн{self.damage} {self.attak_speed}'

class Tank(Hero):
    def __init__(self, name, hp, damage, armor):
        super().__init__(name, hp, damage)
        self.armor = armor
    def get_info(self):
        return f'имя персонажа {self.name} здарове {self.hp} уорн{self.damage} {self.armor}'


class Support(Hero):
    def __init__(self, name, hp, damage, heal_power):
        super().__init__(name, hp, damage)
        self.heal_power = heal_power

    def get_info(self):
        return  f'имя персонажа {self.name} здарове {self.hp} уорн{self.damage} {self.heal_power}'


h1 = Mage("Eudora", 2400, 500, 800)
h2 = Marksman("Layla", 2800, 650, 1.2)
h3 = Tank("Tigreal", 5000, 300, 450)
h4 = Support("Rafaela", 2700, 200, 600)


print(h1.get_info())
print(h2.get_info())
print(h3.get_info())
print(h4.get_info())



#
#
# class Hero:
#     def __init__(self, name, role, hp, damage):
#         self.name = name
#         self.role = role
#         self.hp = hp
#         self.damage = damage
#
#     def get_info(self):
#         return f'Имя персонажа: {self.name}, Здоровье: {self.hp}, Урон: {self.damage}, Роль: {self.role}'
#
#
# class Mage(Hero):
#     def __init__(self, name, hp, damage, mana):
#         super().__init__(name, "Mage", hp, damage)
#         self.mana = mana
#
#     def get_info(self):
#         return f'Имя персонажа: {self.name}, Здоровье: {self.hp}, Урон: {self.damage}, Мана: {self.mana}'
#
#
# class Marksman(Hero):
#     def __init__(self, name, hp, damage, attack_speed):
#         super().__init__(name, "Marksman", hp, damage)
#         self.attack_speed = attack_speed
#
#     def get_info(self):
#         return f'Имя персонажа: {self.name}, Здоровье: {self.hp}, Урон: {self.damage}, Скорость атаки: {self.attack_speed}'
#
#
# class Tank(Hero):
#     def __init__(self, name, hp, damage, armor):
#         super().__init__(name, "Tank", hp, damage)
#         self.armor = armor
#
#     def get_info(self):
#         return f'Имя персонажа: {self.name}, Здоровье: {self.hp}, Урон: {self.damage}, Броня: {self.armor}'
#
#
# class Support(Hero):
#     def __init__(self, name, hp, damage, heal_power):
#         super().__init__(name, "Support", hp, damage)
#         self.heal_power = heal_power
#
#     def get_info(self):
#         return f'Имя персонажа: {self.name}, Здоровье: {self.hp}, Урон: {self.damage}, Сила лечения: {self.heal_power}'
#
#
# # Объекты
# h1 = Mage("Eudora", 2400, 500, 800)
# h2 = Marksman("Layla", 2800, 650, 1.2)
# h3 = Tank("Tigreal", 5000, 300, 450)
# h4 = Support("Rafaela", 2700, 200, 600)
#
# # Вывод информации
# print(h1.get_info())
# print(h2.get_info())
# print(h3.get_info())
# print(h4.get_info())
