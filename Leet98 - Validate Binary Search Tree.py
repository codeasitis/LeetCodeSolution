import sys
class Solution:
    def __init__(self):
        self.lastPrinted = -sys.maxsize-1
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        if root == None:
            return True
        if self.isValidBST(root.left) == False:
            return False
        data = root.val
        if data <= self.lastPrinted:
            return False
        self.lastPrinted = data
        if self.isValidBST(root.right) == False:
            return False
        return True
