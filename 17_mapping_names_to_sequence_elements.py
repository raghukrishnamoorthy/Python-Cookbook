from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

#NEAT!
print(sub.addr, sub.joined)

# Supports most tuple operations

addr, joined = sub

print(addr, joined)

