import sys
import typing


class InputError(Exception):
    pass


class MissingFileError(Exception):
    pass


if (len(sys.argv) == 1):
    print("Usage: ft_ancient_text.py <file>")
elif (len(sys.argv) == 2):
    file_name = sys.argv[1]
    try:
        print(" === Cyber Archives Recovery ===")
        print(f"Accessing file '{file_name}'")
        f = open(file_name)
        print("---\n")
        for line in f:
            print(line, end='')
        print("\n---")
        f.close()
        print(f"File '{file_name}' closed.")
    except FileNotFoundError:
        print("[Error 2]: failed to open file, file not found.")
    except PermissionError:
        print("[Error 13]: failed to open file, permission denied.")
