'''
Problem:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

'''
Logic:
To merge the two sorted linked lists into one, we can iterate through both lists and compare the values of the nodes and add the node
with the smaller value to the new list. We will continously add the nodes until both or one lists reaches the end. To handle the cases
where the lists are different sizes, we will see which list did not reach the end and add the remaining nodes to the new list. We will also
use a dummy node to keep track of the head of the new list and avoid adding to a list that has no nodes.
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next
        
        if list1:
            node.next = list1
        
        if list2:
            node.next = list2

        return dummy.next
