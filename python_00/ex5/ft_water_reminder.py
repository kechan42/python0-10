def ft_water_reminder():
    t_water = int(input("Days since last watering: "))
    if (t_water > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
