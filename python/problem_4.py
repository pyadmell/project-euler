# Written by Peyman Yadmellat
#=============================
# This program finds the largest palindrome made from the product of two 3-digit numbers.

# Example
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#=============================

var1 = 999
var2 = var1
rng = 900
palindrome_lst = []
while not palindrome_lst:
    while var2 >= rng:
        while var1 >= rng:
            num = var1 * var2
            var1 -= 1
            lst = map(int, str(num))
            if lst == lst[::-1]:
                palindrome_lst.append(num)
            
        var2 -= 1
        var1 = var2
        
    rng -= 100
    var1 = 999
    var2 = var1

print max(palindrome_lst)
print palindrome_lst



    
    