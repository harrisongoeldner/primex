p_range_low = int(input())
p_range_high = int(input())

primes = []

for i in range(p_range_low,p_range_high):
    for j in primes:
        if i%j != 0:
            primes.append(i)
            print(i)
    i = i + 1
print(primes)