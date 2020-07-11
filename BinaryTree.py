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
            tracer.leftNode = TreeNode((i+1)*10)
            tracer = tracer.leftNode

    def initRightLeaningTree(self):
        self.root = TreeNode(0)
        tracer = self.root
        for i in range(10):
            tracer.rightNode = TreeNode((i+1)*10)
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
            root = stack.pop()
            output.append(root.val)
            if root.rightNode:
                stack.append(root.rightNode)
            if root.leftNode:
                stack.append(root.leftNode)
        return output
    
    def inorder_stack(self, TreeNode):
        if not TreeNode:
            return []
        output = []
        stack = []
        root = TreeNode
        while stack or root:
            while(root):
                stack.append(root)
                root = root.leftNode
            root = stack.pop()
            output.append(root.val)
            root = root.rightNode
        return output
    
    def postorder_stack(self, TreeNode):
        if not TreeNode:
            return []
        output = []
        stack = []
        
            
            
            
        
