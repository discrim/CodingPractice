# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 17:57:21 2020

@author: shiny
"""

import re

p1 = re.compile("[a-z]+")
print(p1.match('python'))
print(p1.match('3 python'))
print(p1.match('python 3'))

print('\n-------------------- BORDER --------------------\n')

m1 = p1.match('string goes here')
if m1:
    print('Match found: ', m1.group())
else:
    print('No match')

print('\n-------------------- BORDER --------------------\n')

print(p1.search('python'))
print(p1.search('3 python'))

print('\n-------------------- BORDER --------------------\n')

print(p1.findall('life is 2 short'))

print('\n-------------------- BORDER --------------------\n')

r1 = p1.finditer('life is 2 short')
for rr in r1:
    print(rr)

print('\n-------------------- BORDER --------------------\n')

m11 = p1.match('python')
print(m11.group(), ' / ', m11.start(), ' / ', m11.end(), ' / ', m11.span())
m12 = p1.search('3 python')
print(m12.group(), ' / ', m12.start(), ' / ', m12.end(), ' / ', m12.span())

print('\n-------------------- BORDER --------------------\n')

m2 = re.match("[a-z]+", 'python')
print(m2)

print('\n-------------------- BORDER --------------------\n')

p3 = re.compile("a.b")
print(p3.match('a\nb'))
p4 = re.compile("a.b", re.DOTALL)
print(p4.match('a\nb'))

print('\n-------------------- BORDER --------------------\n')

p5 = re.compile("[a-z]", re.IGNORECASE)
print(p5.match('python'))
print(p5.match('Python'))
print(p5.match('PYTHON'))

print('\n-------------------- BORDER --------------------\n')

data = """python one
life is too short
python two
you need python
python three"""
p6 = re.compile("^python\s\w+") # "^python[ \t\n\r\f\v][a-zA-Z0-9_]+
print(p6.findall(data))
p7 = re.compile("^python[ \t\n\r\f\v][a-zA-Z0-9_]+", re.MULTILINE)
print(p7.findall(data))

print('\n-------------------- BORDER --------------------\n')

charref = re.compile(r"&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);")
charref = re.compile(r"""
&[#]                # Start of a numeric entity reference
(
    0[0-7]+         # Octal form
  | [0-9]+          # Decimal form
  | x[0-9a-fA-F]+   # Hexadecimal form
)
;                   # Trailing semicolon
""", re.VERBOSE)

print('\n-------------------- BORDER --------------------\n')

p8 = re.compile('\\section')