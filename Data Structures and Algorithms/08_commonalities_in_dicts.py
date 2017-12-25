# Find common things between two Dictionaries. Use set operators.
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

#Make a new dict with keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}

print(c)