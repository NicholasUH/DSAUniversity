'''
Problem:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

'''
Logic:
We will iterate through the array and add elements to the hashset. As we add, we check if the element has already been added to the hashset. 
If it has, we know that the element is a duplicate and return the appropriate boolean value.
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