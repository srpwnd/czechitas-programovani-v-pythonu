sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

print(sales)

sales["Noc, která mě zabila"] = 0

print(sales)

sales["Vrah zavolá v deset"] += 100
# to stejne jako:
# sales["Vrah zavolá v deset"] = sales["Vrah zavolá v deset"] + 100

print(sales)
