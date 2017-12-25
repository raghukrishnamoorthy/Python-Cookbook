# Sort objects of the same class that does not support 
# native comparison

class User():
    
    def __init__(self, user_id):
        self.user_id = user_id
    
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(42), User(31), User(99)]
print(sorted(users, key=lambda u: u.user_id))

# use attrgetter. using lambda or attrgetter is personal preference but
# attrgetter is a bit faster.

from operator import attrgetter

print(sorted(users, key=attrgetter("user_id")))

# multiple keys allowed print(sorted(users, key=attrgetter("user_id", "last_name")))

# Can also be used for min and max operations
print(min(users, key=attrgetter("user_id")))
print(max(users, key=attrgetter("user_id")))


