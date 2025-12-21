# Set Solution
# class Solution(object):
#   def detectCycle(self, head):
#       """
#       :type head: ListNode
#       :rtype: ListNode
#       """
#       n = head
#       store = set()
#       while n:
#           if n not in store:
#               store.add(n)
#               n = n.next
#           else:
#               return n
#       return None         

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Floyd's Tortoise and Hare (Cycle Detection)
# MAGIC MATH: When slow and fast meet, the distance from the start to the cycle entrance is equal to the distance from the meeting point to the cycle entrance when moving slow.
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None