class Plant:
    def __init__(self, name: str, height: float, growth_rate: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days
        self.growth_rate: float = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 3)}cm, {self.days} days old")

    def age(self) -> None:
        self.days += 1

    def grow(self) -> None:
        self.height += self.growth_rate

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


print("=== Plant Factory Output ===")
p1 = Plant("Rose", 25, 0.8, 30)
p1.show()
p1.cycle(7)
