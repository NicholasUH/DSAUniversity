'''
Problem:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

'''
Logic:
Using the hashset, we can store elements we have already seen as we iterate through nums.
Iterate through nums, check if already seen and do appropriate action. Either, return True or add element to hashset.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    