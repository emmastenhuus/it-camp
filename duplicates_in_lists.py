numbers = [11, 3, 5, 1, 3, 2, 7, 7, 4, 9, 11, 10]
for number in numbers:
    x_count = numbers.count(number)
    if x_count > 1:
        numbers.remove(number)
print(numbers)


ciphers = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for cipher in ciphers:
    if cipher not in uniques:
        uniques.append(cipher)
print(uniques)