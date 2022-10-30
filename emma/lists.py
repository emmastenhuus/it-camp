names = ["Jon","Daenerys","Robb","Ygritte","Rickon"]
print(names[2:])

def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


print(find_max([2, 3, 11, 4]))


L = [int(x) for x in input().split()]

minimum = L[0]
for i in range(len(L)):
    if minimum > L[i]:
        minimum = L[i]

print(minimum)


# How many numbers are bigger than 10?

l = [int(x) for x in input().split()]

bigger_than_10 = 0
for i in range(len(l)):
    if l[i] > 10:
        bigger_than_10 = bigger_than_10 + 1

print(bigger_than_10)

# Sum

#sum = 0
#for i in range(len(L)):
    #sum = sum + L[i]

#print(sum)

A = [5, 6, 14, 3, 1, 6]

A.sort()
print(A)