class TreeNode:
    def __init__(self, val, root=None, leftNode=None, rightNode=None):
        self.val = val
        self.root = root
        self.leftNode = leftNode
        self.rightNode = rightNode


class BinaryTree:
    def __init__(self):
        self.root = None

    def initExampleTree(self):
        self.root = TreeNode(10)
        self.root.leftNode = TreeNode(20)
        self.root.rightNode = TreeNode(30)
        self.root.leftNode.leftNode = TreeNode(40)
        self.root.leftNode.rightNode = TreeNode(50)
        self.root.rightNode.leftNode = TreeNode(60)
        self.root.rightNode.rightNode = TreeNode(70)

    def preorderTraversal(self, TreeNode):
        if not TreeNode:
            return []
        output = []
        output.append(TreeNode.val)
        if TreeNode.leftNode:
            output = output + self.preorderTraversal(TreeNode.leftNode)
        if TreeNode.rightNode:
            output = output + self.preorderTraversal(TreeNode.rightNode)
        return output

    def inorderTraversal(self, TreeNode):
        if not TreeNode:
            return []
        output = []
        if TreeNode.leftNode:
            output = output + self.inorderTraversal(TreeNode.leftNode)
        output.append(TreeNode.val)
        if TreeNode.rightNode:
            output = output + self.inorderTraversal(TreeNode.rightNode)
        return output

    def postorderTraversal(self, TreeNode):
        if not TreeNode:
            return []
        output = []
        if TreeNode.leftNode:
            output = output + self.postorderTraversal(TreeNode.leftNode)
        if TreeNode.rightNode:
            output = output + self.postorderTraversal(TreeNode.rightNode)
        output.append(TreeNode.val)
        return output
