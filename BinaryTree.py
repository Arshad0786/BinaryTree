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

    def initLeftLeaningTree(self):
        self.root = TreeNode(0)
        tracer = self.root
        for i in range(10):
            tracer.leftNode = TreeNode((i + 1) * 10)
            tracer = tracer.leftNode

    def initRightLeaningTree(self):
        self.root = TreeNode(0)
        tracer = self.root
        for i in range(10):
            tracer.rightNode = TreeNode((i + 1) * 10)
            tracer = tracer.rightNode

    def preorder_recursive(self, TreeNode):
        if not TreeNode:
            return []
        output = []
        output.append(TreeNode.val)
        if TreeNode.leftNode:
            output = output + self.preorder_recursive(TreeNode.leftNode)
        if TreeNode.rightNode:
            output = output + self.preorder_recursive(TreeNode.rightNode)
        return output

    def inorder_recursive(self, TreeNode):
        if not TreeNode:
            return []
        output = []
        if TreeNode.leftNode:
            output = output + self.inorder_recursive(TreeNode.leftNode)
        output.append(TreeNode.val)
        if TreeNode.rightNode:
            output = output + self.inorder_recursive(TreeNode.rightNode)
        return output

    def postorder_recursive(self, TreeNode):
        if not TreeNode:
            return []
        output = []
        if TreeNode.leftNode:
            output = output + self.postorder_recursive(TreeNode.leftNode)
        if TreeNode.rightNode:
            output = output + self.postorder_recursive(TreeNode.rightNode)
        output.append(TreeNode.val)
        return output

    def preorder_stack(self, TreeNode):
        if not TreeNode:
            return []
        output = []
        stack = []
        stack.append(TreeNode)
        while stack:
            current = stack.pop()
            output.append(current.val)
            if current.rightNode:
                stack.append(current.rightNode)
            if current.leftNode:
                stack.append(current.leftNode)
        return output

    def inorder_stack(self, TreeNode):
        if not TreeNode:
            return []
        output = []
        stack = []
        current = TreeNode
        while stack or current:
            while current:  # go to the most left node of the tree
                stack.append(current)
                current = current.leftNode
                """
                If it reaches null, goto last node in stack, append it to output
                since it's the most left node, then go right. 
                If right node is null, current will get last node from stack and append it
                to output since it's the second left node
                """
            current = stack.pop()  #
            output.append(current.val)  #
            current = current.rightNode  #
        return output

    def postorder_stack(self, TreeNode):
        # easier to make a postorder traversal by doing it backward then output the reversed result
        if not TreeNode:
            return []
        output = []
        stack = []
        stack.append(TreeNode)
        while stack:
            current = stack.pop()
            output.append(current.val)
            if current.leftNode:
                stack.append(current.leftNode)
            if current.rightNode:
                stack.append(current.rightNode)
        return output[::-1]

    def levelorder(self, TreeNode):
        if not TreeNode:
            return []
        output = []
        nextLevelQueue = []
        nextLevelQueue.append(TreeNode)
        while nextLevelQueue:
            thisLevelOutput = []
            currentLevelQueue = nextLevelQueue
            nextLevelQueue = []
            for current in currentLevelQueue:
                thisLevelOutput.append(current.val)
                if current.leftNode:
                    nextLevelQueue.append(current.leftNode)
                if current.rightNode:
                    nextLevelQueue.append(current.rightNode)
            output.append(thisLevelOutput)
        return output
    
    def depth(self, TreeNode):
        """
        return the depth of Binary Tree 
        """
        if not TreeNode:
            return 0
        return 1 + max(self.depth(TreeNode.leftNode),self.depth(TreeNode.rightNode))

    def isBalanced(self, TreeNode):
        if not TreeNode:
            return True
        if abs(self.depth(TreeNode.leftNode) - self.depth(TreeNode.rightNode)) > 1:
            return False
        return (True and self.isBalanced(TreeNode.leftNode) and self.isBalanced(TreeNode.rightNode))
