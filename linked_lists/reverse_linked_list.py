'''
Problem:
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''


'''
Logic:
The simplest approach to reversing a linked list is to switch the pointer from the next node to the previous node. To achieve this, we will
have a current variable that iterates through the linked list keeping track of the current node that is having its pointer reversed. We
will also have a previous variable that will store the node before the current node, keeping track of what node to switch to. To prevent,
losing the node after the current node after switching, we will store the next node in a temporary variable and then perform the pointer
swap. After swapping the current pointer to the previous node, We will move the previous and current pointer one to the right, by moving the
previous to the current and the current to the next using the temporary variable. Once the current pointer reaches the end of the linked list,
we will return the node at previous as that is the head of the reversed linked list.
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev