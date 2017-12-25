from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

#NEAT!
print(sub.addr, sub.joined)

# Supports most tuple operations

addr, joined = sub

print(addr, joined)

# Named tuple is helpful in that you don't have to use indexes to access 
# fields from the database records. Example follows
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# Using the named tuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost_using_rec(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

# Tuples are immutable. Use _replace method to create a new tuple with changed value
s = Stock(name='ACME', shares=250, price=10)
s = s._replace(shares=75)
print(s)

# Another use of _replace method is to populate named tuples with
# optional or missing fields

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
    return stock_prototype._replace(**s)

a = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
d_a = dict_to_stock(a)
print(d_a)