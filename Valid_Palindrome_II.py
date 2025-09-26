'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
'''
s = "ammay"

def is_palindrome_range(left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

left, right = 0, len(s) - 1
while left < right:
    if s[left] != s[right]:
        # must RETURN the result here
        print(is_palindrome_range(left + 1, right) or
              is_palindrome_range(left, right - 1))
        break
    left += 1
    right -= 1
else:
    # executes if loop completes with no break (already palindrome)
    print(True)

