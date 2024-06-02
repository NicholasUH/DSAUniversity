'''
Problem:
Given a string s, find the length of the longest substring without repeating characters.
'''

'''
Logic:
To find the longest substring, we can utilize a sliding window approach and hashsets. The sliding window will encase the current substring,
while the hashset will hold the characters of the current substring. We will have a left and right pointer, both start at index 0.
We will iterate the right pointer to the end and add each new character to the hashset and update the length if a new longest substring is found.
If a repeating value is found, we will remove all characters from the left pointer up to the repeating value and update the left pointer.
Removing all characters is necessary as we consider continuous characters for the substring.
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