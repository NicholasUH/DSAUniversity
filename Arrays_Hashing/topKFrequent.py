class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = collections.defaultdict(int)
        
        for num in nums:
            hashmap[num] += 1
        
        sorted_map = sorted(hashmap.keys(), key=lambda x: hashmap[x], reverse=True)

        return sorted_map[:k]

'''
create a hashmap that stores int:frequency
store the values of nums into hashmap
descending sort the values of hashmap
'''