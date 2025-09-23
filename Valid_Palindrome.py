'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome. '''

s = "A man, a plan, a canal: Panama"
cleaned = ''.join(char.lower() for char in s if char.isalnum()) 
print(cleaned == cleaned[::-1])

char = [] #`list` to store alphanumeric characters
for i in s: #iterate through each character in the string
    # print(i)
    if i.isalnum(): #check if the character is alphanumeric
        # print(i)
        char.append(i.lower()) #`append` the lowercase version of the character to the list
        # print(char)
print(char == char[::-1])
print(char)
print(''.join(char) == ''.join(char[::-1])) #join the list into a string and compare it with its reverse
print(''.join(char)) #join the list into a string and compare it with its reverse 

# ''.join(char) converts the list of characters back into a single string.
'''
-> in this problem i have learned how to check if a string is a palindrome by removing non-alphanumeric characters and ignoring case sensitivity.
-> i have learned different inner functions like isalnum(), lower(), join(),append() and slicing for reversing a string
-> isalnum() checks if a character is alphanumeric (a letter or a digit).
-> lower() converts a character to lowercase.
-> join() joins a list of characters into a single string.
-> append() appends a character to a list.
-> slicing is used to reverse a string.
'''