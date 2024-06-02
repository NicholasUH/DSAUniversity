'''
Problem:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

'''
Logic:
To solve this problem to check if a string is a palindrone, we can utilize the two pointer approach. We will have two pointers start and end.
We check if the letter at the start and end indices is the same and return the appropiate response. After checking the letter, we will move
the start index right to the next alpha-numeric character and the end index left to the next alpha-numeric character. We will repeat this
process until the start and end indices meet.
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
    