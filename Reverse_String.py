'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

'''
s = ["h","e","l","l","o"]
print(len(s)) #print the length of the list

print(s.reverse()) #inbuilt function to reverse a list
print(s) #print the reversed list

'''
# i have learned how to reverse a list in python using the reverse() method.
# The reverse() method reverses the elements of the list in place, meaning it modifies the original list and does not return a new list.
# The time complexity of the reverse() method is O(n), where n is the number of elements in the list.
# The space complexity of the reverse() method is O(1), as it does not use any extra space.'''