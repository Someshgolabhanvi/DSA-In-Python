'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

'''
s = "IceCreAm"
vowels = set("aeiouAEIOU")  
chars = list(s)
left,right = 0,len(chars) - 1

while left < right:
    if chars[left] not in vowels:
        left += 1
    elif chars[right] not in vowels:
        right -= 1
    else:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
print("".join(chars))

'''
-> I have learned how to reverse only the vowels in a string using the two-pointer technique.   
-> The two-pointer technique involves using two pointers, one starting from the beginning of the string and the other from the end, and moving them towards each other while swapping the vowels they encounter.   
-> The time complexity of this algorithm is O(n), where n is the length of the string.
'''
