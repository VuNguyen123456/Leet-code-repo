# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        beforeLoop = dummy
        count = 1

        # Step 1: Move `beforeLoop` to node before left
        while count < left:
            beforeLoop = beforeLoop.next
            count += 1

        # Step 2: Start reversing
        leftNode = beforeLoop.next      # First node in sublist
        cur = leftNode
        prev = None

        while count <= right:
            # nxt = cur.next
            # cur.next = prev
            # prev = cur
            # cur = nxt
            # count += 1
            # OR 
            tmp = cur
            cur = cur.next
            tmp.next = prev
            prev = tmp
            count += 1

        # Step 3: Connect parts
        beforeLoop.next = prev     # Connect before-loop to the last in the loop (because prev traveled that much now)
        leftNode.next = cur       # Connect the top of the loop tail to after-right (cur is now the next node after the loop)

        return dummy.next
