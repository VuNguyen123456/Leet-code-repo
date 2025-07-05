class Solution(object):
  def detectCycle(self, head):
      """
      :type head: ListNode
      :rtype: ListNode
      """
      n = head
      store = set()
      while n:
          if n not in store:
              store.add(n)
              n = n.next
          else:
              return n
      return None         