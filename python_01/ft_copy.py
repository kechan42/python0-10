class Plant:
    def __init__(self, name: str, height: float,
                 growth_rate: float, days: int) -> None:
        self.name: str = name
        self.__height: float = height
        self.__days: int = days
        self.growth_rate: float = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.__height}cm,", end='')
        print(f" {self.__days} days old")

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

    @staticmethod
    def year_old(age: int) -> bool:
        if (age > 365):
            return True
        else:
            return False

    @classmethod
    def anon_plant(cls, name: str = "Unknown plant", height: float = "0.0", growth_rate: float = "0.0", days: int = "0"):
        return cls(name, height, growth_rate, days)

    class Stats:
        def __init__(self, name) -> None:
            self.name = name
            self.__grow_c: int = 0
            self.__age_c: int = 0
            self.__show_c: int = 0

        def get_grow_c(self) -> int:
            return self.__grow_c

        def get_age_c(self) -> int:
            return self.__age_c

        def get_show_c(self) -> int:
            return self.__show_c

        def increment_grow_c(self) -> None:
            self.__grow_c += 1

        def increment_age_c(self) -> None:
            self.__age_c += 1

        def increment_show_c(self) -> None:
            self.__show_c += 1


        def display_counts(self) -> None:
            print(f"[Statistics for {self.name}]")
            print(f"Stats: {self.get_grow_c()} grow, ", end='')
            print(f"{self.get_age_c()} count, {self.get_show_c()} show")

class Flower(Plant):
    def __init__(self, name: str, height: float,
        growth_rate: float, days: int, color: str, bloomed: bool) -> None:
        super().__init__(name, height, growth_rate, days)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        if (self._bloomed is False):
            self._bloomed = True

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if (self._bloomed != True):
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")


class Seed(Flower):
    def __init__(self, name: str, height: float,
        growth_rate: float, days: int, color: str, bloomed) -> None:
        super().__init__(name, height,
        growth_rate, days, color, bloomed)
        self.seeds = 0

    def bloom(self):
        super().bloom()
        if (self._bloomed is True):
            self.seeds =  42
        else:
            return (0)

    def show(self):
        super().show()
        print(f" Seeds: {self.seeds}")

class Tree(Plant):
    def __init__(self, name: str, height: float,
                 growth_rate: float, days: int, trunk_diameter: float) -> None:
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

    class Stats(Plant.Stats):
        def __init__(self, name) -> None:
            self.name = name
            self.__grow_c: int = 0
            self.__age_c: int = 0
            self.__show_c: int = 0
            self.__shade_c: int = 0

        def get_shade_c(self) -> int:
            return self.__shade_c

        def increment_shade_c(self) -> None:
            self.__shade_c += 1

        def display_counts(self) -> None:
            print(f"[Statistics for {self.name}]")
            print(f"Stats: {self.get_grow_c()} grow, ", end='')
            print(f"{self.get_age_c()} count, {self.get_show_c()} show,", end='')
            print(f" {self.get_shade_c()} shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 growth_rate: float, days: int, harvest_season: str,
                 nutritional_value: int) -> None:
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

def show_stats(stats):
    stats.display_counts()

print("=== Garden Statistics ===")
print("=== Check year-old ===")
print(f"is 60 days older than a year-> {Plant.year_old(60)}")
print(f"is 500 days older than a year-> {Plant.year_old(500)}")

print("\n=== Flower")
p1 = Flower("Rose", 15, 0.1, 15, "red", False)
p1_s = p1.Stats("Rose")
p1.show()
p1_s.increment_show_c()
show_stats(p1_s)
p1_s.increment_grow_c()
p1.bloom()
p1.grow()
p1.show()
p1_s.increment_show_c()
show_stats(p1_s)

print("\n=== Tree")
p2 = Tree("Oak", 200.0, 0.01, 365, 5.0)
p2_s = p2.Stats("Oak")
p2.show()
p2_s.increment_show_c()
show_stats(p2_s)
p2.produce_shade()
p2_s.increment_shade_c()
show_stats(p2_s)

print("\n=== Seed")
p3 = Seed("Sunflower", 80, 0.1, 45, "yellow", False)
p3_s = p3.Stats("Sunflower")
p3.show()
p3_s.increment_show_c()
p3.bloom()
p3.grow()
p3.age()
p3.show()
p3_s.increment_show_c()
show_stats(p3_s)

print("\n=== Anonymous")
p4 = Plant.anon_plant()
p4.show()
p4_s = p4.Stats("Anonymous")
show_stats(p4_s)
