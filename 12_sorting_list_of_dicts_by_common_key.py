rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# Sort the dictionaries by using operator module's itemgetter
from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print("-" * 50)
print(rows_by_uid)
print("-" * 50)
#Using multiple keys
rows_by_lnamefname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lnamefname)

# Lambda expressions can also be used but are slower than itemgetter
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_fname_lname = sorted(rows, key=lambda r: (r['fname'], r['lname']))

# Can be used for min and max functions too
print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))

