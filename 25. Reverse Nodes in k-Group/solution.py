# None one-pass
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        return self.reverse_several(head, k)
         
    def reverse_several(self, start, n):
        node = start
        i = 0
        while node:
            node = node.next
            i += 1

        if i < n:
            return start
        else:
            prev, node = None, start
            for i in range(n):
                next = node.next
                node.next = prev
                prev = node
                node = next
            start.next = self.reverse_several(node, n)
            return prev
        