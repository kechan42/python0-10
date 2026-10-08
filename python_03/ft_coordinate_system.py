import math


class InputError(Exception):
    pass


def get_player_pos() -> list[int]:
    while True:
        coords = []
        i = 0
        prev_comma = 0
        comma_count = 0
        parse = str(input("Enter coordinates as floats in 'x,y,z' format: "))
        try:
            while (i < len(parse)):
                if (parse[i] == ','):
                    if (comma_count <= 1):
                        coords.append(int(parse[prev_comma:i]))
                        prev_comma = i + 1
                        comma_count += 1
                    else:
                        raise InputError
                elif (comma_count == 2):
                    coords.append(int(parse[prev_comma:]))
                    comma_count += 1
                elif (i == len(parse)):
                    raise InputError
                i += 1
            if (len(coords) != 3):
                raise InputError
            return coords
        except (InputError):
            print("Input Error: Try Again.")
    print(coords)


def coord_calc(a: list, b: list) -> None:
    centre_d = math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2] - a[2])**2)
    print(f"Distance to centre is {centre_d:.2f}")


print("Pos 1, ", end='')
x = get_player_pos()
print(f"First tuple: {x}")
print("Pos 2, ", end='')
y = get_player_pos()
print(f"Second tuple: {y}")
coord_calc(x, y)
