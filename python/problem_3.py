# This program finds the largest prime factor of a number

# Example
# The prime factors of 13195 are 5, 7, 13 and 29.
# The largest prime factors of 600851475143 is 6857.

num = 600851475143 # a number to find its largest prime factors

# Finding the largest prime factor
while (num % 2 == 0):
    num /= 2
    print num

p = 3   
while (p <= (num//2)):
    while ( (num % p) == 0):
        num /= p
    
    p += 2

if (num == 1):
    print 2
else:
    print num



    
    