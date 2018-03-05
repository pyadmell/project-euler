# by Peyman Yadmellat
#=============================
# This program finds the difference between the sum of the squares of the first X natural numbers and the square of the sum.

# Example
# The sum of the squares of the first ten natural numbers is,
#  1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#   (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# =============================

X = 100000

# Method 1

sqrd_of_sum = reduce(lambda x, y: x + y, range(1,X+1)) ** 2
sqrd_lst = map(lambda x: x ** 2, range(1,X+1))
sum_of_sqrd = reduce(lambda x, y: x + y, sqrd_lst)

print abs(sum_of_sqrd - sqrd_of_sum)


# Method 2
# sum of numbers from 1 to X equals to X(1+X)/2
# sum of squared numbers from 1 to X equals to (2X+1)(X+1)X/6

sq_sum = ( X * (1+X) / 2 ) ** 2
sum_sq = ( 2 * X + 1 ) * ( X + 1 ) * X / 6
print abs(sq_sum - sum_sq)
    