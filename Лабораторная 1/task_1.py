import doctest


class Guitar:
    def __init__(self, string_quantity: int, neck_length: float):
        """
        Создание и подготовка к работе объекта "Гитара"
        :param string_quantity: Количество струн
        :param neck_length: Длина рифа
        Пример:
        >>> guitar = Guitar(6, 12)  # инициализация экземпляра класса
        """
        if not isinstance(string_quantity, int):
            raise TypeError("Количество струн должно быть типа int")
        if string_quantity < 0:
            raise ValueError("Количество струн должно быть положительным числом")
        self.string_quantity = string_quantity

        if not isinstance(neck_length, (int, float)):
            raise TypeError("Длина грифа должна быть типа int или float")
        if neck_length < 0:
            raise ValueError("Длина грифа не может быть отрицательным числом")
        self.neck_length = neck_length

    def is_empty_string(self) -> bool:
        """
        Функция, которая проверяет, есть ли струны на гитаре

        """
        ...

    def add_string_to_guitar(self, string: int) -> None:

        if not isinstance(string, (int, float)):
            raise TypeError("Добавляемые струны должны быть типа int")
        if string < 0:
            raise ValueError("Добавляемые струны должны быть положительным числом")
        ...


class Concrete:
    def __init__(self, concrete_strength: float, sand_fraction: float):
        """
        Создание и подготовка к работе объекта "Бетон"
        :param concrete_strength: Прочность бетона
        :param sand_fraction: Фракция песка
        Пример:
        >>> concrete = Concrete(50, 5)  # инициализация экземпляра класса
        """
        if not isinstance(concrete_strength, (int, float)):
            raise TypeError("Прочность бетона должна быть типа int или float")
        if concrete_strength < 0:
            raise ValueError("Прочность бетона должна быть положительным числом")
        self.concrete_strength = concrete_strength

        if not isinstance(sand_fraction, (int, float)):
            raise TypeError("Фракция песка должна быть типа int или float")
        if sand_fraction < 0:
            raise ValueError("Фракция песка не может быть отрицательным числом")
        self.sand_fraction = sand_fraction

    def is_empty_sand(self) -> bool:
        """
        Функция, которая проверяет, есть ли песок в бетону

        """
        ...

    def add_sand_to_concrete(self, sand: float) -> None:

        if not isinstance(sand, (int, float)):
            raise TypeError("Добавляемый песок должны быть типа int или float")
        if sand < 0:
            raise ValueError("Добавляемый песок должен быть положительным числом")
        ...

class Students_group:
    def __init__(self, student_quantity: int, student_age: int):
        """
        Создание и подготовка к работе объекта "Бетон"
        :param student_quantity: Количество студентов
        :param student_age: Средний возраст студентов
        Пример:
        >>> student = Students_group(6, 12)  # инициализация экземпляра класса
        """
        if not isinstance(student_quantity, (int, float)):
            raise TypeError("Количество студентов должно быть типа int")
        if student_quantity < 0:
            raise ValueError("Количество студентов должно быть положительным числом")
        self.student_quantity = student_quantity

        if not isinstance(student_age, int):
            raise TypeError("Возраст студентов должен быть типа int")
        if student_age < 7:
            raise ValueError("Возраст студентов не должен быть меньше 7")
        self.student_age = student_age

    def is_empty_student(self) -> bool:
        """
        Функция, которая проверяет, есть ли студенты

        """
        ...

    def add_student_to_group(self, student: float) -> None:

        if not isinstance(student, int):
            raise TypeError("Добавляемыt студенты должны быть типа int")
        if student < 0:
            raise ValueError("Добавляемые студенты должны быть положительным числом")
        ...

if __name__ == "__main__":
    doctest.testmod()