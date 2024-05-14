'''
Problem:
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
'''

'''
Logic
Create a dictionary that stores the num:counts and fill it using nums
Create a list that stores each value at the index equal to their count
Iterate backwards in the list, adding the first k elements to the list
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = collections.defaultdict(int)
        count_list = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            count_dict[num] += 1

        for num, count in count_dict.items():
            count_list[count].append(num)

        for i in range(len(count_list) - 1, 0, -1):
            for num in count_list[i]:
                result.append(num)
                if len(result) == k:
                    return result

        