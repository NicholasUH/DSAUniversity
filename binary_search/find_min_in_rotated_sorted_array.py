'''
Problem:
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''

'''
Logic: To find the minimum value of the special array within the time constraint, we must utilize a modified version of binary search.
We will follow the standard approach of binary approach by having a left, middle, and right pointer. We will iterate the left and right
pointers until they meet or cross and update the middle pointer every iteration. At every iteration, we will update the current minimum
value if a new minimum value is found. Now we must decide either to move to the left or right half portion of the array. We know in a normal sorted array,
the minimum will always be in the leftmost element of the array. But since the array is rotated a certain number of times to the right, there
exists cases where the minimum may be in the right half portion of the array or left half portion of the array. To know whether or not,
the possibility of the minimum being in the right half portion, we must look at the element at the right and middle pointers. If the right
element is less than the middle element, then the mimimum is in the right half. After the left and right pointers meet or cross, we will
return the mimimum between the current minimum and the element at the left pointer. This comparsion is due to the search not going all the way.
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        curr_min = float("inf")


        while l < r:
            mid = l + (r - l) // 2
            curr_min = min(curr_min, nums[mid])

            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return min(curr_min, nums[l])

