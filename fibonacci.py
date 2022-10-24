list_of_fib = []

x = 0
y = 1
z = 0

for i in range(17):
    list_of_fib.append(x)
    z = x + y
    x = y
    y = z
    

print(list_of_fib)