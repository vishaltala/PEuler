i = 2520

while True:
    if all(map(lambda d: i%d == 0, range(11,21))):
        print(i)
        break
    i += 20
