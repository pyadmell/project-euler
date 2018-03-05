# by Peyman Yadmellat
#=============================
# This program finds the X-th prime number.

# Example
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# Fact:
# The only even prime number is 2.
# =============================

X= 1000*4.5

prime_lst = [2,3]
tmp = prime_lst[-1]

while len(prime_lst) < X:
    module = 1
    tmp += 2
    if tmp > 5 and tmp % 5 == 0:
        tmp +=2
    i= 1
    while module > 0 and prime_lst[i] <= tmp ** 0.5:
        module *= tmp % prime_lst[i]
        i += 1
    
    if module != 0:
        prime_lst.append(tmp)
        
        
       
print(prime_lst[-1])           
    