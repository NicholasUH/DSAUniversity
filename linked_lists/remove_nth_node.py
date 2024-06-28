'''
Problem:
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

'''
Logic:
Like most linked list problems, we can utilize a two pointer approach to remove the target node. We will have two pointers, a left pointer 
that will land on the node right before the one we want to remove and a right pointer that will ensure that the left pointer lands on the 
node. Before we iterate the pointers, we must add a dummy node to the head of the linked list, this helps the left pointer land on the node
before the target node. We will then iterate the right pointer n times to ensure that the left pointer lands on the node a distance of n from
the end of the linked list. Now we iterate both pointers until the right pointer reaches the end, the left pointer should land on the node
before the target node. We will then adjust the pointers to remove the target node and return the head of the linked list.
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        

        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next