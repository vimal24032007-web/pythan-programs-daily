low, high = 2, 10
primes = []

for i in range(low, high + 1):
    if i < 2:
        continue
    
    flag = 0
    for x in range(2, int(i**0.5) + 1):
        if i % x == 0:
            flag = 1
            break
            
    if flag == 0:
        primes.append(i)

print(primes)
