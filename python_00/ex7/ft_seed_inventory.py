def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    p_seed = str(seed_type).capitalize()
    if (unit == "grams"):
        print(f"{p_seed} seeds: {quantity} {unit} total")
    elif (unit == "packets"):
        print(f"{p_seed} seeds: {quantity} {unit} available")
    elif (unit == "area"):
        print(f"{p_seed} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
