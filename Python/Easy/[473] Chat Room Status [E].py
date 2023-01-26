"""
##Chat Room Status

Write a function that returns the number of users in a chatroom based on the following rules:

For example, if there are 5 users, return:
___
"user1, user2 and 3 more online"
_____



[Examples]

___
chatroom_status([]) ➞ "no one online"

chatroom_status(["paRIE_to"]) ➞ "paRIE_to online"

chatroom_status(["s234f", "mailbox2"]) ➞ "s234f and mailbox2 online"

chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])
➞ "pap_ier44, townieBOY and 4 more online"
_____



[Notes]

N/A


[arrays] [control_flow]



-------------------------------------------------------------------
[Resources]
_________
Splitting, Concatenating, and Joining Strings in Python
https://realpython.com/python-string-split-concatenate-join/#concatenating-and-joining-strings
In this beginner-friendly article, you’ll learn some of the most fundamental string operations: splitting, concatenating, and joining. Not only will you learn how to us …
_________
_________
format() Method
https://www.geeksforgeeks.org/python-format-function/
One of the string formatting methods in Python3, which allows multiple substitutions and value formatting. This method lets us concatenate elements within a string thro …
_________
"""
# Your code should go here:

# We can solve it using two methods.
# 1. Match case.
# 2. If else.

def chatroomStatus(list1):
    if len(list1) == 0:
        return "No one online."
    if len(list1) == 1:
        return "{} online".format(list1[0])
    if len(list1) == 2:
        return "{0} and {1} online.".format(list[0], list[1])
    if len(list1) > 2:
        return "{0} and {1} and {} others online.".format(list[0], list[1], (len(list1)) - 2)


def chatroomStatusMatch(list1):
    match (len(list1)):
        case 0:
            return "No one online."
        case 1:
            return "{} online".format(list1[0])
        case 2:
            return "{0} and {1} online.".format(list[0], list[1])
        case # More then 2 then what to do about it?
