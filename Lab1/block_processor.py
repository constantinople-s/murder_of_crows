from collections import defaultdict


class BlockProcessor:
    def __init__(self):
        self.blocks = {}
        self.views = defaultdict(list)
        self.votes = []
        self.chain = []
        self.tree_root = None

    def add_block(self, block):
        if block['id'] in self.blocks or \
           block['id'] in self.chain or \
           block['view'] < len(self.chain):
            return False
        self.blocks[block['id']] = block['view']
        self.views[block['view']].append(block['id'])
        self.construct_chain()
        self.build_tree()

    def add_vote(self, vote):
        if vote['block_id'] in self.chain or vote['block_id'] in self.votes:
            return False
        self.votes.append(vote['block_id'])
        self.construct_chain()

    def remove_view(self, view):
        for block_id in self.views[view]:
            del self.blocks[block_id]
        del self.views[view]

    def construct_chain(self):
        while True:
            wanted_view = len(self.chain)
            for block_id in self.views[wanted_view]:
                if block_id in self.votes:
                    self.chain.append(block_id)
                    self.remove_view(wanted_view)
                    self.votes.remove(block_id)
                    print("Added a block to the chain \n", self.chain)
                    break
            else:
                break

    def build_tree(self):
        nodes = []
        for block in self.blocks.values():
            nodes.append(Node(block['value'], block['id']))
        nodes.sort(key=lambda n: n.value)
        if not nodes:
            self.tree_root = None
            return
        self.tree_root = nodes[0]
        for node in nodes[1:]:
            self.insert_node(self.tree_root, node)


    def insert_node(self, root, new_node):
        if new_node.value < root.value:
            if root.left is None:
                root.left = new_node
            else:
                self.insert_node(root.left, new_node)
        else:
            if root.right is None:
                root.right = new_node
            else:
                self.insert_node(root.right, new_node)


class Node:
    def __init__(self, value, block_id):
        self.value = value
        self.block_id = block_id
        self.left = None
        self.right = None