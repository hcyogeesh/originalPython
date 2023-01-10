"""
##The Reverser!

The "Reverser" takes a string as input and returns that string in reverse order, with the opposite case.


[Examples]

___
reverse("Hello World") ➞ "DLROw OLLEh"

reverse("ReVeRsE") ➞ "eSrEvEr"

reverse("Radar") ➞ "RADAr"
_____



[Notes]

There will be no punctuation in any of the test cases.


[formatting] [language_fundamentals] [strings]



-------------------------------------------------------------------
[Resources]
_________
swapcase() Method
https://www.programiz.com/python-programming/methods/string/swapcase
Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters of the given string, and returns it.
_________
_________
How to Reverse a String
https://www.w3schools.com/python/python_howto_reverse_string.asp
Learn how to reverse a string in Python.
_________
_________
swapcase() Method
https://www.geeksforgeeks.org/python-string-swapcase/
Converts all uppercase characters to lowercase and vice versa of the given string, and returns it.
_________
_________
reversed() Function
https://www.programiz.com/python-programming/methods/built-in/reversed
Returns the reversed iterator of the given sequence.
_________
"""
# Your code should go here:

#def reverseAll(str1):
#    print((reversed(str1)).swapcase())

def reverserMyWay(str1):
    def swapcaseMy(stringInput):
        a = []
        for i in range(0, len(str1)):
            b = str1[i]
            if b.isupper() == True:
                a.append(str1[i].lower())
            elif b.islower() == True:
                a.append(str1[i].upper())
            else:
                a.append(str1[i])
        reversed = a[::-1]
        for i in reversed:
            print(i, end="")
    return (str(swapcaseMy(str1)))


print(reverserMyWay("Hello World"))
print(reverserMyWay("Reverse"))
print(reverserMyWay("Radar"))
#print(reverserMyWay("Hello World"))
#print(reverseAll("Reverse"))
#print(reverseAll("Radar"))

