"""
##Card Counting (BlackJack)

In BlackJack, cards are counted with -1, 0, 1 values:
___
*) 2, 3, 4, 5, 6 are counted as +1
*) 7, 8, 9 are counted as 0
*) 10, J, Q, K, A are counted as -1
___

Create a function that counts the number and returns it from the list of cards provided.


[Examples]

___
count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1

count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6

count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5
_____



[Notes]

___
*) String inputs will always be upper case.
*) You do not need to consider case sensitivity.
*) If the argument is empty, return 0.
*) No input other than: 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A".
___



[algebra] [conditions] [games] [loops]



-------------------------------------------------------------------
[Resources]
_________
Multiple Nested Ternary Expression
https://stackoverflow.com/questions/44636514/python-multiple-nested-ternary-expression
Python multiple nested ternary expression.
_________
_________
sum() Method
https://www.programiz.com/python-programming/methods/built-in/sum
Adds the items of an iterable and returns the sum.
_________
_________
List Comprehension
https://www.programiz.com/python-programming/list-comprehension
In this article, we will learn about Python list comprehensions, and how to use it.
_________
"""
# Your code should go here:

def count(list1):
    counter  = 0
    for i in list1:
        if isinstance(i, str) == True:
            global caseInsensitive
            caseInsensitive = i.lower()
        match caseInsensitive:
            case 2 | 3 | 4 | 5 | 6 :
                counter += 1
            case 7 | 8 | 9 :
                counter += 0
            case 10 | "j" | "q" | "k" | "a":
                counter -= 1
    return counter

print(count([5, 9, 10, 3, "J", "A", 4, 8, 5]))
print(count(["A", "A", "K", "Q", "Q", "J"]))
print(count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]))

# The program is complete.
