from sys import argv

with open('bakery.csv', 'r', encoding='utf-8') as f:
    price = len(argv)
    if price == 1:
        print(f.read())
    elif price == 2:
        for line in f.readlines()[int(argv[1]) - 1]:
            print(line, end='')
    elif price == 3:
        i = 0
        for line in f:
            i += 1
            if i >= int(argv[1]):
                if i > int(argv[2]):
                    break
                print(line, end='')
