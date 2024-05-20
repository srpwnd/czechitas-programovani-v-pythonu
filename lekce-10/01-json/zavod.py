import json

with open("lekce-10/zavod.json", mode="r", encoding="utf-8") as file:
    runners = json.load(file)

finishers = []

for runner in runners:
    if runner["casy"]["oficialni"] != "DNF":
        finishers.append([runner["jmeno"], runner["casy"]["oficialni"]])


print(finishers[1])