'''
Problem:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
'''

'''
Logic:
Like the original two sum problem, we need to find the two numbers that add up to the target. This problem adds in the stipulation that the
array is sorted. We can use two pointers starting at the begin and end of the array to find the two numbers that add up to the target. We will
iterate until the pointers meet or cross. We will add the two numbers together at the pointers and check if it is equal to the target.
To determine how to iterate the pointers, we will use the fact that the array is sorted to our advantage. When the bound move to the left,
we know that the sum will get smaller, and vice versa when the bounds moves to the right due to the sorted array.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left <= right:
            sum = numbers[right] + numbers[left]

            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
            