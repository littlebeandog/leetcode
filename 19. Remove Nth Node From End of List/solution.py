# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodes = []
        node = head
        while node:
            if len(nodes) < n + 1:
                nodes.append(node)
            else:
                nodes = nodes[1:] + [node]
            node = node.next
        nodes.append(None)      # append virtual ending
        if len(nodes) == n + 1: # head is removed
            return nodes[1]
        else:                   # head is not removed
            nodes[0].next = nodes[2]
            return head