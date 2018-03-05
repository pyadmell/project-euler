# This program finds the sum of all the multiples of 3 or 5 below 1000.

# Example:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.


max_range = 1000 #maximum range

#Finding all multiples of 3 and 5
summation = 0 # The sume variable
i = 3 
while (i < max_range):
    if ( (i % 3) == 0 ) or ( (i % 5) == 0 ):
        summation += i
    
    i += 1
    

print summation

    
    