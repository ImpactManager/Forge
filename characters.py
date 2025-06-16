"Класс гравця"
import random
class Player:
    def __init__(self, name: str, hp: int = 100, attack: int = 5, main_class: str = "warrior") -> None:
        
        """Ініціалізує гравця.
        Args:
            name (str): Ім'я гравця.
            hp (int): Здоров'я гравця. За замовчуванням 100.
            attack (int): Сила атаки гравця. За замовчуванням 5.
            main_class (str): Основний клас гравця. За замовчуванням "warrior".
        """
        self.name = name
        self.hp = hp
        self.attack = attack
        self.main_class = main_class
        pass
    
    def __str__(self) -> str:
        """Повертає представлення гравця."""
        return f"Гравець: {self.name}, Классу: {self.main_class}"

"Класс ворога"
class Enemy(Player):
    def __init__(self, hp: int = 100, attack: int = 5, type: str = "goblin") -> None:
        
        """
            Ініціалізує ворога.
            Args:
                hp (int): Здоров'я ворога. За замовчуванням 100.
                attack (int): Сила атаки ворога. За замовчуванням 5.
                type (str): Основний клас ворога. За замовчуванням "goblin".
        """
        self.name = "ворог"
        self.hp = hp
        self.attack = attack
        self.type = type
        self.enemy_list = ["Гоблін", "Вовк", "Змія"]
        pass
    
    def random(self):
         self.type = random.choice(self.enemy_list)
         self.attack = random.randint(1,5)
         return self
    def __str__(self) -> str:
        """Повертає представлення ворогу."""
        return f"Тип: {self.type}, Аттака: {self.attack} HP: {self.hp}"
    
