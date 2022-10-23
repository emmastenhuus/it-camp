print("Hej, hvad hedder du?")
navn = input()
print(f"Hej med dig {navn}")

print("Hvor gammel er du?")
alder = int(input())

if alder < 15:
    print(alder, "år, du er da godt nok ung.")
    print("Du må hellere vente til næste år med at deltage")
elif alder > 25:
    print(alder, "år. Gamle jas.")
else:
    print(alder, "år, det er perfekt!")
    

