class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        node = root
        while node != None:
            self.stack.append(node)
            node = node.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    # @return an integer, the next smallest number
    def next(self):
        """
        :rtype: int
        """
        nextNode = self.stack.pop()
        currentNode = nextNode.right
        while currentNode != None:
            self.stack.append(currentNode)
            currentNode = currentNode.left
        return nextNode.val