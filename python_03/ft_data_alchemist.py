import random

ini_names = ['Alice',
             'bob',
             'Charlie',
             'dylan',
             'Emma',
             'Gregory',
             'john',
             'kevin',
             'Liam']
capped_names = [element.capitalize() for element in ini_names]
ini_capped_names = [element for element in ini_names
                    if element.capitalize() == element]

print("=== Game Data Alchemist ===")

print(f"Initial list of players: {ini_names}")
print(f"New list with all names capitalized: {capped_names}")
print(f"New list of capitalized names only: {ini_capped_names}\n")

cvt_names = {element: random.randint(0, 1000) for element in capped_names}
print(f"Score dict: {cvt_names}")

total = 0
for element in cvt_names:
    total += cvt_names[element]
avg = total/len(cvt_names)
print(f"Score average is {avg:.2f}")

upper_scores = {element: cvt_names[element] for element in capped_names
                if cvt_names[element] > avg}
print(f"High Scores: {upper_scores}")
