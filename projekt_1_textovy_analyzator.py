"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Pavel Boštík
email: pawelbostik@gmail.com
discord: pawelbostik
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

separator = 40*"_"

user_password = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
    }

print(separator)

user = input("Enter your username: ")
password = input("Enter your password: ")
password_1 = user_password.get(user)
if user in user_password and password_1 in password:
  print("Welcome to the app", user.title(), f"\nwe have {len(TEXTS)} texts to be analyzed.", sep=", ")
else:
    print("Unregistered user, terminating the program...")
    exit()

print(separator)

select = input("Enter a number btw. 1 and 3 to select: ")
if select.isnumeric():
    select = int(select)
    if select < 1 or select > 3:
        print(f"{select} is not numbers 1-3, terminating the program...")
        exit()
    else:
        text = TEXTS[select - 1]
else:
    print(f"{select} is not a number, terminating the program....")
    exit()

print(separator)

word = text.split()

titlecase = list()
lowercase = list()
numbers = list()
uppercase = list()

for letter in word:
    if letter.istitle():
        titlecase.append(letter)
    elif letter.islower():
        lowercase.append(letter)
    elif letter.isupper():
        uppercase.append(letter)
    else:
        numbers.append(letter)

print("There are", len(word), "words in the selected text.")
print("There are", len(titlecase), "titlecase words.")
print("There are", len(lowercase), "lowercase words.")
print("There are", len(uppercase), "uppercase words.")
print("There are", len(numbers), "numeric strings.")

numbers_1 = (int(number) for number in numbers)
print("The sum of all the numbers:", sum(numbers_1))

punctuation = [",", "."]
for punctuation in punctuation:
    text = " ".join(text.split(punctuation))
    text_1 = text.split()

names = list()
for logos in text_1:
    lenght = len(logos)
    names.append(lenght)

num = dict()
for index in names:
    num[index] = num.get(index, 0) + 1
key = list(num.keys())
key.sort()
sort_dict = {index: num[index] for index in key}

print(separator)
star = "*"
space = " "
print(space, "LEN", "|", 3*space, "OCCURRENCES ", 3*space, "|", "NR.")
print(separator)

for key, value in sort_dict.items():
    if key < 10:
        print(2 * space, key, "|", star * value, space * (19 - value), "|", value)
    if key >= 10:
        print(space, key, "|", star * value, space * (19 - value), "|", value)

print(separator)