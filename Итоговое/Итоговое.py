if __name__ == "__main__":
    # Write your solution here
    pass

class Guitar:
    """Базовый класс гитары"""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name!r})'

    def __str__(self):
        return f'Гитара"{self.name}"'


class Eguitar(Guitar):
    """Электрогитара"""

    def __init__(self, name: str, sound_pickup: str = "Хамбакер"):
        super().__init__(name)
        self.sound_pickup = sound_pickup

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.sound_pickup!r})'

    def __str__(self):
        return f'Электрогитара"{self.name}"'


class Classguitar(Guitar):
    """Классическая гитара"""

    def __init__(self, name: str, resonator: str = "Резонаторное отверстие"):
        super().__init__(name)
        self.resonator = resonator

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.resonator!r})'

    def __str__(self):
        return f'Классическая гитара"{self.name}"'