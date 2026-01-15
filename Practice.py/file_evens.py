nums = [3, 10, 7, 4, 8, 5, 2]


print("File evens.txt created successfully!")

def save_even_numbers(filename, numbers):
    count = 0
    with open(filename, "w") as f:
        for num in numbers:
            if num % 2 == 0:
                f.write(f"{num}\n")
                count += 1
    return count

with open("evens.txt","r") as f:
    for line in f:
        print(line.strip())

count = save_even_numbers("evens.txt", nums)
print("count = ", count)
