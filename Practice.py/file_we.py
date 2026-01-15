users = [
    {"name":"Alice", "age":30},
    {"name":"Bob", "age":25},
    {"name":"Charlie", "age":35}    
]

with open("users.txt","w") as f:
    for user in users:
        f.write(f"{user['name']},{user['age']}\n")


print("File users.txt created successfully!")

with open("users.txt","r") as f:
    for line in f:
        name, age = line.strip().split(",")
        print(f"Name: {name}, Age: {age}")