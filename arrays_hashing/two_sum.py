'''
Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that 
they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

'''
Logic:
Our goal for this problem is to find the two numbers that add up to the target. The apparent solution is to use two for-loops and individually
check each combination of numbers. The time complexity of this solution is O(n^2) which is highly inefficient. The better solution is to utilize
a hashmap that maps the value to the index, as we need to return the indices of the values. The logic is to iterate through each index and check
whether a value that has been since seen adds up the current value to the target and return the two indicies. The time complexity of this 
solution is O(n) as we only need to iterate once through the array in total.
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        index_dict = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in index_dict:
                return [index, index_dict[complement]]
            
            index_dict[value] = index 
