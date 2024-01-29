class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        '''
        hashset to store values
        iterate through each value in nums
        continously count length as long as num + 1, num + 2, num + k exists in hashset
        keep track of longest with integer
        '''

        hashset = set(nums)
        answer = 0

        for num in nums:
            if num - 1 not in hashset:
                length = 1
                while num + length in hashset:
                    length += 1
                answer = max(answer, length)
        
        return answer
                