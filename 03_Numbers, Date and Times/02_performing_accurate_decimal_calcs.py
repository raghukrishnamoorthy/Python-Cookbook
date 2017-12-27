# floating point numbers don't give expected result

a = 4.2
b = 2.1
print(a + b)

# use decimal for higher accuracy

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
c = a + b
print(c)

# localcontext controls rounding and number of digits
from decimal import localcontext
with localcontext() as ctx:   
    ctx.prec = 3
    print(a / b)


