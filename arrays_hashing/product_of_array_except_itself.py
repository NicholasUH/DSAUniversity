'''
Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

'''
Logic:
The problem behind this problem is that each index should contain the product of all the elements except the element at that index and to achieve a O(n) time complexity.
The best solution is to create a prefix(product of left elements) and postfix (product of right elements) variable and then multiply them when iterating through the array.
We will have a answer array that originally stores [1] length nums. At each iteration, we will update the answer array with the current prefix/postfix and update the prefix/postfix
for the next indices. After iterating for prefix and postfix, the answer array should contain the correct products. The time complexity is O(n) time we iterate through
the array once and have O(n) space for the answer array.

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