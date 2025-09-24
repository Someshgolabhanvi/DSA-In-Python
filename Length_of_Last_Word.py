"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""
s = "Hello World"
words = s.split() #split the string into words
last_word = words[-1] #get the last word
print(len(last_word))

'''
-> in this problem i have learned how to find the length of the last word in a string by splitting the string into words using the split() method and then getting the last word using indexing.
-> The split() method splits a string into a list of words based on whitespace by default.  
-> Indexing is used to access the last word in the list of words.
'''