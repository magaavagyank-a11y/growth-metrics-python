from datetime import datetime
from datetime import timedelta
from json_practice import users

today = datetime.now()
formatted_date = today.strftime("%d-%B-%Y ")
print("Current date and time:", formatted_date)

registration_date_str = "2024-06-01"
registration_date = datetime.strptime(registration_date_str, "%Y-%m-%d")
days_since_registration = (today - registration_date).days
print("Days since registration:", days_since_registration)

def days_since_registration(reg_date_str):
    reg_date = datetime.strptime(reg_date_str, "%Y-%m-%d")
    return (datetime.now() - reg_date).days
print("Days since registration function test:", days_since_registration("2024-05-20"))



dates_last_week = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]
print("Last week:", dates_last_week)

with open("last_week_dates.json", "w") as f:
    for d in dates_last_week:
        f.write(d + "\n")


def calc_retention(users, day):
    retained = 0
    total = len(users)

    for user in users:
        reg = datetime.strptime(user["registration_date"], "%Y-%m-%d")
        for login in user["logins"]:
            login_date = datetime.strptime(login, "%Y-%m-%d")
            diff = (login_date - reg).days
            if diff == day:
                retained += 1
                break

    return round(retained / total, 2)

d1 = calc_retention(users, 1)
d3 = calc_retention(users, 3)
d7 = calc_retention(users, 7)

print("D1 Retention:", d1)
print("D3 Retention:", d3)
print("D7 Retention:", d7)
