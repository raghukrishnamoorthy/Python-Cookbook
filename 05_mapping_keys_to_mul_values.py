from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

d = defaultdict(set)
pairs = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(pairs)

for key, value in pairs.items():
    d[key].add(value)

print(d)
