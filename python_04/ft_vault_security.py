def secure_archive(fn: str, rw: str = "r", content: str = "") -> tuple:
    check = False
    line_out = None
    try:
        if (rw == "w"):
            with open(fn, "w") as f:
                f.write(content)
                line_out = "Content successfully written to file"
                check = True
        elif (rw == "r"):
            with open(fn, "r") as f:
                line_out = f.read()
                check = True
        return (check, line_out)
    except FileNotFoundError:
        return (check, "[Error 2] File not found.")
    except PermissionError:
        return (check, "[Error 13] Permission denied.")


print("=== Cyber Archives Security ===")
print("Using 'secure_archive' to read from a nonexistent file:")
print(secure_archive("foo", "r"), end='\n\n')
print("Using 'secure_archive' to read from an inaccessible file:")
print(secure_archive("illegal_file.txt", "r"), end='\n\n')
print("Using 'secure_archive' to read from a regular file:")
print(secure_archive("ancient_fragment.txt", "r"), end='\n\n')
print("Using 'secure_archive' to write to a new file:")
print(secure_archive("new.txt", "w", "this is a test"), end='\n\n')
print(secure_archive("new.txt"), end='\n\n')
