def ft_count_harvest_recursive():
    i = int(1)
    t_harvest = int(input("Days until harvest: "))
    recursion_count(t_harvest, i)


def recursion_count(t_harvest: int, i: int) -> None:
    if (i == t_harvest + 1):
        print("Harvest time!")
    else:
        print("Day", i)
        return (recursion_count(t_harvest, (i + 1)))
