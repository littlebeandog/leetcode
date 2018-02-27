class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow_pre, slow, fast = None, head, head
        while fast and fast.next:
            slow_pre, slow, fast = slow, slow.next, fast.next.next
        slow_pre.next = None

        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, head1, head2):
        head = tail = ListNode(0)
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                tail = tail.next
                head1 = head1.next
            else:
                tail.next = head2
                tail = tail.next
                head2 = head2.next
        tail.next = head1 or head2
        return head.next
