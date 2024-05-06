'''
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


'''
create a dictionary mapping (value:index)
iterate through nums repeating the following steps
- calculate complement(target - value)
- if complement exists, return the two indices
- else, add to dictionary (current value : current index)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        index_dict = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in index_dict:
                return [index, index_dict[complement]]
            
            index_dict[value] = index 
