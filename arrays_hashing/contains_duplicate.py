'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
'''

'''
Psuedo Code:
1. create a set to store already visited elements 
2. iterate through nums
3. continuously check if the current element is in the set
- if it is in the set, return true indicating there is a duplicate
- if it is not in the set, add it to the set
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


'''
Logic: if the set has no duplicates, the length of the set will be equal to the length of the array
'''
class AlternateSolution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)
    