print("Welcome to the tip calculator!")
bill = float(input("What's the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
total = tip / 100 * bill + bill
bill_per_person = total / people
print(f"Each person should pay R$ {round(bill_per_person):.2f}.")
