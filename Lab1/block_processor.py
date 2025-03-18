from collections import defaultdict


class BlockProcessor:
    def __init__(self):
        self.blocks = {}
        self.views = defaultdict(list)
        self.votes = []
        self.chain = []

    def add_block(self, block):
        if block['id'] in self.blocks or \
           block['id'] in self.chain or \
           block['view'] < len(self.chain):
            return False
        self.blocks[block['id']] = block['view']
        self.views[block['view']].append(block['id'])
        self.construct_chain()

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