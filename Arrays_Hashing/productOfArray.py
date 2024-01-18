class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix, postfix = 1, 1
        result = [1] * len(nums)
        
        for i in range(len(nums)):
            # forward step
            result[i] *= prefix
            prefix *= nums[i]

            # backward step
            result[len(nums) - 1 - i] *= postfix
            postfix *= nums[len(nums) - 1 - i]
        
        
        return result
        
        '''
        have two ints, prefix/postfix
        prefix - product of values on the left
        postfix - product of values on the right
        initialize an array of size len(nums)

        iteration steps:
        update result[current index] by multiplying with prefix
        update the prefix with nums[current index]
        '''