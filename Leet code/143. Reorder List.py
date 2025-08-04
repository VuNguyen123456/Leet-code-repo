# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next # 2nd halve of next
        slow.next = None

        # Reserving 2nd portion of list
        prev = None
        while second:
            tmp = second
            second = second.next
            tmp.next = prev
            prev = tmp

        #Merge the 2 havlves of the list
        second = prev # prev is the last element, second is now null (after this second will be the start of the 2nd array(the biggest))
        first = head
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
