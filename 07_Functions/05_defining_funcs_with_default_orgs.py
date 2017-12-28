# Default arguments should appear last
def spam(a, b=42):
    print(a, b)

spam(1)
spam(1, 2)

# If the default value is a mutable container, use None
def spam2(a, b=None):
    if b is None:
        b = []

# Check if optional argument was given interesting value or not
_no_value = object()

def spam(a, b=_no_value):
    if b is _no_value:
        print("No value was given for b")

