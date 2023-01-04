"""
##Vowel Replacer

Create a function that replaces all the vowels in a string with a specified character.


[Examples]

___
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"

replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"

replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
_____



[Notes]

All characters will be in lower case.


[regex] [strings] 



-------------------------------------------------------------------
[Resources]
_________
Python RegEx (With Examples)
https://www.programiz.com/python-programming/regex
In this tutorial, you will learn about regular expressions (RegEx), and use Python's re module to work with RegEx (with the help of examples).
_________
_________
join() Method
https://www.programiz.com/python-programming/methods/string/join
Provides a flexible way to create strings from iterable objects. It joins each element of an iterable (such as list, string and tuple) by a string separator (the string …
_________
_________
String replace() Method
https://www.w3schools.com/python/ref_string_replace.asp
Replaces a specified phrase with another specified phrase.
_________
""" 
# Your code should go here:

def replaceVowels(str1, replacer1):
    vowelStr = "aeiou"
    word = []
    for i in str1:
        if i.lower() in vowelStr:
            word.append(replacer1)
        else:
            word.append(i)
    return ("".join(word))

print(replaceVowels("the aardvark","#"))
print(replaceVowels("minnie mouse","?"))
print(replaceVowels("shakesapeare","*"))

# The program is complete.