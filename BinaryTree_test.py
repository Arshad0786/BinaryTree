import unittest
from BinaryTree import BinaryTree


class BinaryTreeTest(unittest.TestCase):
    def test_preorderTraversal(self):
        temp = BinaryTree()
        temp.initExampleTree()
        self.assertEqual(
            temp.preorderTraversal(temp.root), [10, 20, 40, 50, 30, 60, 70]
        )

    def test_inorderTraversal(self):
        temp = BinaryTree()
        temp.initExampleTree()
        self.assertEqual(temp.inorderTraversal(temp.root), [40, 20, 50, 10, 60, 30, 70])

    def test_postorderTraversal(self):
        temp = BinaryTree()
        temp.initExampleTree()
        self.assertEqual(
            temp.postorderTraversal(temp.root), [40, 50, 20, 60, 70, 30, 10]
        )


if __name__ == "__main__":
    unittest.main()
