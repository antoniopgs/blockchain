# ---------- DEPENDENCIES ----------
import datetime


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
        current_block = self.tail_block
        return current_block

    def __next__(self):
        current_block = current_block.previous_block
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
        if not self.tail_block:
            print("There are no Blocks in this Blockchain.\n")
        else:
            current_block = self.tail_block
            while True:
                print(current_block)
                if not current_block.previous_block:
                    break
                else:
                    current_block = current_block.previous_block


# ---------- MAIN CYCLE ----------
blockchains = []
while True:
    # Blockchains main view
    print("---------- BLOCKCHAINS ----------")
    # If no Blockchains exist
    if not blockchains:
        print("There are no existing Blockchains.")
    # If Blockchains do exist
    else:
        for blockchain in blockchains:
            print(f"- {blockchain}")
    user_input_1 = input("""N - New Blockchain
Q - Quit

Insert Command: """)
    if any(blockchain.name == user_input_1 for blockchain in blockchains):
        while True:
            user_input_2 = input(f"""---------- {blockchain.name.upper()} ----------
1 - New Block
2 - View Blocks
3 - Delete Blockchain
4 - Back

Insert Command: """)
            if user_input_2 == "1":
                print(f"\n----- {blockchain.name.upper()} - NEW BLOCK -----")
                user_input_3 = input("Insert Your Name: ")
                user_input_4 = input("Insert Value: ")
                user_input_5 = input("Insert Recipient: ")
                blockchain.add_block(user_input_3, user_input_4, user_input_5)
                print()
            elif user_input_2 == "2":
                print(f"\n----- {blockchain.name.upper()} - VIEW BLOCKS -----")
                blockchain.view()
            elif user_input_2 == "3":
                blockchains.remove(blockchain)
                print(f"{blockchain.name.upper()} SUCCESSFULLY DELETED\n")
                break
            elif user_input_2 == "4":
                break
            else:
                print("Invalid Command.\n")
    # If User selects to create a new Blockchain
    elif user_input_1 == "N":
        new_blockchain = Blockchain()
        print(f"{new_blockchain.name.upper()} SUCCESSFULLY CREATED\n")
    elif user_input_1 == "Q":
        break
    else:
        print("Invalid Command.\n")
