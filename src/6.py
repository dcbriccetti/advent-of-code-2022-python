from pathlib import Path

data = Path('../data/6.txt').read_text().rstrip()
for marker_len in (4, 14):
    for i in range(len(data) - marker_len):
        four_chars = data[i:i + marker_len]
        if len(set(four_chars)) == marker_len:
            print(i + marker_len)
            break
