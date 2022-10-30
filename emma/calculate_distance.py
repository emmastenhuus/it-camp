from math import sqrt

x1, y1 = map(int, input().split(","))
x2, y2 = map(int, input().split(","))

distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print(f"The distance between ({x1},{y1}) and ({x2},{y2}) is {distance}.")