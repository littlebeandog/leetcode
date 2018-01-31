class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists) > 1:
            lists = lists + [[]] if len(lists) % 2 == 1 else lists
            for i in range(int(len(lists) / 2)):
                lists[i] = self.merge_2_lists(lists[i * 2], lists[i * 2 + 1])
            lists = lists[0: int((len(lists) + 1) / 2)]
        return [] if not lists else lists[0]

    def merge_2_lists(self, list1, list2):
        head = ListNode(0)
        node = head
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return head.next