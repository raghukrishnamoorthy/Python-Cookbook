prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

#ZIP CREATES AN ITERATOR THAT CAN BE USED ONLY ONCE!!!!

min_price = min(zip(prices.values(), prices.keys()))

max_price = max(zip(prices.values(), prices.keys()))


prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

#In case of Duplicate values, min, max or sorted will operate on the Key

prices = {'AAA': 45.23, 'ZZZ': 45.23}

print(min(zip(prices.values(), prices.keys())))