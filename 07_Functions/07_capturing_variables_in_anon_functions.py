x = 10
a = lambda y : x + y
x = 20
b = lambda y: x + y

print(a(10)) # 30
print(b(10)) # 30

# The above result is because variables get bound at runtime and not defn time
# To capture variables at the point of defn, do this

x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y

print(a(10)) # 20
print(b(10)) # 30

funcs = [lambda x: x+n for n in range(5)]
for f in funcs:
    print(f(0))

funcs = [lambda x, n=n: x+n for n in range(5)]
for f in funcs:
    print(f(0))
 