# main.py
from blockchain import Blockchain, Block
from datetime import datetime
import time
import json
from transactions import create_dummy_transactions, get_tampered_transaction, get_additional_transaction
from tamper import tamper_blockchain

def print_blockchain_state(blockchain, title):
    """
    Helper function to consistently print blockchain state
    """
    print(f"\n{title}:")
    blockchain_dict = []
    for block in blockchain.chain:
        blockchain_dict.append(block.to_dict())
    formatted_json = json.dumps(blockchain_dict, indent=4)
    print(formatted_json)
    print(f"Blockchain valid: {blockchain.is_chain_valid()}")

def main():
    # Create a new blockchain
    print("Initializing blockchain with custom SHA-256 implementation...")
    my_blockchain = Blockchain()
    
    # Getting transactions from transactions.py
    print("\nFetching transactions from transactions module...")
    transactions = create_dummy_transactions()
    
    # Adding transactions to the blockchain
    print("\nAdding transactions to the blockchain:")
    
    for i, transaction in enumerate(transactions, 1):
        print(f"\nMining block {i} with transaction: {transaction}")
        start_time = time.time()
        
        success = my_blockchain.add_block(Block(i, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), transaction, ""))
        
        if success:
            elapsed = time.time() - start_time
            print(f"Block {i} added successfully in {elapsed:.2f} seconds")
        else:
            print(f"Failed to add block {i}")
    
    # Validate the blockchain before tampering
    print_blockchain_state(my_blockchain, "Blockchain before tampering")
    
    # Tamper with the blockchain
    print("\nTampering with the blockchain...")
    tampered_transaction = get_tampered_transaction()
    tamper_blockchain(my_blockchain, 1, tampered_transaction)
    
    # Validate the blockchain after tampering
    print_blockchain_state(my_blockchain, "Blockchain after tampering")

    # Add another block after tampering to see how it affects the chain
    print("\nAttempting to add another block after tampering...")
    additional_transaction = get_additional_transaction()
    
    # Use the correct index for the new block
    new_index = len(my_blockchain.chain)
    success = my_blockchain.add_block(Block(
        new_index, 
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
        additional_transaction, 
        ""  # Empty string, will be replaced by the blockchain.add_block method
    ))
    
    if success:
        print(f"Block {new_index} added successfully after tampering")
    else:
        print(f"Failed to add block {new_index} after tampering")
    
    # Final blockchain state
    print_blockchain_state(my_blockchain, "Final Blockchain state")

if __name__ == "__main__":
    main()
