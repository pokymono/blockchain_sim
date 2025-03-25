# block.py
import json
from sha256_custom  import sha256  # Replace 'SHA_256' with your module name if needed
import time # For timestamping

class Block:
    def __init__(self, index, transactions, previous_hash, proof):
        self.index = index                          # Block number or index
        self.timestamp = time.time()                # Timestamp of block creation
        self.transactions = transactions            # List of transactions
        self.previous_hash = previous_hash          # Hash of the previous block
        self.proof = proof                          # Proof-pf-work
        self.hash = self.compute_hash()             # Current block hash

    def compute_hash(self):
        """
        Compute the block's hash using the custom sha256 function and converted to JSON.
        """
        block_content = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "proof": self.proof
        }, sort_keys=True)
        return sha256(block_content)
