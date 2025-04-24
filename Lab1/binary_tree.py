class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def build_bst(self, chain):
        if not chain:
            return None
        for block in chain:
            self.add(block)

    def add(self, block):
        if self.value is None:
            self.value = block
        elif block['value'] <= self.value['value']:
            if self.left is None:
                self.left = Node(block)
            else:
                self.left.add(block)
        else:
            if self.right is None:
                self.right = Node(block)
            else:
                self.right.add(block)


    def is_full(self):
        if not self.left and not self.right:
            return True
        if self.left and self.right:
            return self.left.is_full() and self.right.is_full()
        return False

    def is_complete(self):
        """Check if the tree is complete using BFS"""
        if self.value is None:  # Empty tree
            return True

        queue = [self]
        non_full_node_seen = False

        while queue:
            current = queue.pop(0)

            # Check left child
            if current.left:
                if non_full_node_seen:
                    return False
                queue.append(current.left)
            else:
                non_full_node_seen = True

            # Check right child
            if current.right:
                if non_full_node_seen:
                    return False
                queue.append(current.right)
            else:
                non_full_node_seen = True

        return True

    def is_perfect(self, depth=0, level=None):
        """Check if the tree is perfect"""
        if level is None:
            level = self.max_depth()
        if not self.left and not self.right:
            return depth == level - 1
        if not self.left or not self.right:
            return False
        return self.left.is_perfect(depth+1, level) and self.right.is_perfect(depth+1, level)

    def count_nodes(self):
        """Count nodes in the tree"""
        left_count = self.left.count_nodes() if self.left else 0
        right_count = self.right.count_nodes() if self.right else 0
        return 1 + left_count + right_count
    
    def max_depth(self):
        """Calculate maximum depth of the tree"""
        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0
        return 1 + max(left_depth, right_depth)

    def pre_order_traversal(self):
        print(self.value, end=" ")
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value, end=" ")
        if self.right:
            self.right.in_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value, end=" ")

    def print_tree_type(self):
        is_full = self.is_full()
        is_complete = self.is_complete()
        is_perfect = is_full and is_complete and self.is_perfect()
        
        if is_perfect:
            print("Perfect")
        if is_full:
            print("Full")
        if is_complete:
            print("Complete")

        if not(is_full and is_complete):
            print('Not a special type')
