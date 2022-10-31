course = "Python for Beginners"
print(course[0])
print(course[-2])
print(course[1:3])
print(course[1:])
print(course[:7])

another = course[:]
print(another)

name = "Jennifer"
print(name[1:-1])

# Initials program
first_name = "Emma"
middle_name = "Stenhuus"
last_name = "Andersen"

# Formatted strings:
ints = f"{first_name[0]}.{middle_name[0]}.{last_name[0]}"
msg = f"{ints} is a teacher at DTU"

print(msg)

# Functions specific to strings: "."
instrument = "Blue Trombone"

print(len(instrument)) # len is non-specific

print(instrument)
print(instrument.upper())
print(instrument.lower())
print(instrument.find("o"))
print(instrument.find("Trombone"))
print(instrument.replace("Blue", "Yellow"))

# Use of boolean
print("Blue" in instrument)

# Encryption

print(chr(0x66))

encrypt = {
    "a": "b",
    "b": "c",
    "c": "d",
}

msg = input()
enc = ""

for i in msg:
    enc += encrypt[i]

print(enc)