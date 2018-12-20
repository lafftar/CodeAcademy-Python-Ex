def is_prime(x):
## Checks if x is negative, and creates range() accordingly.
    if x < 0:
        rng = range(-2, x, -1)
    else:
        rng = range(2, x)
        
## Takes care of 0, 1 and 2.
    if x in (0, 1):
        return False
    elif rng == []:
        return True
    else:
        pass
        
##Loops through the list
    for n in rng:
        print(x,n, x%n)
        if x % n == 0:
            print("It's not a prime number! Program Ending!")
            return False
    else:
        print("It's a prime number! Ooh!")
        return True

print(is_prime(-7))
