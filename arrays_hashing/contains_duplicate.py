'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct
'''

'''
Brute Force Logic: The goal is to check if an integer array contains any duplicates and return a boolean result. 
A straightforward solution uses two loops: one iterates through each element as a "benchmark," 
while the other checks every subsequent element against it. 
Although effective, this solution has a time complexity of O(n^2), as each element is compared with all elements that follow, 
which can lead to slow performance for large arrays.
'''

def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

'''
Optimized Logic: To reduce iterations and increase efficiency, we can use a hash set, which allows fast access. 
As we iterate through the array, we add each value to the hash set if it’s not already present. 
If we find a value already in the set, it's a duplicate, so we return `True`. 
Otherwise, we complete the loop and return `False` if no duplicates are found.
'''

def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num) 
        
        return False

