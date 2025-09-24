'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

'''
haystack = "sadbutsad"
needle = "sad"

if haystack.find(needle) != -1:
    print(haystack.find(needle))
else:
    print(-1)

'''
# i have learned how to find the index of the first occurrence of a substring in a string using the find() method. …
# The find() method returns the lowest index of the substring if it is found in the string. If it is not found, it returns -1.
'''
