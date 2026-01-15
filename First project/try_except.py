import csv
import json
from datetime import datetime


try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the file path.")
        
try:
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) !=3:
                raise ValueError("Row does not have exactly 3 columns")
            print(row)

except FileNotFoundError:
    print("data.csv file not found.")
except ValueError as ve:
    print("ValueError:", ve)
               

def self_divide(number1,number2):
    try:
        result = number1 / number2
        print("Result:", result)
    except ZeroDivisionError:
        print("Cannot divide by zero.")

print(self_divide(10,5))
print(self_divide(10,0))

try:
    with open("users.json","r") as f:
        data = json.load(f)
        print(data)
except FileNotFoundError:
    print("users.json file not found.")
except json.JSONDecodeError:
    print("Error decoding JSON from the file.")


def calc_retention(users, day):
    try:
        if len(users) == 0:
            raise ZeroDivisionError("No users provided.")
        total = len(users)
        retained = 0

        for user in users:
            reg = datetime.strptime(user["registration_date"], "%Y-%m-%d")
            target_day = reg.replace(day=reg.day + day)

            if target_day.strftime("%Y-%m-%d") in user["logins"]:
                retained += 1

        return round(retained / total, 2)
    except ZeroDivisionError:
        print("Error: No users to calculate retention.")
        return 0.0