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


if __name__ == "__main__":
    unittest.main()
