import requests

day = input("Please enter the day: ")
month = input("Please enter the month: ")

date_str = f"{int(day):02d}{int(month):02d}"

params = {"date": date_str}

response = requests.get("https://svatky.adresa.info/json", params=params)

if response.status_code == 200:
    data = response.json()
    # Check if the data list is not empty
    if data:
        print(f"Name day on {day}. {month}. is for: {data[0]['name']}")
    else:
        print(f"No name day found for the date {day}. {month}.")
else:
    print("Failed to fetch data from the API")
