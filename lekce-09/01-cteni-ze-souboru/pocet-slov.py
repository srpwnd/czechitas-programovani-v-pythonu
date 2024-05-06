total_words = 0
word_counts_per_line = []

with open("lekce-09/praha.txt", encoding="utf-8") as file:
    for line in file:
        words = line.split()
        word_count = len(words)
        word_counts_per_line.append(word_count)
        total_words += word_count

print(f"celkovy pocet slov: {total_words}")

for num, line in enumerate(word_counts_per_line, start=1):
    print(f"{num}: {line}")
