'''
Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

'''
Logic:
sort nums to get all negative numbers first
iterate through unique negative values in nums
-create left and right pointers, covering values left of current index
-while left < right
 -calculate sum of three values
 -if sum < 0, increase left to increase sum as sorted
 -if sum > 0, decrease right to decrease sum as sorted
 -else, append list of 3 values to result list, continue with current iteration but left pointer must start on new value
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, value in enumerate(nums):
            if value > 0:
                break
            
            if index > 0 and value == nums[index - 1]:
                continue
            
            left, right = index + 1, len(nums) - 1

            while left < right:
                current_sum = value + nums[left] + nums[right]
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    result.append([value, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return result
