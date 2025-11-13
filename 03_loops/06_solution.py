# factorial of 5 = 5*4*3*2*1 = 120
# factorial of 6 = 6*5*4*3*2*1 = 720

# Problem: Compute the factorial of a number using a while loop.

number = 5
factorial = 1

while number > 0:
    # factorial = factorial*number 
    factorial *= number
    number -= 1

print("Factorial value of number is:",factorial)


