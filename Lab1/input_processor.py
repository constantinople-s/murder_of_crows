class InputProcessor:
    def __init__(self, block_processor):
        self.bp = block_processor
        self.input_processing = "block"

    def get_input(self):
        while True:
            if self.input_processing == "block":
                self.get_blocks()
            elif self.input_processing == "vote":
                self.get_votes()
            else:
                break
    
    def get_blocks(self):
        while True:
            text = input("To add a block, enter its id, view and value, \
separated by a comma, or hit enter to enter votes, or enter 'stop' to finish:\n")
            if text == '':
                self.input_processing = "vote"
                break
            elif text == 'stop':
                self.input_processing = "stop"
                break
            block = text.split(',')
            self.process_blocks(block)

    def process_blocks(self, block):
        try:
            hex_string, view, value = block
        except ValueError:
            print("Invalid input")
            return False
        if not all(c in '0123456789abcdefABCDEF' for c in hex_string):
            print("Invalid id")
            return False
        try:
            view = int(view)
            value = float(value)
        except ValueError:
            print("Invalid view or value")
            return False
        if view >= 0:
            self.bp.add_block({'id': hex_string, 'view': view, 'value': value})

    def get_votes(self):
        while True:
            text = input("To add a vote, enter the block id, or hit enter to add blocks:\n")
            if text == '':
                self.input_processing = "block"
                break
            self.process_votes(text)

    def process_votes(self, vote):
        if not all(c in '0123456789abcdefABCDEF' for c in vote):
            print("Invalid id")
            return False
        self.bp.add_vote({'block_id': vote})