### first version
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode(0)
        node0 = node
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            node.next = ListNode(0)
            node = node.next
            print(node.val)
            node.val = (0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + carry
            print(node.val)
            if node.val >= 10:
                carry = 1
                node.val -= 10
            else:
                carry = 0
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return node0.next

## better version
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node = ListNode(0)
        node0 = node
        carry = 0
        while l1 or l2 or carry != 0:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, rem = divmod(carry, 10)
            node.next = ListNode(rem)
            node = node.next

        return node0.next