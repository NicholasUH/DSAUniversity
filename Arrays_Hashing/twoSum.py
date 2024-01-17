class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [index, hashmap[diff]]
            else:
                hashmap[num] = index
        
'''

'''