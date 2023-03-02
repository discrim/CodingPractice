# regex lookaround

from re import compile

samples1 = [
    "fruit:apple",
    "fruit:apple:look",
    "fruit:apple:eat",
    "fruit:banana",
    "fruit:banana:look",
    "fruit:banana:eat",
    "fruit:cherry",
    "fruit:cherry:look",
    "fruit:cherry:eat",
    "fruit:grape",
    "fruit:grape:look",
    "fruit:grape:eat"
]

p1 = compile("fruit:(?!apple|banana).*")

for sample in samples1:
    print(p1.findall(sample))

samples2 = [
    "calendar:accept",
    "calendar:accept_tentatively",
    "calendar:add",
    "calendar:call",
    "calendar:delete",
    "calendar:directions",
    "calendar:edit",
    "calendar:lookup",
    "calendar:na",
    "calendar:read",
    "calendar:reject",
    "calendar:search",
    "calendar:question"
]

p2 = compile("calendar:(?:search|question)(:(?:.*)|)")
# p2 = compile("calendar:(:search|question)")

for sample in samples2:
    print(p2.findall(sample))