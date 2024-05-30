'''
Problem:
Given a string s, find the length of the longest substring without repeating characters.
'''

'''
Logic:
create a set to store the letters in the current substring
Iterate the right pointer to the end
-check if letter is a repeat by checking the set
-if seen, remove that letter and the ones before it, and iterate the left pointer
add the letter to the set and update the max length
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left, length = 0, 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            
            charSet.add(s[right])
            length = max(length, right - left + 1)
        
        return length