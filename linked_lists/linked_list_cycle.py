'''
Problem:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

'''
Logic: To detect a cycle in a linked list, we can utilize the tortoise and hare cycle dectection algorithm. The algorithm utilizes two pointesrs, slow and fast. Both start
at the same position, the slow pointer will move one position at a time while the fast pointer will move two at a time. If a cycle exists, the pointers will eventually meet at some
point. Using this approach, we will iterate the pointers until either they meet, indicating a cycle, or until the fast pointer reaches the end of the list, indicating no cycle.
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False