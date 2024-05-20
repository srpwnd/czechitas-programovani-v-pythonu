import requests

url = "https://api.kodim.cz/python-data/people"

response = requests.get(url)
data = response.json()

people_count = len(data)
print(f"Celkem lidi: {people_count}")

print(data[0].keys())

female_count = 0
for person in data:
    if person["gender"] == "Female":
        female_count += 1

f_count = sum([1 for person in data if person["gender"] == "Female"])

print(f"V souboru je {f_count} žen.")
print(f"{people_count - female_count}")