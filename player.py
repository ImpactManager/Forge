"класс гравця" 
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