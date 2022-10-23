numbers = [5, 2, 3, 7, 4, 3]
numbers_2 = numbers.copy()

numbers.append(13)
print(numbers)

numbers.insert(1, 9)
print(numbers)

numbers.remove(2)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(3))

print(50 in numbers)

print(numbers.count(3))

numbers.sort()
print(numbers)

numbers.clear()
print(numbers)