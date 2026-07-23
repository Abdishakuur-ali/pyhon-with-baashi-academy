# challenge phase three

# Challenge 1: Say Hello

# def say_hello():
#     print(f"hello ,world !" )

# say_hello()
# say_hello()
# say_hello()

# Challenge 2: Say Hello

# def welcome(name):
#   print(f"welcome to baashi academy, {name }")
# welcome("Ahmed!")
# welcome("hodan!")
# welcome("faarah!")

# Challenge 3: Full Name

# def full_name(first, last):
#     print(f"{first.upper()} {last.upper()}")

# full_name("ahmed","yuusuf")
# full_name("hodan", "bile")
# full_name("nimco","faarah")

#   Challenge 4: Double It
# def double(number):
#     print(number * 2)

# double(5)
# double(10)
# double(25)

# Challenge 5: Ticket Price

# def ticket_price(age):

#     if age <12:
#         return 5
#     elif age <=17:
#         return 8
#     else:
#       return 12

# print(f"Age 10: ${ticket_price(10)}")
# print(f"Age 15: ${ticket_price(15)}")
# print(f"Age 25: ${ticket_price(25)}")

# Challenge 6: Area Calculator

# def area(length, width):

#     return length * width


# print(f"Room 1: {area(5, 4)}")
# print(f"Room 2: {area(10, 3)}")

# Challenge 7: Is Adult


# def is_adult(age):
#   if age >=18:
#     return True
#   else:
#      return False


# print(f"12: {is_adult(12)}")
# print(f"18: {is_adult(20)}")
# print(f"25: {is_adult(25)}")

# Challenge 8: Delivery Fee

# def delivery_fee(order_total):
#       if order_total > 50:
#          return 0
#       elif order_total <=50:
#          return 10
# fee = delivery_fee(35)
# print(f"order: $35 -fee: ${fee} - Total: ${35 + fee}")
# fee = delivery_fee(60)
# print(f"order: $60 -fee: ${fee} - Total: ${60 + fee}")
# fee = delivery_fee(48)
# print(f"order: $48 -fee: ${fee} - Total: ${48 + fee}")


# Challenge 9: Greeting Card

# def greeting(name, message):

#     print("=============================")
#     print(f"TO: {name}")
#     print(f"message: {message}")
#     print("================================")


# greeting(f"Ahmed", "Happy brithday !")
# greeting(f"Hodan" , "congratulation !")


# Challenge 10: Receipt Printer

# Function to calculate the subtotal
def subtotal(price, qty):

    # Return price multiplied by quantity
    return price * qty


# Function to calculate 10% tax
def tax(amount):

    # Return 10% of the subtotal
    return amount * 0.10


# Function to print the receipt
def print_receipt(item, price, qty):

    # Calculate subtotal
    sub = subtotal(price, qty)

    # Calculate tax
    tax_amount = tax(sub)

    # Calculate total
    total = sub + tax_amount

    print("========================")
    print("       RECEIPT")
    print("========================")
    print(f"Item: {item}")
    print(f"Qty: {qty}")
    print(f"Subtotal: ${sub}")
    print(f"Tax: ${tax_amount}")
    print(f"Total: ${total}")
    print("========================")


print_receipt("Pizza", 10, 3)
