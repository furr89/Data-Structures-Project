import hashlib
import datetime
import time
import random

def calc_hash(hash_str):
      sha = hashlib.sha256()

      #hash_str = "We are going to encode this string of data!".encode('utf-8')
      hash_str = hash_str.encode('utf-8')

      sha.update(hash_str)

      sha.digest

      return sha.hexdigest()

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = None
      self.prev = None


# Blockchain class which is implemented using a linked list with pointers to the previous node, the block
class BlockChain:
    def __init__(self):
        self.head = None
        self.ledger = {}

    # Creates and adds the block to the front of the list
    def add_block(self, data):

        if data == "" or data == None:
            return

        # Handles Strange inputs like numbers and null
        if type(data) != str:
            data = str(data)

        creation_time = datetime.datetime.now()

        # Block creation if the list is empty
        if self.head == None:
            new_block = Block(creation_time, data, 0)
            new_block.hash = calc_hash(data)
            self.head = new_block
            self.ledger[new_block.data] = new_block.hash

        # Adds to the front if it's not empty
        else:
            prev_block = self.head

            new_block = Block(creation_time, data, prev_block.hash)
            new_block.hash = calc_hash(data)

            new_block.prev = self.head
            self.head = new_block

            # Checks if the data is not in the ledger, it is, it will generate a salted hash
            if data not in self.ledger.keys():
                self.ledger[new_block.data] = new_block.hash
            else:

                salt = random.randint(100, 999)
                salted_hash = calc_hash(data + str(salt))

                new_block.hash = salted_hash
                self.ledger[new_block.data] = salted_hash

    def get_block_details(self, block):

        print("Timestamp:", block.timestamp)
        print("Data:", block.data)
        print("Previous Hash:", block.previous_hash)
        print("Current Hash:", block.hash, "\n")
                

    # Loop through and checks if the data has been modified
    def check_validity(self):

        current = self.head

        while current.prev:
            
            if current.data in self.ledger:
                print("No tampering")
                self.get_block_details(current)
            else:
                print("There is tampering")
                self.get_block_details(current)

            current = current.prev


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

block_chain = BlockChain()

block_chain.add_block("First mined item")
#time.sleep(random.randrange(1, 2)) # For timestamp testing purposes
block_chain.add_block("Second block")
block_chain.add_block("Thrid block")
block_chain.add_block("Another one added")
block_chain.add_block("Last block")

# Test Case 1
#block_chain.check_validity() # Output should not have any tampering

# Test Case 2
block_chain.add_block(None) # Incorrect input, it will not be added
block_chain.add_block("") # Will also not be added

# Test Case 3
block_chain.head.prev.data = "This block is stolen!"
block_chain.check_validity() # Should output that there is tampering because of the changed data

#Test Case 4
block_chain.add_block("Third block") # Adds a block with same message as a previous block but with different hash

# Verifies if hashes are indeed different
for x in block_chain.ledger.items():
    print(x)
