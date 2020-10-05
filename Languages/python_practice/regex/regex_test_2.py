from re import compile

p01 = compile(r"one|two|three")
m01 = 'one and two and three and four'
print(p01.findall(m01))

p02 = compile(r"\d\d? o'clock")
m02 = "1 o'clock, 12 o'clock"
print(p02.findall(m02))

p03 = compile(r'\d\d? [AP]M')
#p03 = compile(r'1 AM')
m03 = '1 AM 12 PM'
print(p03.findall(m03))

p04 = compile(r' ')
m04 = ' a b '
print(p04.findall(m04))

p05 = compile(r'\d\d\d\d[-/]\d\d[-/]\d\d')
m05 = '2020-09-23 2020/09/23'
print(p05.findall(m05))

p06 = compile(r'Mondays?|Tuesdays?')
m06 = 'Monday Mondays Tuesday Tuesdays'
print(p06.findall(m06))

p07 = compile(r'Mon\.|Tue\.')
m07 = 'Mon. Tue.'
print(p07.findall(m07))

p08 = compile(r'\S+@\S+')
m08 = 'junkeunp@umich.edu junkeun.p4rk@gmail.com your_addr@very.long.domain.io'
print(p08.findall(m08))

p09 = compile(r'\$\d+.\d\d')
m09 = '$14.65 $20 $0.50'
print(p09.findall(m09))

p10 = compile(r'www\.\S+')
m10 = 'www.google.com www.eecs.umich.edu'
print(p10.findall(m10))

p11 = compile(r'https?://\S+')
m11 = 'http://naver.com https://github.com'
print(p11.findall(m11))

p12 = compile(r'one.*?dollars?')
m12 = 'I have one dollar. You have one million dollars.'
#m12 = 'one dollars'
print(p12.findall(m12))

p13 = compile(r'\$\d{1,3} billion')
m13 = 'I have $100 billion. How about you?'
print(p13.findall(m13))

p14 = compile(r'a .*?dollars?')
m14 = 'Give me a few hundred dollars or so. How about a thousand dollars?.'
print(p14.findall(m14))

p15 = compile(r'several .*?dollars?')
m15 = 'Need several hundred dollars for the job. Or several thousand dollars is also good.'
print(p15.findall(m15))

p16 = compile(r"\b[a-zA-Z'-]+\b")
m16 = "word apple 12 times _fase_ don't center-fielder"
print(p16.findall(m16))

p17 = compile(r"[Ff]ive past [a-z]+")
m17 = "it is five past ten or so"
print(p17.findall(m17))

p18 = compile(r'September \d\d?, \d\d\d\d')
m18 = "Today is September 23, 2020 as I know."
print(p18.findall(m18))