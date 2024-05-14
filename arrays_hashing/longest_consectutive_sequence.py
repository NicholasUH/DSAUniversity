'''
Problem:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

'''
Logic:
Create a hashset containing the unique values of nums.
Iterate through that hashset and at each element,
-see if it is the first in a sequence
-if so, keep checking if the next numbers in the sequence exists
Update longest if a new longest is found
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_length = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_length = 1
                while num + current_length in nums_set:
                    current_length += 1
                longest_length = max(longest_length, current_length)
        
        return longest_length
