'''
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".


Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

'''
s    = "aaaaaaabcb"
goal = "aaaaaaacbc"

if len(s) != len(goal):
    print("False")
if s == goal:
    print(set(s))  #check if there are duplicate letters in s
    print(len(set(s))<len(s))
diffs = [(a,b) for a,b in zip(s,goal) if a != b]
print(diffs)
print(len(diffs) == 2 and diffs[0] == diffs[1][::-1])  #check if the two differences are reverses of each other

'''
-> I have learned how to determine if two strings can be made equal by swapping exactly two letters in one of the strings.
-> The approach involves checking the lengths of the strings, comparing the characters at each position, and checking if the two strings are equal.
-> The time complexity of this algorithm is O(n), where n is the length of the string.
'''