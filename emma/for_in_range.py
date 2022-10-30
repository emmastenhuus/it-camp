number = int(input("Choose a number: "))
the_sum = 0

for i in range(number,0,-1):
    the_sum = the_sum + i

print(f"The sum is {the_sum}.")


x = int(input("Choose a number: "))

for i in range(1,11):
    print(x * i)