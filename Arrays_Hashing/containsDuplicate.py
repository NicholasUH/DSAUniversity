class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
    

'''
1.create hashset to store already seen values
2. iterate through array and check each index to see if already seen
3. if seen, return True indicating a duplicate
4. add value at index to hashset and continue
5. return false at end of iteration indicating no duplicates were found
'''