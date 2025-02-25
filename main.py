from block_processor import BlockProcessor
from input_processor import InputProcessor

def main():
    bp = BlockProcessor()
    ip = InputProcessor(bp)
    ip.get_input()
    print(bp.construct_chain())

main()