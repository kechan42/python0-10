class Plant:
    def __init__(self, name:str, height:float, growth_rate:float, days:int) -> None:
        self.name: str = name
        self.__height: float = height
        self.__days: int = days
        self.growth_rate: float = growth_rate

    class Stats:
        def __init__(self, grow_c: int, age_c: int, show_c: int) -> None:
            self.__grow_c: int = 0
            self.__age_c: int = 0
            self.__show_c: int = 0

        def get_grow_c(self) -> int:
            return self.__grow_c

        def get_age_c(self) -> int:
            return self.__age_c

        def get_show_c(self) -> int:
            return self.__show_c

        def set_grow_c(self, count: int) -> None:
            self.__grow_c = count

        def set_age_c(self, count: int) -> None:
            self.__age_c = count

        def set_show_c(self, count: int) -> None:
            self.__show_c = count

        def display_counts(self) -> None:
            print(f"Stats: {get_grow_c()} grow, {get_age_c} count, {get_show_c} show")

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

    def anon_plant(self):
        self.name: str = "Unknown Plant"
        self.__height: float = 0
        self.__days: int = 0
        self.growth_rate: float = 0

    @staticmethod
    def year_query(days: int) -> bool:
        if (days >= 365):
            return True
        else:
            return False



class Flower(Plant):
    def __init__(self, name: str, height: float, growth_rate: float, days: int, color: str) -> None:
        super().__init__(name, height, growth_rate, days)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        if (self.bloomed == False):
            print(f" {self.name.capitalize()} has not bloomed yet.")
            print(f"[asking the {self.name} to bloom]")
            self.bloomed = True
            self.show()
            print(f" {self.name} is blooming beautifully!")

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")

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

    class TreeStats(Stats):
        def __init__(self, grow_c: int, age_c: int, show_c: int, shade_c: int) -> None:
            super().__init__(grow_c, age_c, show_c)
            self.shade_c = 0

        def get_shade_c(self) -> int:
            return self.__shade_c

        def set_shade_c(self, count: int) -> None:
            self.__shade_c = count

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

class Seed(Flower):
        def __init__(self, name: str, height: float, growth_rate: float, days: int, color: str, seeds: int) -> None:
            super().__init__(name, height, growth_rate, days, color)
            self.seeds = 0

        def seed_count(self):
            if (self.bloomed == True):
                self.seeds = ((self.growth_rate / 2) * self.days) / 2
                return (seeds)
            else:
                return (0)

        def show(self):
            super().show()
            print(f"Seeds: {self.seeds}")

def display_stats(plantae: Plant):
    plant_stats = plantae.Stats()
    plant_stats.display_counts()

print("=== Garden statistics ===")
print("=== Check year-old")
print(f"Is 30 days more than a year? -> {Plant.year_query(30)}")
print(f"Is 400 days more than a year? -> {Plant.year_query(400)}\n")

print("=== Flower")
# Flower name: str, height: float, growth_rate: float, days: int, color: str
p1 = Flower("Rose", 15.0, 0.1, 10, "red")
p1.show()
p1.bloom()

print("\n=== Tree")
# name: str, height:float, growth_rate: float, days: int, trunk_diameter: float
p2 = Tree("Oak", 200.0, 0.01, 365, 5.0)
p2.show()
display_stats(p2)

print("=== Seed")

print("=== Anonymous")
