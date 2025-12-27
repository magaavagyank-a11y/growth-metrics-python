def array(string):
    if not string:
        return None

    parts = string.split(",")

    if len(parts) <= 2:
        return None

    return " ".join(parts[1:-1])




def is_uppercase(inp):
    return inp == inp.upper()
