'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Example 3:

Input: strs = [""]
Output: ""

'''

strs = ["flower","flowx","floght"]
# print(strs)

if not strs:
    print("")

strs.sort() # sorting list of string 
# print(strs)

first, last = strs[0],strs[-1] # taking first and last element of list beacuse it already sorted
# print(first,last)

i=0
while i < len(first) and i  <len(last) and first[i] == last[i]: #checking match indexs with i
    i+=1
print(first[:i]) # printing a string with last match index with help of i

'''
-> In this problem i have learned how to find longest common prefix of a given List of string
-> I have learnt new method called sort() with will help in ordering elements in a list 
-> I have learnt how while loop works and condotional handaling
'''