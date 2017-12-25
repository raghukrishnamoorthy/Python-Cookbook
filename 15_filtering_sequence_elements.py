# Filter a sequence using some criteria

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print([n for n in mylist if n < 2])

# If original sequence is large

pos = (n for n in mylist if n < 2)

for x in pos:
    print(x)

# Use separate function when filter logic is complicated
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = filter(is_int, values)

for item in ivals:
    print(item)

myList = list(ivals)

print(myList)

# List Comprehensions

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

import math
[math.sqrt(n) for n in mylist if n > 0]

#if and else in list comprehension
clip_neg = [n if n > 0 else 0 for n in mylist]

addresses = [
'5412 N CLARK',
'5148 N CLARK',
'5800 E 58TH',
'2122 N CLARK'
'5645 N RAVENSWOOD',
'1060 W ADDISON',
'4801 N BROADWAY',
'1039 W GRANVILLE',
]

# Iterable and selector

from itertools import compress

counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]

filtered_list = list(compress(addresses, more5))

print(filtered_list)