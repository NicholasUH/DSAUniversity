'''
Problem:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

'''
Logic:
To find the maximum amount of water that can be stored, we can use a two pointer approach. We will have two pointers left and right that start
at the beginning and end of the array respectively. We will then calculate the amount of water that can be contained by multiplying 
the height(shorter array value of the two pointers) and the width(difference between the two pointers' indices), we will then update the maximum if
a new maximum is found. We can then iterate one pointer by only moving the pointer with the lower height until the two pointers meet or cross.
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
        