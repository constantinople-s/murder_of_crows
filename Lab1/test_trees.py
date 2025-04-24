import unittest
from binary_tree import Node

class TestTreePropertiesDirect(unittest.TestCase):
    def test_perfect_tree(self):
        """Perfect tree: all levels fully filled"""
        chain = [{'value': 4}, {'value': 2}, {'value': 6}, 
                 {'value': 1}, {'value': 3}, {'value': 5}, {'value': 7}]
        tree = Node()
        tree.build_bst(chain)
        
        self.assertTrue(tree.is_perfect())
        self.assertTrue(tree.is_full())
        self.assertTrue(tree.is_complete())

    def test_full_tree(self):
        """Full tree: each node has 0 or 2 children"""
        chain = [{'value': 3}, {'value': 1}, {'value': 5}, {'value': 2}, {'value': 0}]
        tree = Node()
        tree.build_bst(chain)
        
        self.assertTrue(tree.is_full())
        self.assertFalse(tree.is_perfect())

    def test_complete_tree(self):
        """Complete tree: all levels except last fully filled"""
        chain = [{'value': 4}, {'value': 2}, {'value': 6}, 
                 {'value': 1}, {'value': 3}, {'value': 5}]
        tree = Node()
        tree.build_bst(chain)
        
        self.assertTrue(tree.is_complete())
        self.assertFalse(tree.is_perfect())

    def test_degenerate_tree(self):
        """Degenerate tree (worst-case BST)"""
        chain = [{'value': 1}, {'value': 2}, {'value': 3}, {'value': 4}]
        tree = Node()
        tree.build_bst(chain)
        
        self.assertFalse(tree.is_full())
        self.assertFalse(tree.is_perfect())
        self.assertFalse(tree.is_complete())

    def test_empty_tree(self):
        """Edge case: empty tree"""
        chain = []
        tree = Node()
        tree.build_bst(chain)
        
        self.assertTrue(tree.is_full())  # Vacuous truth
        self.assertTrue(tree.is_perfect())
        self.assertTrue(tree.is_complete())

    def test_single_node(self):
        """Edge case: single node tree"""
        chain = [{'value': 5}]
        tree = Node()
        tree.build_bst(chain)
        
        self.assertTrue(tree.is_full())
        self.assertTrue(tree.is_perfect())
        self.assertTrue(tree.is_complete())

if __name__ == '__main__':
    unittest.main(verbosity=2)