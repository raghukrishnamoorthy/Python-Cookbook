print(round(1.23,1))
print(round(1.2345, 3))

# Negative numbers round the ones, tens, hundreds and so on..
print(round(123124123, -1))
print(round(54213, -2))

# Round is not neccessary for display reasons. use format instead

x = 1.8913479812313

print("value is {:0.3f}".format(x))