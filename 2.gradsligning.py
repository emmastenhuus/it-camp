from math import sqrt

a = int(input("Vælg a-værdi: "))
b = int(input("Vælg b-værdi: "))
c = int(input("Vælg c-værdi: "))

d = b * b - 4 * a * c

if d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(f"Svaret er {x1} og {x2}")
elif d == 0:
    x1 = (-b) / (2 * a)
    print(f"Svaret er {x1}")
else:
    print("Der er intet svar")
    
    
