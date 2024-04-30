print("Welcome to Tip Calculator!")

bill = input("What was the total bill? ")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

tip_amount = float(bill) * (int(tip) / 100)
bill_per_person = round((float(bill) + tip_amount) / int(people), 2)

print(f"Each person should pay: {bill_per_person}")