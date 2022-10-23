customer = {
    "name": "John Smith",
    "age": 50,
    "is_verified": True,
    "birthdate": "March 13 1972"
}
customer["name"] = "Jack Smith"
print(customer.get("name"))

age = {"Marie": 10, "Liv": 12}
age["Marie"] += 3
print(age["Marie"])

phone = input("Phone: ")
numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for number in phone:
    output += numbers.get(number, "!") + " "
print(output)