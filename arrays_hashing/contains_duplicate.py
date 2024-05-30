'''
Problem:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

'''
Logic:
For this problem, our goal is to find the duplicate element efficiently. The traditional way to solve this problem is brute forcing using two
for-loops and individually check each element with the others. This is very inefficient as the time complexity is O(n^2). 
A better solution is to use hashset. We can use the set as a way to store already seen elements and have efficent access to them. 
The approach is to iterate through the array and add each element to the set. We also check if the element is already in the set. 
If so, return True else return False. The time complexity of this solution is O(n) which is faster than the brute force, but does require O(n) space.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    