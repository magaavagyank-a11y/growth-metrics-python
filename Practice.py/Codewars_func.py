def disemvowel(string_):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string_ if char not in vowels)

def square_digits(num):
    return int(''.join(str(int(digit) ** 2) for digit in str(num)))

