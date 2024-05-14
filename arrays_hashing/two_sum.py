'''
Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

'''
Logic:
Use a dictionary to store the value and its index.
Iterate through nums, at each element, check if complement(target - element) exists in the dictionary and do appropriate action.
If exists, return two indicies and if not, add element and its index to the dictionary.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_dict = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in index_dict:
                return [index, index_dict[complement]]
            
            index_dict[value] = index 
