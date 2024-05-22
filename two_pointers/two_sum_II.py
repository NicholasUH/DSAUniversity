'''
create a left and right pointer that starts at the first and last index respectively
keep iterating the left and right towards each other and repeat steps
-find the sum of values at pointers
- if sum < target, then we increase left pointer, increasing current sum closer to target
- if sum > target, then we decrease right pointers, decreasing current sum closer to target
-else return [left, right] + 1, as 1-indexed
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
            