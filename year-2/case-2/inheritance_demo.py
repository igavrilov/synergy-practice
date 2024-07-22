class Mammal:
    type: str
    tail: str

    def __init__(self, name: str) -> None:
        self.name = name

    def make_sound(self) -> str:
        raise NotImplementedError()

    def report(self) -> str:
        sound = self.make_sound()
        return f"{self.type.capitalize()} {self.name} говорит \"{sound}\", у неё {self.tail} хвост."


class Dog(Mammal):
    type = "собачка"
    tail = "короткий"

    def make_sound(self):
        return "гав"


class Cat(Mammal):
    type = "кошечка"
    tail = "красивый"

    def make_sound(self):
        return "мяу"


class Mouse(Mammal):
    type = "мышка"
    tail = "длинный"

    def make_sound(self):
        return "и-и-и"


def main():
    dog = Dog("Жучка")
    cat = Cat("Мурка")
    mouse = Mouse("Норушка")
    for mammal in [dog, cat, mouse]:
        print(mammal.report())


if __name__ == "__main__":
    main()
