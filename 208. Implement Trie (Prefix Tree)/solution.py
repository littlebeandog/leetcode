class Node(object):
    def __init__(self):
        self.nodes = {letter: None for letter in 'abcdefghijklmnopqrstuvwxyz'}
        self.cnt = 0


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        head, pre = self.head, None
        for one_letter in word:
            if not head.nodes[one_letter]:
                head.nodes[one_letter] = Node()
            head = head.nodes[one_letter]
            pre = head
        if pre:
            head.cnt += 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        head, pre = self.head, None
        for one_letter in word:
            if not head.nodes[one_letter]:
                return False
            head = head.nodes[one_letter]
        if word != '' and not head.cnt:
            return False
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        head = self.head
        for one_letter in prefix:
            if not head.nodes[one_letter]:
                return False
            head = head.nodes[one_letter]
        return True



        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)