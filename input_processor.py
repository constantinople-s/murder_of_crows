class InputProcessor:
    def __init__(self, block_processor):
        self.bp = block_processor

    def get_input(self):
        self.get_blocks()
        self.get_votes()
    
    def get_blocks(self):
        while True:
            text = input("To add a block, enter its id and view, \
separated by a comma, or hit enter to skip:\n")
            if text == '':
                break
            block = text.split(',')
            self.process_blocks(block)

    def process_blocks(self, block):
        try:
            hex_string, view = block
        except ValueError:
            print("Invalid input")
            return False
        if not all(c in '0123456789abcdefABCDEF' for c in hex_string):
            print("Invalid id")
            return False
        try:
            view = int(view) 
        except ValueError:
            print("Invalid view")
            return False
        if view >= 0:
            self.bp.add_block({'id': hex_string, 'view': view})

    def get_votes(self):
        while True:
            text = input("To add a vote, enter the block id, or hit enter to skip:\n")
            if text == '':
                break
            self.process_votes(text)

    def process_votes(self, vote):
        if not all(c in '0123456789abcdefABCDEF' for c in vote):
            print("Invalid id")
            return False
        self.bp.add_vote({'block_id': vote})