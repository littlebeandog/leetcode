class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse_couple(head)
    
    def reverse_couple(self, left):
        if not left:
            return None
        elif not left.next:
            return left
        else:
            right = left.next
            next_couple = right.next
            right.next = left
            left.next = self.reverse_couple(next_couple)
            return right

