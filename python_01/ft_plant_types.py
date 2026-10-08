class Plant:
    def __init__(self, name:str, height:float, growth_rate:float, days:int) -> None:
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
        return self.__days


class Flower(Plant):
    def __init__(self, name: str, height: float, growth_rate: float, days: int, color: str) -> None:
        super().__init__(name, height, growth_rate, days)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        if (self.bloomed == False):
            self.bloomed = True
            self.show()
            print(f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")

class Tree(Plant):
    def __init__(self, name: str, height:float, growth_rate: float, days: int, trunk_diameter: float) -> None:
        super().__init__(name, height, growth_rate, days)
        self.trunk_diameter = trunk_diameter

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        x = super().get_height()
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of", end='')
        print(f" {x}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, growth_rate:float, days:int, harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, growth_rate, days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def cycle(self, duration):
        pre_height = super().get_height()
        pre_age = super().get_age()
        print(f"[make {self.name} grow and age for {duration} days]")
        super().set_height(pre_height + self.growth_rate * duration)
        super().set_age(pre_age + duration)
        self.nutritional_value += duration
        self.show()


print("=== Garden Plant Types ===")
print("=== Flower")
p1 = Flower("Rose", 15, 0.1, 15, "red")
p1.show()
print("Rose has not bloomed yet")
p1.bloom()
print("\n=== Tree")
p2 = Tree("Oak", 200.0, 0.01, 365, 5.0)
p2.show()
p2.produce_shade()
print("\n=== Vegetable")
p3 = Vegetable("Tomato", 5.0, 0.5, 10, "April", 0)
p3.show()
p3.cycle(20)



