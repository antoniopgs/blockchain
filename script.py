# ---------- DEPENDENCIES AND OTHERS ----------
import datetime
blockchains = []
n = 0
# ---------- BLOCK CLASS ----------
class Block:
    def __init__(self, sender, money, receiver, previous_block=None):
        self.time = datetime.datetime.now()
        self.sender = sender
        self.money = money
        self.receiver = receiver
        self.previous_block = previous_block

    def __repr__(self):
        return f"""> NEW BLOCK:
Time: {self.time}
Sender: {self.sender}
Money: {self.money}
Receiver: {self.receiver}
"""


# ----------BLOCKCHAIN CLASS ----------
class Blockchain:
    def __init__(self):
        # Set "Tail Block" default as none. This will help identify if Blockchain is empty or not.
        self.tail_block = None
        # Check if there are any existing blockchains
        if not blockchains:
            self.name = input("Insert New Blockchain Name: ")
            blockchains.append(self)
        else:
            # Cycle to ensure new Blockchain has a unique name.
            valid_name = False
            while not valid_name:
                name = input("Insert New Blockchain Name: ")
                print()
                if any(blockchain.name == name for blockchain in blockchains):
                    print("Name already in use.\n")
                else:
                    valid_name = True
                    self.name = name
                    blockchains.append(self)
                        
    def __iter__(self):
        return self

    def __next__(self):
        # If Blockchain is empty:
        if not self.tail_block:
            raise StopIteration
        # If Blockchain is not empty:
        else:
            """ 'n' counts what iteration of "__next__()" the program is in.
                Or in other words, how many times the "__next__()" function has been run."""
            global n
            n += 1
            # If it's the first "__next__()" iteration:
            if n == 1:
                return self.tail_block
            # If it's after the first "__next__()" iteration:
            else:
                current_block = self.tail_block
                for i in range(n-1):
                    current_block = current_block.previous_block
                if not current_block:
                    # Reset "n" to 0, so that next iteration works the same:
                    n = 0
                    raise StopIteration
                else:
                    return current_block
            
    def __repr__(self):
        return f"{self.name}"

    def add_block(self, new_block_sender, new_block_money, new_block_receiver):
        # Check to see if Blockchain is empty
        if not self.tail_block:
            new_block = Block(new_block_sender, new_block_money, new_block_receiver)
        # If it's not empty, the new block's "previous block" will be the existing "tail block"
        else:
            new_block = Block(new_block_sender, new_block_money, new_block_receiver, self.tail_block)
        # Update "Tail Block" to the newly created block
        self.tail_block = new_block

    def view(self):
        if not [block for block in self]:
            print("This Blockchain is empty.\n")
        else:
            for block in self:
                print(block)


# ---------- TESTS ----------
# Testing my iterator with an empty Blockchain:
blockchain_1 = Blockchain()
blockchain_1.view()

# Testing my iterator with non empty Blockchain:
blockchain_2 = Blockchain()
blockchain_2.add_block("António", 200000, "Tim")
blockchain_2.add_block("António", 100000, "Bob")
blockchain_2.add_block("António", 50000, "John")
blockchain_2.add_block("António", 50000, "Bill")
blockchain_2.view()
