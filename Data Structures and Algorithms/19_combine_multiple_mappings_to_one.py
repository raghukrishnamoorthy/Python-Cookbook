# Combine two mappings into one
# For eg, performing look up on two dicts combined looks in the first dict for a value,
# if not found, looks at the second 

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap
c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])

# Mutate operations always affect the first mapping only !!!
c['z'] = 10
c['w'] = 40
del c['x']
#del c['y']
print(c)

# Useful when working with scoped values like variables
# in programming

values = ChainMap()
values['x'] = 1
print(values)
values = values.new_child()
values['x'] = 2
print(values)
values = values.new_child()
values['x'] = 3
print(values)
values = values.parents
print(values)
values = values.parents
print(values)
values = values.parents
print(values)

# One can also merge dictionaries using the update method
# but the merged dict does not reflect changes in the original dict
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['x'])
print(merged['y'])
print(merged['z'])

#Chainmap solves the above problem
c= ChainMap(a, b)
a['x'] = 500
print(c)