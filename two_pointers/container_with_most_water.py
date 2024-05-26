'''
Problem:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

'''
Logic:
Create a left and right pointer at first and last index to create a container
Iterate the pointers until they both meet or cross
-calculate the maximum area of the current container and update if it is a new maximum
-update the lower height pointer by 1 to get new bounds
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maximum_area = 0

        while left < right:
            maximum_area = max(maximum_area, (right - left) * min(height[right], height[left]))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maximum_area
        