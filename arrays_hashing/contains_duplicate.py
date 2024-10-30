'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct
'''

'''
To determine if an integer array contains duplicates, we can start with a simple brute-force solution: use two loops to compare each element against every element that follows. 
This approach checks every possible pair, allowing us to identify duplicates. 
However, it has a time complexity of O(n²) due to repeated comparisons, which can slow down significantly with larger arrays.
'''

def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

'''
To optimize, we can use a hash set to leverage its fast access time. As we iterate through the array, we add each number to the hash set if it’s not already there. 
If we encounter a number that’s already in the set, we know it’s a duplicate and return `True` immediately. This approach reduces runtime to O(n), making it much more efficient for large arrays. 
If no duplicates are found after checking all elements, we return `False`.
'''

def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num) 
        
        return False

