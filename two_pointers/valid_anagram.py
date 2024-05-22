'''
Have 2 pointers, ones starts at the beginning and one at the end.
Keep iterating while the start is less than the end pointer
On each iteration, iterate the start right and end left until both are on alnumeric characters
Check if the character at both pointers are equal, return False if they are not, else iterate to next character for next iteration.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start <= end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            
            if s[start].lower() != s[end].lower():
                return False
            
            start += 1
            end -= 1
        
        return True