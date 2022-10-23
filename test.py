import png
import random

BLACK = 0
WHITE = 255

WIDTH = 1400
HEIGHT = 700

def calc1(x, prev):
    p0 = prev[x - 1]
    p1 = prev[x]
    p2 = prev[x + 1]
    return int((p0 + 4 * p1 + p2) / 6)

def torulearray(r): # r is between 0 and 255
    arr = []

    if r >= 128:
        arr.append(BLACK)
    else:
        arr.append(WHITE)
    r = r % 128

    if r >= 64:
        arr.append(BLACK)
    else:
        arr.append(WHITE)
    r = r % 64
    
    if r >= 32:
        arr.append(BLACK)
    else:
        arr.append(WHITE)
    r = r % 32
    
    if r >= 16:
        arr.append(BLACK)
    else:
        arr.append(WHITE)
    r = r % 16
    
    if r >= 8:
        arr.append(BLACK)
    else:
        arr.append(WHITE)
    r = r % 8
    
    if r >= 4:
        arr.append(BLACK)
    else:
        arr.append(WHITE)
    r = r % 4
    
    if r >= 2:
        arr.append(BLACK)
    else:
        arr.append(WHITE)
    r = r % 2

    if r >= 1:
        arr.append(BLACK)
    else:
        arr.append(WHITE)

    return arr

def calc2(x, prev, rulearray):
    p4 = 0 if prev[x - 1] == BLACK else 4
    p2 = 0 if prev[x] == BLACK else 2
    p1 = 0 if prev[x + 1] == BLACK else 1
    p = p4 + p2 + p1
    return rulearray[p]

#rule = 30 # Rule number (between 0 and 255)

for rule in range(256):
    rulearray = torulearray(rule)
    img = []

    for y in range(HEIGHT):
        row = []
        if y == 0:
            for x in range(WIDTH):
                mid = int(WIDTH / 2)
                if x - 1 == mid or x + 1 == mid:
#                if x == mid:
#                if x % 2 == 1:
                    row.append(BLACK)
                else:
                    row.append(WHITE)
        else:
            for x in range(WIDTH):
                if x == 0 or x == WIDTH - 1:
                    row.append(WHITE)
                else:
                    row.append(calc2(x, img[y - 1], rulearray))
        img.append(row)

    with open('yrule' + str(rule) + '.png', 'wb') as f:
        w = png.Writer(WIDTH, HEIGHT, greyscale=True)
        w.write(f, img)
