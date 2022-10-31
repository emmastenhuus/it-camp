def converter(phone):
    numbers = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four"
    }
    output = ""
    for number in phone:
        output += numbers.get(number, "!") + " "
    return output


phone = input("Phone: ")
print(f"Your phone number is: {converter(phone)}")