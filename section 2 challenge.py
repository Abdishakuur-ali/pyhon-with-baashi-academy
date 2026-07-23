
# # # Challenge 1: Can You Vote?

age= int (input("Age:"))

if age >= 18:
    print(f"Age: You can vote")
else:
     print(f"You can't vote yet. 3 more years !")

# # Challenge 2: Ticket Price

age= int(input("Age :"))
if age <12:
     print("Ticket: $5")
elif age <=17:
      print("Ticket: $8")
else:
        print("Ticket: $12")

# Challenge 3: Parking Fee

hours= int (input("How many hours they parked: "))
if hours == 1:
 print("fee: $5")
elif hours <=3:
     print("fee: $10")
else:
     print("fee: $20")

# # Challenge 4: Speed Check

speed_limit = int(input("Speed limit: "))
your_speed = int(input("Your speed: "))

if your_speed > speed_limit:
    over = your_speed - speed_limit
    fine = (over // 10) * 50

    print(f"Over by: {over} km/h")
    print(f"Fine: ${fine}")
else:
    print("No fine.")

# # Challenge 5: Countdown

start = int(input("Start: "))

for i in range(start, 0, -1):
    print(i)

print("Go!")


# # Challenge 6: Grade Checker


score= int (input("Enter your score: "))

if score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("c")
elif score>=60:
    print("D")
else:
    print("f")

# # Challenge 7: Even or Odd

number = int(input("Number: "))
if number % 2 == 0:
    print(F" {number} is even ")
else:
    print(f"{number} is odd ")
    print("\nEven numbers:", end=" ")


for i in range(2, number + 1, 2):
    if i == number or i + 2 > number:
        print(i)
    else:
        print(i, end=", ")


# # Challenge 8: Discount Day

day = input("Day: ")
price = float(input("Price: $"))

if day == "monday" or day == "friday":
    discount = 20
elif day == "wednesday":
    discount = 10
else:
    discount = 0

final_price = price - (price * discount / 100)

print(f"Discount: {discount}%")
print(f"Final: ${final_price}")


# Challenge 9: Star Printer

number = int(input("Number: "))
print("*" * number)


# # Challenge 10: Flight Check-in

name = (input("Name: "))
age = int(input("Age: "))
bag_weight = float(input("bag-weight: "))

if age >= 18 and bag_weight < 23:
    print("=======================")
    print("   BOARDING PASS")
    print("========================")
    print(f"Passenger: {name.upper()}")
    print("Status: Checked in")
    print("========================")

else:
    if age < 18:
        print("You must be 18 or older to fly alone.")

    if bag_weight >= 23:
        print("Bag weight must be under 23 kg.")



