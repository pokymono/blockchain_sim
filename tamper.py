# tamper.py
def tamper_blockchain(blockchain, block_index, new_data):
    """
    Tamper with the blockchain by replacing data in a specified block.
    After tampering, the block's hash is recalculated.
    """
    if 0 < block_index < len(blockchain.chain):
        # Update the data in the specified block
        blockchain.chain[block_index].data = new_data
        # Recalculate the hash for the tampered block
        blockchain.chain[block_index].hash = blockchain.chain[block_index].calculate_hash()
        print(f"Block {block_index} tampered. New data: {new_data}")
        print(f"New hash: {blockchain.chain[block_index].hash}")
    else:
        print(f"Cannot tamper with block {block_index} - invalid block index")
