# Written by Peyman Yadmellat
#=============================
# This program finds the smallest positive number that is evenly divisible (dividable with no remainder) by all of the numbers from 1 to X.

# Example
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# Idea:
# The smallest positive number should be evenly dividable to all prime numbers within range of 1 to X,
# and it should be even since it is dividable by the product of the sequence of all prime numbers <= X. 
# =============================

X = 20

def primeFndr (num):
    largest_prime = 2
    if (num > 2): 
        while (num % 2 == 0):
            num /= 2
            largest_prime = 2

        p = 3   
        while (p <= (num//2)):
            while ( (num % p) == 0):
                num /= p
    
            p += 2

        if (num != 1):
            largest_prime = num
    
    return largest_prime

def remainder(num1,num2):
    return num1 % num2

# Finding list of prime numbers in the range(1,X)
prime_lst = []
for x in range(2,X+1):
    if primeFndr(x) not in prime_lst: prime_lst.append(primeFndr(x)) 


result = reduce( (lambda x, y: x * y), prime_lst)
inc = result  # The result should be evenly dividable by the product of the prime_lst
while sum(map((lambda x: result % x),range(1,X+1))) > 0:
    result += inc
    
print result



    
    