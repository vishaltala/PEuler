a = 0
b = 1
fib = 0
sum = 0

while fib < 4000000:
    fib = a + b
    a = b
    b = fib
    if fib % 2 == 0:
        sum = fib + sum

print (sum)
