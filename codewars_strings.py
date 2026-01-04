def array(string):
    if not string:
        return None

    parts = string.split(",")

    if len(parts) <= 2:
        return None

    return " ".join(parts[1:-1])




def is_uppercase(inp):
    return inp == inp.upper()


def reverse_words(s):
    return " ".join(s.split(" ")[::-1])

def filter_list(l):
    return [x for x in l if isinstance(x, int)]

def double_integer(i):
    return i * 2


def lovefunc( flower1, flower2 ):
    return (flower1 + flower2) % 2 == 1



def number(bus_stops):
    return sum(on - off for on, off in bus_stops)


def find_longest(arr):
