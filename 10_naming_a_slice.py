# When you have a slice hardcoded like example[20:32]
# instead create a slice object.

SHARES = slice(20, 32)
PRICE = slice(50, 104)
# Better Readability

#Slice objects can be used anywhere
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)
print("Get information about the slice")
a = slice(10, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

# Map a slice to a sequence using the indices method
s = "HelloWorld"
indicestuple = a.indices(len(s))
print(indicestuple)