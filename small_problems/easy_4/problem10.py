"""
PROBLEM:
Write a function that returns True or False based on whether a given product
specified via an ID number is available.

The function should take two arguments: an ID and a list of transactions. Each
transaction is a dictionary.

True means that the sum of the quantity values of the item's transactions is 
greater than zero.

Each transaction has a movement identifier. 'out' means the amount in quantity is
leaving. 'in' means the quantity is incoming.


DATA:
- Input: Int (ID, and List of transactions. Each transaction is a dict)
- Output: List

EXAMPLE:
transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True

ALGORITHM:
- I think we want to generate a new list of transactions with their ID
and current quantity.
- Create new blank dictionary (inventory)
- Loop through transaction dictionary.
- For each transaction, check inventory for the item.
- If it's blank, add the id and quantity +/- based on movement
- If it's there, take the current quantity and update it with the quantity
in the current transaction


- We need to loop through all of the transactions.
- Check the ID.
- If the ID matches what we input for the argument, we should add that 
to an empty list.

- We could loop through with a for loop.
- Check the ID using transactions['id'] == ID
"""
def create_inventory(transactions):    
    result = {}

    for transaction in transactions:
        id = transaction['id']

        if transaction['movement'] == 'out':
            quantity = -transaction['quantity']
        else:
            quantity = transaction['quantity']

        result[id] = result.get(id, 0) + quantity
    
    return result

def is_item_available(inventory_id, transactions):
    inventory = create_inventory(transactions) 
    return inventory[inventory_id] > 0

# def transactions_for(inventory_id, transactions):
#     return [transaction for transaction in transactions if transaction['id'] == inventory_id]

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True