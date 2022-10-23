# temperature
temperature = 25

if temperature >= 30:
    print("It's a hot day")
elif temperature < 10:
    print("It's a cold day")
elif temperature == 25:
    print("It's a perfect day")
else:
    print("It's neither a hot nor a cold day")


# naming
name = "Liva"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can have a maximum of 50 characters")
else:
    print("Name looks good!")