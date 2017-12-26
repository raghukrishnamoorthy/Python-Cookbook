# split() method does not allow for multiple delimiters.
# use the re.split method

import re

line = 'asdf fjdk; afed, fjek,asdf,    foo'
print(re.split(r'[;\s]\s*', line))

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

#reform the original line 
reformed_string = ''.join(v+d for v,d in zip(values, delimiters))
print(reformed_string)