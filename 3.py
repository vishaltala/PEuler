def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            #`n % i` is effectively the opposite of `n % i ==0`.
            i += 1
        else:
            n //= i
    return n

print(largest_prime_factor(600851475143))