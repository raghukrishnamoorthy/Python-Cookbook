filename = 'spam.txt'

print(filename.endswith('.txt'))
print(filename.startswith('file:'))

#for multiple choices, use a tuple
filenames = ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
myFiles = [name for name in filenames if name.endswith(('.c', '.h'))]
print(myFiles)

print(any(name.endswith('.py') for name in filenames))

#Example to read web urls
from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

#startswith combined with Data Reductions
import os
print(os.listdir(os.getcwd()))
if any(name.endswith((".c", ".h")) for name in os.listdir(os.getcwd())):
    print(True)
else:
    print(False)