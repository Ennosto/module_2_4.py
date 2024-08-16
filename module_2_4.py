numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
num = 0
prime = []
not_prime = []
i = 0
for i in range(len(numbers)):
    is_prime = True
    num = numbers[i]
    if num < 2:
        continue
    else:
        for a in range(2, int((num ** (1 / 2)) + 1)):
            if num % a == 0:
                is_prime = False
                break
        if not (is_prime):
            not_prime.append(num)
        else:
            prime.append(num)
            is_prime = True
print(prime)
print(not_prime)