init python:

    import random

    class Player:
        def __init__(
            self, name: str, hp: int = 100, attack: int = 25, main_class: str = "Воїн"
        ) -> None:
            """Ініціалізує гравця.
            Args:
                name (str): Ім'я гравця.
                hp (int): Здоров'я гравця. За замовчуванням 100.
                attack (int): Сила атаки гравця. За замовчуванням 25.
                main_class (str): Основний клас гравця. За замовчуванням "Воїн".
            """
            self.name = name
            self.hp = hp
            self.attack = attack
            self.main_class = main_class
            pass

        def __str__(self) -> str:
            """Повертає представлення гравця."""
            return f"Гравець: {self.name}, Классу: {self.main_class}"

default player = None

init python:
    """Класс ворога"""
    class Enemy:
        def __init__(self, hp: int = 100, attack: int = 25, type: str = "Гоблін") -> None:
            """
            Ініціалізує ворога.
            Args:
                hp (int): Здоров'я ворога. За замовчуванням 100.
                attack (int): Сила атаки ворога. За замовчуванням 25.
                type (str): Основний клас ворога. За замовчуванням "Гоблін".
            """

            """Імя Буде використовуватись для спеціальних ворогів, 
            наприклад боссів. 
            Звичайни моби імя не мають"""

            self.name = ""
            self.hp = hp
            self.attack = attack
            self.type = type
            self.enemy_list = ["Гоблін", "Вовк", "Змія"]
            self.enemy_replics = ["Зараз ти помреш!", "Ррр...", "Не твій сьогодні день.."]
            # ворог каже рандомну репліку зі списку
            self.say = self.say_something()
            pass

        def say_something(self):
            self.say = random.choice(self.enemy_replics)
            return self.say

        """Повертає рандомного ворога, з рандомною атакою"""

        def random_enemy(self):
            self.type = random.choice(self.enemy_list)
            self.attack = random.randint(10, 25)
            return self

        def __str__(self) -> str:
            """Повертає представлення ворогу."""
            return f"{self.type}\nHP: {self.hp}\nАттака: {self.attack}"

default enemy = None        