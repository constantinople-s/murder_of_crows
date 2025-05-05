from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Block:
    id: str
    view: int
    value: float

class BlockProcessor:
    def __init__(self):
        self.blocks = {}
        self.views = defaultdict(list)
        self.votes = []
        self.chain = []

    def add_block(self, id, view, value):
        block = Block(id, view, value)
        if block.id in self.blocks or \
           block.id in self.chain or \
           block.view < len(self.chain):
            return False
        self.blocks[block.id] = block.view
        self.views[block.view].append(block)
        self.construct_chain()

    def add_vote(self, vote):
        if vote in self.chain or vote in self.votes:
            return False
        self.votes.append(vote)
        self.construct_chain()

    def remove_view(self, view):
        for block in self.views[view]:
            del self.blocks[block.id]
        del self.views[view]

    def construct_chain(self):
        while True:
            wanted_view = len(self.chain)
            for block in self.views[wanted_view]:
                if block.id in self.votes:
                    self.chain.append(block)
                    self.remove_view(wanted_view)
                    self.votes.remove(block.id)
                    print("Added a block to the chain \n", self.chain)
                    break
            else:
                break