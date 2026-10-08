def parse_input() -> list:
    raw_input = str(input("Hark adventurer! Fill your inventory with items! "))
    group_input = raw_input.split(' ')
    clean_input = []
    for element in group_input:
        clean_input.append(element.split(':'))
    return clean_input


raw_inv = parse_input()

while True:
    try:
        for element in raw_inv:
            element[1] = int(element[1])
        break
    except IndexError:
        print("Invalid Input! Input items in format <item_name>:<quantity>.")
    except ValueError:
        print("Invalid Input! Input items in format <item>:<quantity (int)>.")
    raw_inv = parse_input()

inv = dict(raw_inv)
print(f"Got inventory: {inv}")
print(f"Item list: {list(inv.keys())}")

item_total = 0
for element in inv:
    item_total += inv[element]

print(f"Total quantity of the {len(inv)} items: {item_total}")

largest_n = 0
ln_key = ""
smallest_n = list(inv.values())[0]
sn_key = list(inv)[0]
for element in inv:
    if (inv[element] > largest_n):
        largest_n = inv[element]
        ln_key = element
    if (inv[element] < smallest_n):
        smallest_n = inv[element]
        sn_key = element
    print(f"Item {element} represents", end='')
    print(f"{((inv[element]/ item_total) * 100):.1f}%")

print(f"Item most abundant: {ln_key} with quantity {largest_n}")
print(f"Item least abundant: {sn_key} with quantity {smallest_n}")

inv.update({"Wabbajack": 1})
print(f"Updated inventory: {inv}")

# unfinished: discard illegal and duplicate vals
