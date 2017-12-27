text = 'yeah, but no, but yeah, but no, but yeah'

print(text == 'yeah')

print(text.startswith('yeah'))

print(text.endswith('no'))

print(text.find('no'))

# For complicated matching use regex

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

if re.match(r'\d+/\d+/\d+', text1):
    print('yes', text1)
else:
    print('no')

# If you are going to perform a lot of matches then precompile
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text):
    print('yes', text)
else:
    print('no', text)

# match always finds only start of string. use findall for all occurences

text = 'Today is 11/27/2012. PyCon starts 3/13/2013'
datepat.findall(text)

