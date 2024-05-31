'''
Problem:
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
'''

'''
Logic:
In this problem, the goal is to find the k most frequent elements in an array. For our solution, we can utilize a dictionary or hashmap to map the value to the count. After
creating the dictionary, we can sort the values based on the count by creating a empty list ,that contains another list, size length of nums + 1. We will use the indicies to represent the count, meaning
at index 1 of the list, we can say that the values store there have a count of 1. After storing the values, we will iterate backwards and and get the first k elements.
This solution has a O(n) time complexity as we only iterate through the array once and have O(n) space for the dictionary.
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

        