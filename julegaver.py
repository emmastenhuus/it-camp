anna_gaver = int(input("Hvor mange gaver har Anna fået? "))
laura_gaver = int(input("Hvor mange gaver har Laura fået? "))
oscar_gaver = int(input("Hvor mange gaver har Oscar fået? "))
antal_sure = 0

if laura_gaver and oscar_gaver > anna_gaver:
    print("Anna er sur!")
    antal_sure = antal_sure + 1
if anna_gaver > laura_gaver:
    print("Laura er sur!")
    antal_sure = antal_sure + 1
if oscar_gaver < anna_gaver or oscar_gaver < laura_gaver:
    print("Oscar er sur!")
    antal_sure = antal_sure + 1
if antal_sure == 0:
    print("Ingen er sure.")


                 
