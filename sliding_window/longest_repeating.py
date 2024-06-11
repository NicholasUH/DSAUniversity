'''
Problem:
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

'''
Logic:
The solution behind finding the length of the substring involves using a dictionary and the sliding window approach.
The dictionary will be used to store the count of each character of the sliding window at any given point. The bounds
of the sliding window will represent the current substring that is being considered. We will also keep track of the frequency
of the most frequent character in the sliding window. This will help us figure out if we have enough replacements to continue
the substring. At each iteration, we will update the dictionary counts and update the frequency of the most frequent character.
To check if we have enough replacements, we will check if the length of the sliding window minus the frequency of the most frequent
in the sliding window is less than k, meaning that replacements can be made. Else, we will move the left pointer of the window
and update the dictionary.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        l, max_freq = 0, 0

        for r in range(len(s)):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])

            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
        
        return (r - l + 1)