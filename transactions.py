# transactions.py
def create_dummy_transactions():
    """
    Return a list of dummy transactions.
    """
    return [
        {"sender": "Aditya", "recipient": "Dwija", "amount": 5000},
        {"sender": "Dwija", "recipient": "Tarun", "amount": 3000},
        {"sender": "Dhanush", "recipient": "Ganesh", "amount": 2000}
    ]   

def get_tampered_transaction():
    """
    Return a tampered transaction.
    """
    return {"sender": "Hacker", "recipient": "Hacker", "amount": 500000}

def get_additional_transaction():
    """
    Return an additional transaction.
    """
    return {"sender": "Tanvi", "recipient": "Kushagra", "amount": 8000}