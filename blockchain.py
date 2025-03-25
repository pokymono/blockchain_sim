from datetime import datetime
import json
import sha256_custom
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return sha256_custom.sha256(block_string)
    
    def mine_block(self, difficulty):
        target = "0" * difficulty
        start_time = time.time()
        max_iterations = 10000  # Limit iterations to prevent infinite loops
        
        print(f"Mining block... (target: {target})")
        
        for i in range(max_iterations):
            if i % 100 == 0:  # Print progress every 100 attempts
                print(f"Mining attempt {i}, current hash: {self.hash[:10]}...")
            
            if self.hash[:difficulty] == target:
                elapsed_time = time.time() - start_time
                print(f"Block mined in {elapsed_time:.2f} seconds after {i} attempts: {self.hash}")
                return True
            
            self.nonce += 1
            self.hash = self.calculate_hash()
            
        print(f"Mining failed after {max_iterations} attempts. Try with lower difficulty.")
        return False

    def to_dict(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'hash': self.hash,
            'nonce': self.nonce
        }

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2  # Reduced difficulty for faster mining
    
    def create_genesis_block(self):
        return Block(0, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Genesis Block", "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        if new_block.mine_block(self.difficulty):
            self.chain.append(new_block)
            return True
        return False
    
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if hash is correctly calculated
            if current_block.hash != current_block.calculate_hash():
                print("Invalid hash")
                return False
            
            # Check if this block points to the correct previous block
            if current_block.previous_hash != previous_block.hash:
                print("Invalid previous hash reference")
                return False
        
        return True
    
    def to_json(self):
        """
        Convert the blockchain to JSON format.
        """
        blockchain_dict = []
        for block in self.chain:
            blockchain_dict.append(block.to_dict())
        return json.dumps(blockchain_dict, indent=4, sort_keys=True)