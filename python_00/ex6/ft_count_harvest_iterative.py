def ft_count_harvest_iterative():
    i = int(1)
    t_harvest = int(input("Days until harvest: "))
    while (i <= t_harvest):
        print("Day", i)
        i += 1
    print("Harvest time!")
