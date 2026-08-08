from pickle import TRUE

print(min(1, 2, 4), 3, 6, sep=" - ")

print(100, 51, 14)


def mod_5(x):
    return x % 5


print(max(100, 51, 14, key=lambda x: x % 5))
print(max(100, 51, 14, key=mod_5))


def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings."""
    return not (ketchup or mustard or onion)


print(wants_plain_hotdog(False, False, False))
print(wants_plain_hotdog(True, True, True))
print(wants_plain_hotdog(False, False, True))


def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    return (ketchup and not mustard) or (mustard and not ketchup)


def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (ketchup + mustard + onion) == 1


planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]
print(planets[:2])  # Mercury, Venus
print(planets[0:])  # Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
print(planets[2:-2])  # Earth, Mars, Jupiter, Saturn
print(planets[-2:])  # Uranus, Neptune
print("Earth" in planets)  # True
print(planets.index("Earth"))  # 2
planets[:3] = ["Mur", "Vee", "Ur"]
print(planets)  # ['Mur', 'Vee', 'Ur', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)


x = 1123
print(x.bit_length())
print(bin(x))

tup = (1, 2, 3)
print(tup)  # (1, 2, 3)
print(tup[0])  # 1
print(tup[-1])  # 3
tup1 = 0, 3, 6
print(tup1)  # (0, 3, 6)
print(tup + tup1)  # (1, 2, 3, 0, 3, 6)


x = 0.125
num, den = x.as_integer_ratio()
print(num, den, sep=" / ")  # 1 / 8

a = 1
b = 0
a, b = b, a
print(a, b)  # 0 1


a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]
lengths = [3, 2, 0, 2]
# a: There are three items in this list. Nothing tricky yet.
# b: The list [2, 3] counts as a single item. It has one item before it. So we have 2 items in the list
# c: The empty list has 0 items
# d: The expression is the same as the list [2, 3], which has length 2.


s = "steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video."
msg = ""
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end="")
print()

squares = [n**2 for n in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)  # ['Mur', 'Vee', 'Ur']
loud_short_planets = [planet.upper() + "!" for planet in planets if len(planet) < 6]
print(loud_short_planets)  # ['MUR!', 'VEE!', 'UR!']
#     for(plantet in planets):
#      if(len(plantet) < 6):
#       print(plantet.upper() + "!")

print([32 for planet in planets])  # [32, 32, 32, 32, 32, 32, 32, 32]
nums = [5, -1, -2, 0, 3]
print([num for num in nums if num < 0])
print([num < 0 for num in nums])
print(any([num % 7 == 0 for num in nums]))
print([num > 2 for num in nums])

nums = [0, 0, 0, 1, 2, 3, 4]
for i in range(1, len(nums)):
    print(nums[i - 1] == nums[i])

equal = [nums[i - 1] == nums[i] for i in range(1, len(nums))]
print(equal)  # [False, False, False, False]

print(nums[i - 1] == nums[i] for i in range(1, len(nums)))
# <generator object <genexpr> at 0x000002276480FA00>
#
print(*(nums[i - 1] == nums[i] for i in range(1, len(nums))))  # False False False False

print([nums[i - 1] == nums[i] for i in range(1, len(nums))])
# [False, False, False, False]

xd = [5, 6, "si"]
print(xd)
print(*xd, sep=" *** ")
# the '*' means unpacking operator

hello = "hello\nworld"
print(hello)
triplequoted_hello = """hello
world"""
print(triplequoted_hello)
print(triplequoted_hello == hello)  # True
xxxd = "XdxdXD"
print([c + "!" for c in xxxd])  # ['X!', 'd!', 'd!', 'X!', 'D!', 'X!']

ooo = "ooo aaa bbb"
print(ooo.upper())
print(ooo.index("aa"))  # 4
print(ooo.startswith("oao"))  # False
print(ooo.endswith("bbb"))  # True
words = ooo.split()
print(words)  # ['ooo', 'aaa', 'bbb']
print(words[0])  # 'ooo'
a, b, c = words
print(a, b, c)  # 'ooo' 'aaa' 'bbb'
date = "1992-01-01"
y, m, d = date.split("-")
print(y, m, d)  # '1992' '01' '01'
print("/".join([y, m, d]))  # '1992/01/01'
print(" ".join(words))  # 'ooo aaa bbb'

newD = 30
print(y + m + d)  # '19920101'
# print(y + m + newD) = TypeError: can only concatenate str (not "int") to str
print(y + str(m) + str(newD))  # '19920130'

planet = "Pluto"
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print(
    "{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
        planet,
        pluto_mass,
        pluto_mass / earth_mass,
        population,
    )
)
# Pluto weighs about 1.3e+22 kilograms (0.218% of Earth's mass). It is home to 52,910,390 Plutonians.


# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format("planet", "dwarf planet")
print(s)


planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
}

for k in numbers:  # iterate over the keys
    print("{} = {}".format(k, numbers[k]))

print(" ".join(sorted(planet_to_initial.values())))
for planet, initial in planet_to_initial.items():
    print('{} begins with "{}"'.format(planet.rjust(10), initial))

docdoc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
keyword = "casino"


def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword.
    Returns list of the index values into the original list for all documents
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    list = []
    for i, stt in enumerate(doc_list):
        words = stt.split()
        unique = [word.rstrip(".,").lower() for word in words]
        if keyword.lower() in unique:
            list.append(i)
    return list


print(word_search(docdoc_list, keyword))


def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    indices = {keyword: [] for keyword in keywords}  # the dict need to be initialized
    for keyword in keywords:
        for i, doc in enumerate(doc_list):
            tokens = doc.split()
            normalized = [token.rstrip(".,").lower() for token in tokens]
            if keyword.lower() in normalized:
                indices[keyword].append(i)
    return indices


print(multi_word_search(docdoc_list, ["casino", "they", "car"]))
