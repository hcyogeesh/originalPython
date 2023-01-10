"""
##Find the Odd Integer

Create a function that takes a list and finds the integer which appears an odd number of times.


[Examples]

___
find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1

find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5

find_odd([10]) ➞ 10
_____



[Notes]

There will always only be one integer that appears an odd number of times.


[arrays] [bit_operations] [loops] [math]



-------------------------------------------------------------------
[Resources]
_________
count() Method
https://www.programiz.com/python-programming/methods/list/count
Returns the number of occurrences of an element in a list.
_________
_________
Find the Number Occurring Odd Number of Times
https://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/
Given an array of positive integers. All numbers occur even number of times except one number which occurs odd number of times. Find the number in O(n) time & constant …
_________
_________
if/else in Python's list comprehension?
https://stackoverflow.com/questions/4260280/if-else-in-pythons-list-comprehension
How can I do the following in Python? row = [unicode(x.strip()) for x in row if x is not None else ''] Essentially: replace all the Nones with empty strings, and then …
_________
_________
How can I count the occurrences of a list item?
https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
Discussions on how to count occurrences in a list without using count() method.
_________
"""
# Your code should go here:

def oddCountIndex(list1):
    uniquieList1 = list(set(list1))
    print(uniquieList1, "unique list print:")
    appended = [] #If dictionary is used then it will good, right?
    for i in uniquieList1:
        if i in list1:
            count = list1.count(i)
            appended.append(count)
    print(appended, "appended print")
    finalAppend = []
    for i in appended:
        if i % 2 == 1:
            finalAppend.append(i) # From here everything is good. # Plan is to point the index in appended and then unique list and thus print out the integer.
    finalAppend1 = int("".join(finalAppend))
    print(type(finalAppend1))
    indexation = appended.index(finalAppend1)
    print(indexation, "indexation check it, of counts")
    return finalAppend, "finalappend print"

print(oddCountIndex([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
print(oddCountIndex([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]))
print(oddCountIndex([10]))
# find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) ➞ -1
#
#
# find_odd([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) ➞ 5
#
# find_odd([10]) ➞ 10
# _____
#
#
#
# [Notes]
#
# There will always only be one integer that appears an odd number of times.
#
# INCOMPLETE
