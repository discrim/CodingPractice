with open("sample_text.txt", mode="r") as infile:
    raw = infile.readlines()
print(raw)

import json
data = [json.loads(line) for line in raw]
print(data)