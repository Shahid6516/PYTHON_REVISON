age = int(input("Please input your age: "))
day = "Wednesday"

# if age >= 18:
#     print("$12 for the adult")
# else:
#     print("$8 for the chidren")


price = 12 if age >= 18 else 8 
# print(price)
if day == "Wednesday":
    # price= price - 2
    price-=2

print(price)