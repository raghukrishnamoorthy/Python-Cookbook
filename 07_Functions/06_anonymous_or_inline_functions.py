add = lambda x, y: x + y
print(add(4, 5))
print(add("hello", "world"))

# used in other operations
names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger',
         'Ned Batchelder']

names.sort(key=lambda name: name.split(' ')[-1].lower())

print(names)