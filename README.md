# Blockchain Simulation

A simple blockchain simulation implemented in Python that demonstrates the core concepts of blockchain technology, including mining, transaction verification, and tamper detection.

## Overview

This project implements a basic blockchain with the following features:
- Custom SHA-256 hashing implementation
- Proof-of-work consensus mechanism
- Block mining with adjustable difficulty
- Transaction creation and verification
- Tamper detection and chain validation
- Interactive command-line interface

## Project Structure

- `main.py` - Entry point and interactive CLI
- `blockchain.py` - Core blockchain and block implementation
- `sha256_custom.py` - Custom implementation of SHA-256 algorithm
- `transactions.py` - Transaction handling and creation utilities
- `tamper.py` - Tools for demonstrating blockchain tampering
- `__init__.py` - Python package initialization

## Technical Details

### Blockchain

The blockchain consists of a chain of blocks, with each block containing:
- Index (position in the chain)
- Timestamp (when the block was created)
- Transaction data
- Previous block's hash
- Current block's hash
- Nonce (used in the mining process)

### Mining Process

The mining process implements a proof-of-work algorithm:
1. The system tries to find a block hash that starts with a specific number of zeros (determined by the difficulty level)
2. The nonce is incremented until a valid hash is found
3. This process requires computational power, making it difficult to tamper with the chain

### Tamper Detection

The integrity of the blockchain is maintained by:
- Each block containing the hash of the previous block
- Block validation checks that ensure hashes are correctly calculated
- Chain validation that verifies the entire blockchain's integrity

## Installation

1. Clone this repository:
```
git clone https://github.com/pokymono/blockchain_sim.git
cd blockchain_sim
```

2. No external dependencies are required as the project uses only Python standard libraries.

## Usage

### Running the Simulation

To run the blockchain simulation:

```
python main.py
```

### Interactive Options

The simulation provides an interactive CLI with the following options:

1. **Transaction Creation:**
   - Use dummy transactions provided by the system
   - Create custom transactions with your own sender, recipient, and amount

2. **Blockchain Monitoring:**
   - View the entire blockchain state in JSON format
   - See validation results for the chain's integrity

3. **Tamper Demonstration:**
   - The system demonstrates how tampering with a block affects the entire chain
   - Shows how the blockchain detects invalid modifications

### Example Session

```
Initializing blockchain with custom SHA-256 implementation...

Do you want to use dummy transactions or input your own?
1. Use dummy transactions
2. Input my own transactions
Enter your choice (1 or 2): 1

Fetching transactions from transactions module...

Adding transactions to the blockchain:

Mining block 1 with transaction: {'sender': 'Aditya', 'recipient': 'Dwija', 'amount': 5000}
Mining block... (target: 00)
Mining attempt 0, current hash: 8f3d27e7d0...
Block mined in 0.05 seconds after 217 attempts: 00f8a73a991e638c67b87517e3436ead20ad1a5b52cb55ef8852292a7a4d9623
Block 1 added successfully in 0.06 seconds

Mining block 2 with transaction: {'sender': 'Dwija', 'recipient': 'Tarun', 'amount': 3000}
Mining block... (target: 00)
Mining attempt 0, current hash: f1ad5e7bae...
Block mined in 0.08 seconds after 314 attempts: 00aef1ba72e94f4c7d374f167a3171931de9cb3c6c95cf9ee07e35a3328943f2
Block 2 added successfully in 0.09 seconds

Mining block 3 with transaction: {'sender': 'Dhanush', 'recipient': 'Ganesh', 'amount': 2000}
Mining block... (target: 00)
Mining attempt 0, current hash: 91ca741c3e...
Block mined in 0.03 seconds after 126 attempts: 00e9a672786d35e04cf126836df9cf6214aff394cff9e9621e485f5f2f36bf03
Block 3 added successfully in 0.04 seconds

Blockchain before tampering:
[
    {
        "index": 0,
        "timestamp": "2023-07-15 10:23:17",
        "data": "Genesis Block",
        "previous_hash": "0",
        "hash": "f4a742d76516a44383d8a5b8ddc4c4072ebc7d5a9c0ba0cfa5b5386a05156566",
        "nonce": 0
    },
    ...
]
Blockchain valid: True

Tampering with the blockchain...
Block 1 tampered. New data: {'sender': 'Hacker', 'recipient': 'Hacker', 'amount': 500000}
New hash: 7ae1c28e29e689c6acb220e32f8f6cd302a558bfce4a43dfa71b2cb5b1e249a7

Blockchain after tampering:
[
    ...
]
Blockchain valid: False

Attempting to add another block after tampering...
Mining block... (target: 00)
Mining attempt 0, current hash: 578c19ae35...
Block mined in 0.06 seconds after 249 attempts: 0023f57a8c19dfa367ad3fcbbc3478d692f34a7ee32e1f4c9ebaed3f9fa732c5
Block 4 added successfully after tampering

Final Blockchain state:
[
    ...
]
Blockchain valid: False
```

## Key Learnings

Through this simulation, you can learn:
- How blockchain achieves immutability through hash linking
- The role of proof-of-work in securing the blockchain
- Why tampering with a block invalidates all subsequent blocks
- How cryptographic hashing provides security to the blockchain

## Extending the Project

Some ways you could extend this simulation:
- Implement networking to create a distributed blockchain
- Add a consensus mechanism beyond proof-of-work
- Create a web interface for better visualization
- Implement smart contracts functionality
- Add digital signature verification for transactions

## License

This project is open source and available under the [MIT License](LICENSE).
