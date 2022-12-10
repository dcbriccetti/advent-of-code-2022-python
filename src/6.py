from pathlib import Path

data = Path('../data/6.txt').read_text().rstrip()
for i in range(len(data) - 4):
    four_chars = data[i:i + 4]
    if len(set(four_chars)) == 4:
        print(i + 4)
        break
