"""
##Sum of Evenly Divisible Numbers from a Range

Create a function that takes three arguments a, b, c and returns the sum of the
numbers that are evenly divided by c from the range a, b inclusive.


[Examples]

___
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.

evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30

evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
_____



[Notes]

Return 0 if there is no number between a and b that can be evenly divided by c.


[math] [numbers] 



-------------------------------------------------------------------
[Resources]
_________
sum() Method
https://www.geeksforgeeks.org/sum-function-python/
Sum of numbers in the list is required everywhere. Python provide an inbuilt function sum() which sums up the numbers in the list.
_________
_________
Python For Loops
https://www.w3schools.com/python/python_for_loops.asp
Used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
_________
_________
range() Method
https://www.w3schools.com/python/ref_func_range.asp
Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
_________
_________
Modulo Operator
https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python/
Finds the remainder or signed remainder after the division of one number by another (called the modulus of the operation).
_________
""" 
# Your code should go here:

def evenDiv(start, end, divider):
    sumList = []
    for i in range(start-1, end+1, divider):
        if i % divider == 0:
            # print(float(i)) # To test the program outputs.
            sumList.append(i)
        else:
            pass
    return sum(sumList)

print(evenDiv(1,10,20)) # Some kind of modulo I have to use, for sure.
print(evenDiv(1, 10, 2))
print(evenDiv(1, 10, 3))
print(evenDiv(1,100,20))
print(evenDiv(1,100,50))
print(evenDiv(1,100,25))

# The program is complete.