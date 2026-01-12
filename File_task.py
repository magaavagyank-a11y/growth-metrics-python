from datetime import datetime
import random

users = [
    {"name":"John", "age":30,"registered":True},
    {"name":"Jane", "age":25,"registered":False},
    {"name":"Doe", "age":40,"registered":True},
    {"name":"Smith", "age":28,"registered":False},
    {"name":"Emily", "age":22,"registered":True},
    {"name":"Michael", "age":33,"registered":False},
    {"name":"Sarah", "age":27,"registered":True},
    {"name":"David", "age":45,"registered":False}
]

with open("users.csv","w") as f:
    f.write("Name,Age,Registered\n")  # Write header
    for user in users:
        f.write(f"{user['name']},{user['age']},{user['registered']}\n")


with open("users.csv","r") as f:
    next(f)  # Skip header line
    for line in f:
            name, age ,registered  = line.strip().split(",")
            if int(age) > 30:
                print("name:",name,"age:",age)


def save_users_to_file(users_list, filename):
    with open(filename, "w") as f:
        f.write("name,age,registered\n")
        for u in users_list:
            f.write(f"{u['name']},{u['age']},{u['registered']}\n")


def load_users_from_file(filename):
    users = []
    with open(filename, "r") as f:
        next(f)
        for line in f:
            name, age, registered = line.strip().split(",")
            users.append({
                "name": name,
                "age": int(age),
                "registered": registered
            })
    return users

with open("login_logs.csv", "w") as f:
    f.write("user_id,timestamp\n")
    for _ in range(10):
        if "registered" in users[random.randint(0, len(users)-1)] and users[random.randint(0, len(users)-1)]["registered"]:
            user_id = random.randint(1, 5)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{user_id},{timestamp}\n")