import unittest
from block_processor import BlockProcessor
from input_processor import InputProcessor

class TestBlockProcessor(unittest.TestCase):
    def setUp(self):
        self.bp = BlockProcessor()

    def test_add_block(self):
        block = {'id': 'a1b2c3', 'view': 0}
        self.bp.add_block(block)
        self.assertEqual(self.bp.blocks['a1b2c3'], 0)

    def test_add_vote(self):
        vote = {'block_id': 'a1b2c3'}
        self.bp.add_vote(vote)
        self.assertIn('a1b2c3', self.bp.votes)

    def test_construct_chain(self):
        blocks = [
            {'id': 'a1b2c3', 'view': 0},
            {'id': 'd4e5f6', 'view': 1},
            {'id': 'g7h8i9', 'view': 2},
            {'id': 'j0k1l2', 'view': 1}
        ]
        votes = [{'block_id': 'a1b2c3'}, {'block_id': 'd4e5f6'}, {'block_id': 'g7h8i9'}]

        for block in blocks:
            self.bp.add_block(block)
        
        for vote in votes:
            self.bp.add_vote(vote)
        
        chain = self.bp.construct_chain()
        
        self.assertEqual(chain, ['a1b2c3', 'd4e5f6', 'g7h8i9'])

class TestInputProcessor(unittest.TestCase):
    def setUp(self):
        self.bp = BlockProcessor()
        self.ip = InputProcessor(self.bp)

    def test_process_blocks(self):
        self.assertIsNone(self.ip.process_blocks(['a1b2c3', '0']))
        self.assertFalse(self.ip.process_blocks(['a1b2c3']))
        self.assertFalse(self.ip.process_blocks(['a1b2c3', 'invalid']))
        self.assertFalse(self.ip.process_blocks(['invalid', '0']))

    def test_process_votes(self):
        self.assertIsNone(self.ip.process_votes('a1b2c3'))
        self.assertFalse(self.ip.process_votes('invalid'))

    def test_get_blocks(self):
        self.ip.process_blocks(['a1b2c3', '0'])
        self.ip.process_blocks(['d4e5f6', '1'])
        self.assertEqual(self.bp.blocks['a1b2c3'], 0)
        self.assertEqual(self.bp.blocks['d4e5f6'], 1)

    def test_get_votes(self):
        self.ip.process_votes('a1b2c3')
        self.ip.process_votes('d4e5f6')
        self.assertIn('a1b2c3', self.bp.votes)
        self.assertIn('d4e5f6', self.bp.votes)

if __name__ == '__main__':
    unittest.main()