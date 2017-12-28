# *args to accept any no. of arguments
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1, 2))
print(avg(1, 2, 3, 4))

# **args to accept any no. of keyword arguments

def kwargs_function(**args):
    for key, value in args.items():
        print(key, value)

kwargs_function(a=1, b=2)