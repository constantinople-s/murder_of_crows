class InputProcessor:
    def __init__(self, block_processor):
        self.bp = block_processor

    def get_input(self):
        while True:
            text = input("Enter 'block id:view:value' to add blocks, 'vote id' to add votes, or 'stop' to finish:\n")
            if text == 'stop':
                print("Exiting input processor")
                break
            try:
                mode, data = text.split()
            except ValueError:
                print("Invalid input")
                continue
            if mode == 'block':
                self.process_blocks(data.split(':'))
            elif mode == 'vote':
                self.process_votes(data)
            else:
                print("Invalid input")
    
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
            self.bp.add_block(hex_string, view, value)

    def process_votes(self, vote):
        if not all(c in '0123456789abcdefABCDEF' for c in vote):
            print("Invalid id")
            return False
        self.bp.add_vote(vote)