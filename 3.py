sum1 = 0
#sum1 is sum of the squares of the first one hundred natural numbers

a = 0

for i in range(101):
    sum1 = (i*i) + sum1 

for i in range(101):
    a = i + a 
sum2 = (a*a)
#sum2 is square of the sum of the first one hundred natural numbers

diff = sum2 - sum1

print(diff)
