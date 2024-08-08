numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(0, len(numbers)):
    current = numbers[i]
    is_prime = True
    if current == 1:
        continue
    for j in range(2, current):
        if current % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(current)
    else:
        not_primes.append(current)
print('Prime:', primes)
print('Not_prime:', not_primes)


