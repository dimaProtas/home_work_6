import sys

with open('bakery.csv', 'a', encoding='utf-8') as f:
    price = sys.argv[1]
    print(price, file=f)








