'''
Problem:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
'''

'''
Logic:
For this problem, we need to find the longest consectutive sequence. One solution is to sort the array and then iterate through it, but sorting
takes O(nlogn) time complexity. A better solution is to use a hashset to remove duplicates and have a constant time complexity for accessing
elements. We will iterate through all the numbers in the hashset and for each number, check if it is the first in a sequence, meaning the number - 1
does not exists. If so, see how long of a sequence can be made starting from that number and update the longest length. This solution will take O(n) time but have O(n) space.
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
