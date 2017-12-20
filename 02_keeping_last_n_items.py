from collections import deque

# maxlen is the size of the deque. oldest item automatically removed
# when size > maxlen
# deque is double ended
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
q.appendleft(5)
print(q)

# deque without maxlen has no maxlen. Duh!
q = deque()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.pop()
q.popleft()
print(q)

# NOTE: Inserting or removing items from the beginning of
#       a list has O(N) complexity while deque has O(1)
#       complexity at both ends.


# Keeping history of last few items during Iteration
# If you use a list here, n number of lines will get appended
# with deque you append only the number of lines you want as specified 
# in the maxlen parameter
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == "__main__":
    with open('sample_text.txt', 'r') as f:
        for line, prevlines in search(f, 'complex'):
            for pline in prevlines:
                print(pline, end='')
            print("The line:", line, end='')
            print('-' * 20)


