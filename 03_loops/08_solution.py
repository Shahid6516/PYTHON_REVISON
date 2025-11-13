# prime number -  a whole number greater than 1 that cannot be exactly divided by any whole number other than it 
#  example 2 3,5,7,11


number = 29
isPrime = True

if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            isPrime=False 
            break

print(isPrime)


    
