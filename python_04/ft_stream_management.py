import sys
import typing


class InputError(Exception):
    pass


class MissingFileError(Exception):
    pass


file_lines = []
new_lines = []
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
            file_lines.append(line)
        print("\n---")
        f.close()
        print(f"File '{file_name}' closed.\n")

        print("Transform data:")
        print("---\n")
        for line in file_lines:
            nlines = line.strip() + "#"
            print(f"{nlines}")
            new_lines.append(nlines+"\n")
        print("\n---")

        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_fn = sys.stdin.readline().strip()
        sys.stdout.flush()
        if (new_fn == ""):
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_fn}'")
            nf = open(new_fn, "w")
            for line in new_lines:
                nf.write(line)
            print(f"Data saved in file '{new_fn}'.\n")
            nf.close()
    except FileNotFoundError:
        print("[STDERR] [Error 2]: failed to ", end='', file=sys.stderr)
        print("open file, file not found.", file=sys.stderr)
    except PermissionError:
        print("[STDERR] [Error 13]: failed to ", end='', file=sys.stderr)
        print("open file, permission denied.", file=sys.stderr)
