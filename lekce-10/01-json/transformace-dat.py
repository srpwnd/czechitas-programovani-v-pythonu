import json

words = {}

with open("lekce-10/words.txt", mode="r", encoding="utf-8") as file:
    for line in file:
        word = line.strip()
        letter = word[0]
        if letter in words:
            words[letter].append(word)
        else:
            words[letter] = [word]

with open("lekce-10/output.json", mode="w", encoding="utf-8") as json_file:
    json.dump(words, json_file, indent=4, sort_keys=True)