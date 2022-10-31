weight = int(input("Weight: "))
lbs_or_kg = input("Lbs or kg: ")

if lbs_or_kg.upper == "LBS":
    converted = weight * 0.45
    print(f"You weigh {converted} kilos")
else:
    converted = weight / 0.45
    print(f"You weigh {converted} pounds")