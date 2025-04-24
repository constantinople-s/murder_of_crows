from block_processor import BlockProcessor
from input_processor import InputProcessor
from binary_tree import Node

def main():
    bp = BlockProcessor()
    ip = InputProcessor(bp)
    ip.get_input()
    tree = Node()
    tree.build_bst(bp.chain)
    tree.print_tree_type()

    print("\nPre-order traversal")
    tree.pre_order_traversal()
    print("\nIn-order traversal")
    tree.in_order_traversal()
    print("\nPost-order traversal")
    tree.post_order_traversal()

main()