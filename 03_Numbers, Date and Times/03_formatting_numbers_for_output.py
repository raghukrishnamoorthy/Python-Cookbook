# Need to format a number for output, number of digits, alignment etc.,

x = 1234.56789

# TWO DECIMALS
print(format(x,'0.2f')) 
# or 
print("{:0.2f}".format(x))

# RIGHT JUSTIFIED
print(format(x, '>10.1f'))
# or 
print("{0:>10.1f}".format(x))

# LEFT JUSTIFIED
print(format(x, '<10.1f'))
# or 
print("{0:<10.1f}".format(x))

# CENTERED
print(format(x, '^10.1f'))
# or 
print("{0:^10.1f}".format(x))

# INCLUSION OF THOUSANDS OPERATOR
print(format(x, ','))
print("{:0,}".format(x))

