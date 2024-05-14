'''
Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

'''
Logic:
Create a answer list length equal to nums filled with 1
Create two ints, prefix(product of left elements), postfix(product of right elements)

Prefix Iteration:
set current answer to the prefix
multiply prefix with the current nums

Postfix Iteration:
multiply current answer with postfix to get final result
multiply postfix with current nums
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1,-1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer