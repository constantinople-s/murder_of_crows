class BlockProcessor:
    def __init__(self):
        self.blocks = {}
        self.votes = []

    def add_block(self, block):
        self.blocks[block['id']] = block['view']

    def add_vote(self, vote):
        self.votes.append(vote['block_id'])

    def construct_chain(self):
        voted_block_ids = set(self.votes)
        filtered_blocks = {block_id: view for block_id, view in self.blocks.items() 
                           if block_id in voted_block_ids}
        sorted_blocks = sorted(filtered_blocks.keys(), key=lambda x: filtered_blocks[x])

        result = []
        for block_id in sorted_blocks:
            if filtered_blocks[block_id] == len(result):
                result.append(block_id)
        return result
    