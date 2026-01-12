import json

users = [
    {
        "user_id": 1,
        "name": "Anna",
        "registration_date": "2026-01-05",
        "logins": ["2026-01-05", "2026-01-06", "2026-01-08"]
    },
    {
        "user_id": 2,
        "name": "Bob",
        "registration_date": "2026-01-05",
        "logins": ["2026-01-05"]
    },
    {
        "user_id": 3,
        "name": "Marta",
        "registration_date": "2026-01-05",
        "logins": ["2026-01-05", "2026-01-12"]
    }
]

with open("users.json", "w") as f:
    json.dump(users, f, indent=4)

print("users.json сreated successfully!")

with open("users.json", "r") as f:
    loaded_users = json.load(f)

print(loaded_users)

dau = 0
mau = len(loaded_users)

for user in loaded_users:
    if len(user["logins"]) > 0:
        dau += 1

ratio = round(dau / mau, 2)

print("DAU:", dau)
print("MAU:", mau)
print("DAU/MAU ratio:", ratio)

from datetime import datetime

def calc_retention(users, day):
    retained = 0
    total = len(users)

    for user in users:
        reg = datetime.strptime(user["registration_date"], "%Y-%m-%d")
        target_day = reg.replace(day=reg.day + day)

        if target_day.strftime("%Y-%m-%d") in user["logins"]:
            retained += 1

    return round(retained / total, 2)

d1 = calc_retention(loaded_users, 1)
d3 = calc_retention(loaded_users, 3)
d7 = calc_retention(loaded_users, 7)

print("D1 Retention:", d1)
print("D3 Retention:", d3)
print("D7 Retention:", d7)