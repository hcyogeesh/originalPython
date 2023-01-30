"""
##Western Showdown

Wild Roger is participating in a Western Showdown, meaning he has to draw (pull out and shoot).
his gun faster than his opponent in a gun standoff.
Given two strings,p1 and p2, return which person drew their gun the fastest.
If both are drawn at the same time, return "tie".


[Examples]

___
showdown(
  "   Bang!        ",
  "        Bang!   "
) ➞ "p1"

# p1 draws his gun sooner than p2

showdown(
  "               Bang! ",
  "             Bang!   "
) ➞ "p2"

showdown(
  "     Bang!   ",
  "     Bang!   "
) ➞ "tie"
_____



[Notes]

Both strings are the same length.


[conditions] [strings]



-------------------------------------------------------------------
[Resources]
_________
find() Method
https://www.geeksforgeeks.org/string-find-python/
Returns the lowest index of the substring if it is found in given string. If its is not found then it returns -1.
_________
_________
index() Method
https://www.w3schools.com/python/ref_list_index.asp
Returns the position at the first occurrence of the specified value.
_________
"""
# Your code should go here:

def showdown(p1, p2):
    p1LowerCase = p1.lower()
    p2LowerCase = p2.lower()
    if p2LowerCase.find("bang!") < p1LowerCase.find("bang!"):
        return "p2"
    elif p1LowerCase.find("bang!") < p2LowerCase.find("bang!"):
        return "p1"
    elif p1LowerCase.find("bang!") == p2LowerCase.find("bang!"):
        return "tie"

print(showdown(
  "   Bang!        ",
  "        Bang!   "
))


print(showdown(
  "               Bang! ",
  "             Bang!   "
))

print(showdown(
  "     Bang!   ",
  "     Bang!   "
  ))

# The program is complete.
