# 1.1
# UNPACKING SEQUENCES

p = (4, 5, 6)
x, y, z = p
print(x, y, z)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, mon, day) = data
print(name, shares, price, year, mon, day)

# Works with any iterable object
s = "Hello"
a, b, c, d, e = s
print(a, b, c)

# Use _ for throwaway variables
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, _, _ = data
print(shares)


# 1.2
# UNPACKING SEQUENCES - ARBITRARY LENGTH

# Use * expressions for arbitrary length unpacking
# Dropping first and last grades and average the rest
grades = []
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)/len(middle)

record = ("John", "john@gmail.com", "123123214312", "6452434324", "6435435")
name, email, *phone_numbers = record
print(phone_numbers)

# Works even if phone numbers is []
record = ("John", "john@gmail.com")
name, email, *phone_numbers = record
print(phone_numbers)

# Use the * in the beginning if neccessary
four_quarters_data = [2.5, 4.2, 3.5, 4.5]
*prev_quarters, curr_quarter = four_quarters_data
print((sum(prev_quarters)/ len(prev_quarters)) + curr_quarter / 2 )

# Iterating over tuples of varying length
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]

def do_foo(x, y):
    print('foo', x , y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    else:
        do_bar(*args)

# Helpful in string splitting 
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)

# Use *_ or *ign when you need to unpack values and throw them away
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

# Use * to split a list into Head and Tail
head, *tail = [1, 2, 3, 4 ,5]
print(tail)

# Using it in recursive algos
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

