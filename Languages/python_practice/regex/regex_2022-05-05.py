from re import compile

p1 = compile(r"\b(오늘|오늘에|오늘의)\b")
m1 = \
    ["오늘 뉴스", "오늘뉴스", "어제 오늘 뉴스", "어제오늘 뉴스", "어제 오늘뉴스",
    "오늘에 뉴스", "오늘의 상", "오늘의상"]
for elem in m1:
    print(elem, ": ", p1.findall(elem))

p2 = compile(r"답신|되돌|반환|회신")
m2 = \
    ["전화 답신", "전화 답신해", "통화 되돌려줘", "회신전화", "회신전화 걸어"]
for elem in m2:
    print(elem, ": ", p2.findall(elem))