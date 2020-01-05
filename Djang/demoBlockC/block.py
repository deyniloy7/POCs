import time
from hashlib import sha256

class Block:
    CHECKSUM_LEAD_ZEROES = 5
    NONCE_SYMBOL = 'Z'

    def __init__(self, prev_block, data):
        self._prev_block = prev_block
        self.data = data
        self.checksum = None
        self.nonce = 0
        self.timestamp = time.time()

    @property
    def is_valid(self):
        ckecksum = self.calculate_checksum()

        return (
            checksum[:self.CHECKSUM_LEAD_ZEROES] == '0' * self.CHECKSUM_LEAD_ZEROES
            and checksum == self.checksum
        )
    
    def calculate_checksum(self):
        data = '|'.join([
            str(self.timestamp),
            self.data,
            self._prev_block.checksum,
        ])
        data += self.NONCE_SYMBOL * self.nonce

        return sha256(bytes(data, 'utf-8')).hexdigest()