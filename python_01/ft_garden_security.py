class Plant:
    def __init__(self, name: str, height: float, growth_rate: float, days: int) -> None:
        self.name: str = name
        self.__height: float = height
        self.__days: int = days
        self.growth_rate: float = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.__height, 3)}cm, {self.__days} days old")

    def age(self) -> None:
        self.__days += 1

    def grow(self) -> None:
        self.__height += self.growth_rate

    def cycle(self, duration) -> None:
        i: int = 1
        while (i <= duration):
            print(f'=== Day {i} ===')
            self.age()
            self.grow()
            self.show()
            i += 1
        total_growth: float = self.growth_rate * duration
        print(f"Growth this week: {round(total_growth, 3)}cm")

    def set_height(self, new_height: float):
        if (new_height >= 0):
            self.__height = new_height
            print(f"Height updated: {self.__height}cm")
        else:
            print(f"{self.name}: Error: height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int):
        if (new_age >= 0):
            self.__days = new_age
            print(f"Age updated: {self.__days}cm")
        else:
            print(f"{self.name}: Error: age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age


print("=== Garden Security System")
p1 = Plant("Rose", 25, 0.8, 30)
print("Created: ", end='')
p1.show()
print()

p1.set_height(42)
p1.set_age(42)
print()

p1.set_height(-42)
p1.set_age(-42)
print()

print("Current state: ", end='')
p1.show()
