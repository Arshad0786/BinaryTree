import unittest
from BinaryTree import BinaryTree


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
        self.assertEqual(temp.inorder_recursive(temp.root), [40, 20, 50, 10, 60, 30, 70])

    def test_postorder_recursive(self):
        temp = BinaryTree()
        temp.initExampleTree()
        self.assertEqual(
            temp.postorder_recursive(temp.root), [40, 50, 20, 60, 70, 30, 10]
        )

    def test_preorder_stack(self):
        temp = BinaryTree()
        temp.initExampleTree()
        self.assertEqual(temp.preorder_recursive(temp.root),temp.preorder_stack(temp.root))

    def test_inorder_stack(self):
        temp = BinaryTree()
        temp.initExampleTree()
        self.assertEqual(temp.inorder_recursive(temp.root),temp.inorder_stack(temp.root))
    
    def test_leftLeaningTreeTest(self):
        temp = BinaryTree()
        temp.initLeftLeaningTree()
        result = []
        for i in range(11):
            result.append((i)*10)
        self.assertEqual(temp.preorder_recursive(temp.root),result)
        self.assertEqual(temp.inorder_recursive(temp.root),result[::-1])
        self.assertEqual(temp.postorder_recursive(temp.root),result[::-1])

    def test_rightLeaningTreeTest(self):
        temp = BinaryTree()
        temp.initRightLeaningTree()
        result = []
        for i in range(11):
            result.append((i)*10)
        self.assertEqual(temp.preorder_recursive(temp.root),result)
        self.assertEqual(temp.inorder_recursive(temp.root),result)
        self.assertEqual(temp.postorder_recursive(temp.root),result[::-1])
        


if __name__ == "__main__":
    unittest.main()
