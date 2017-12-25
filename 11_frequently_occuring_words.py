words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(word_counts)
print(top_three)

# Counter is a dictionary
print(word_counts['eyes'])

# Use addition to Increment count
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1

# Or use the update method of Counter
word_counts.update(morewords)

# The Counter objects can also be manipulated using mathematical operators
a = Counter(words)
b = Counter(morewords)
c = a + b # Add Counts
print(c)
d = a - b # Subtract Counts
print(d)


