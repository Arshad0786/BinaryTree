import unittest
from BinaryTree import BinaryTree,TreeNode


class BinaryTreeTest(unittest.TestCase):
    def test_preorder_recursive(self):
        temp = BinaryTree()
        temp.initExampleTree()
        self.assertEqual(
            temp.preorder_recursive(temp.root), [10, 20, 40, 50, 30, 60, 70]
        )

    def test_inorder_recursive(self):
        temp = BinaryTree()
        temp.initExampleTree()
        self.assertEqual(
            temp.inorder_recursive(temp.root), [40, 20, 50, 10, 60, 30, 70]
        )

    def test_postorder_recursive(self):
        temp = BinaryTree()
        temp.initExampleTree()
        self.assertEqual(
            temp.postorder_recursive(temp.root), [40, 50, 20, 60, 70, 30, 10]
        )

    def test_preorder_stack(self):
        temp = BinaryTree()
        temp.initExampleTree()
        self.assertEqual(
            temp.preorder_recursive(temp.root), temp.preorder_stack(temp.root)
        )

    def test_inorder_stack(self):
        temp = BinaryTree()
        temp.initExampleTree()
        self.assertEqual(
            temp.inorder_recursive(temp.root), temp.inorder_stack(temp.root)
        )

    def test_postorder_stack(self):
        temp = BinaryTree()
        temp.initExampleTree()
        self.assertEqual(
            temp.postorder_recursive(temp.root), temp.postorder_stack(temp.root)
        )

    def test_levelorder(self):
        temp = BinaryTree()
        temp.initExampleTree()
        result = [[10], [20, 30], [40, 50, 60, 70]]
        self.assertEqual(temp.levelorder(temp.root), result)

    def test_leftLeaningTree(self):
        temp = BinaryTree()
        temp.initLeftLeaningTree()
        result = []
        for i in range(11):
            result.append((i) * 10)
        self.assertEqual(temp.preorder_recursive(temp.root), result)
        self.assertEqual(temp.inorder_recursive(temp.root), result[::-1])
        self.assertEqual(temp.postorder_recursive(temp.root), result[::-1])

    def test_rightLeaningTree(self):
        temp = BinaryTree()
        temp.initRightLeaningTree()
        result = []
        for i in range(11):
            result.append((i) * 10)
        self.assertEqual(temp.preorder_recursive(temp.root), result)
        self.assertEqual(temp.inorder_recursive(temp.root), result)
        self.assertEqual(temp.postorder_recursive(temp.root), result[::-1])

    def test_depth(self):
        temp = BinaryTree()
        self.assertEqual(temp.depth(temp.root),0)
        temp.root = TreeNode(10)
        self.assertEqual(temp.depth(temp.root),1)
        temp.initExampleTree()
        self.assertEqual(temp.depth(temp.root),3)
        temp.initLeftLeaningTree()
        self.assertEqual(temp.depth(temp.root),11)
        temp.initRightLeaningTree()
        self.assertEqual(temp.depth(temp.root),11)

    def test_isBalanced(self):
        temp = BinaryTree()
        self.assertEqual(temp.isBalanced(temp.root),True)
        temp.root = TreeNode(10)
        self.assertEqual(temp.isBalanced(temp.root),True)
        temp.initExampleTree()
        self.assertEqual(temp.isBalanced(temp.root),True)
        temp.initLeftLeaningTree()
        self.assertEqual(temp.isBalanced(temp.root),False)
        temp.initRightLeaningTree()
        self.assertEqual(temp.isBalanced(temp.root),False)
        temp.root = TreeNode(1)
        temp.root.leftNode = TreeNode(2)
        temp.root.rightNode = TreeNode(2)
        temp.root.leftNode.leftNode = TreeNode(3)
        temp.root.leftNode.leftNode.leftNode = TreeNode(4)
        self.assertEqual(temp.isBalanced(temp.root),False)





if __name__ == "__main__":
    unittest.main()
