# im using every challeng comment


# challenge one Grocery Run

budget = 200

rice = 25
chicken = 40
bread = 8
milk = 6

# total
total = rice + chicken + bread + milk
change = budget - total
print(f"Total: ${total}")
print(f"budget: ${budget}")
print(f"change: ${change}")

# challenge 2 gym membership
fee = 50
money = 320

months = money // fee
Remaining = money % fee
print(f"months: {months}")
print(f"Remaining: {Remaining}")

# Challenge 3: Flight Booking

flight = 500

fee = flight * 10 / 100
total = flight + fee
print(f"flight: $ {flight}")
print(f"fee: $", int(fee))
print(f"Total: $", int(total))

# challenge 4 greeting car

name= input("Enter your name: ")
freind= input("Enter your name: ")
message= "wishing the best !"

print(f"To: {name}")
print(f"from: {freind.upper()}")
print(f"message: {message}")

# challenge 5  Name tag
full_name = input("Enter your full-name: ")
print(f"upper: {full_name.upper()}")
print(f"lower: {full_name.lower()}")
print(f"Letters: {len(full_name.replace(" ", ""))}")
print(f"first: {full_name[0].upper()}")
print(f"last:  {full_name[-1]}")

# challenge 6 pizza split
total_bill = float(input("Total bill:"))
Friends = int(input("Friends:"))
each_pays = round(total_bill / Friends, 2)
print(f"Each pays:  ${each_pays}")

# Challenge 7: Username Generator
first_name = input("Enter your first-name: ")
birth_year = input("Enter your birth_year:")
username = "abdi".lower()
print(f"Name: {first_name}")
print(f"Year: {birth_year}")
print(f"username: {username}{birth_year}")

#  Challenge 8: Coffee Receipt
name = input("Enter your name: ")
coffees = int(input("How many coffee: "))

price = 5
total = coffees * price

print(f"Customer: {name.upper()}")
print(f"Coffees: {coffees}")
print(f"Total: ${total}")


# Challenge 9: Contact Card

name = input("Enter your name: ")
phone_number = int(input("Enter your phone-number: "))
Email = input("Enter your email: ")
print(f"name: {name.capitalize()}")
print(F"phone: {phone_number}")
print(f"email:  {Email} ({len(Email)} characters )")

# Challenge 10: Travel Profile

name = input("Enter your name: ")
Destination = input("Enter your destination: ")
days = int(input("Enter your days: "))
print(f"Travel: {name.upper()}")
print(f"destination: {Destination.capitalize()}")
print(f"days: {days}")
print(f"Note: {name} is spending {days} days in {Destination}.Bon voyage! ")
