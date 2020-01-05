import json
import os
from block import Block


class Chain:

    def __init__(self):
        self._chain = [
            self._get_genesis_block(),
        ]
        print(self._chain)

    def is_valid(self):
        prev_block = self._chain[0]
        for block in self._chain[1:]:
            assert prev_block.checksum == self._prev_block.checksum
            assert block.is_valid()
            prev_block = block

    def add_block(self, data):
        print(data)
        block = Block(self._chain[-1], data)
        block = self._find_nonce(block)
        self._chain.append(block)
        
        return block

    @staticmethod
    def _get_genesis_block():
        print("here we are")
        genesis_block = Block(None, None)
        genesis_block.checksum = '00000453880b6f9179c0661bdf8ea06135f1575aa372e0e70a19b04de0d4cbc7'

        return genesis_block

    @staticmethod
    def _find_nonce(block):
        beginning = '0' * Block.CHECKSUM_LEAD_ZEROES
        while True:
            checksum = block.calculate_checksum()
            if checksum[:Block.CHECKSUM_LEAD_ZEROES] == beginning:
                break
            block.nonce += 1
        
        block.checksum = checksum

        return block