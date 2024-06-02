'''
Problem:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

'''
Logic:
The logic behind this problem is a combination of the two sum I and II problems with the target value being 0. To begin, we only need
to consider the negative numbers as adding to positive numbers will never result in zero and making sure that each negative number is considered
once in case of duplicates. We will also sort the array as the indices does not matter in this case getting all the negatives to the beginning of the array. 
At each negative number, we will have a left and right pointer that encase the numbers to the right of the negative number. Similar to two sum II, we will
iterate the pointers to increase or decrease the current sum, move right when we want to increase sum, or move left when we want to decrease sum.
When the current sum equals zero, we will append the three numbers to the result list and continue iterating, but also making sure to move the
left pointer to the next unique number making sure not to consider the same three numbers again.
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
