import datetime


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


class Blockchain:
    def __init__(self):
        # Set "Tail Block" default as none. This will help identify if Blockchain is empty or not.
        self.tail_block = None
        # Check if there are any existing blockchains
        if not blockchains:
            self.name = input("Insert New Chain Name: ")
            blockchains.append(self)
        else:
            # Cycle to ensure new Blockchain has a unique name.
            valid_name = False
            while not valid_name:
                name = input("Insert New Chain Name: ")
                print()
                for blockchain in blockchains:
                    if blockchain.name == name:
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
        # Check to see if Chain is empty
        if not self.tail_block:
            new_block = Block(new_block_sender, new_block_money, new_block_receiver)
        # If it's not empty, the new block's "previous block" will be the existing "tail block"
        else:
            new_block = Block(new_block_sender, new_block_money, new_block_receiver, self.tail_block)
        # Update "Tail Block" to the newly created block
        self.tail_block = new_block

    def view(self):
        current_block = self.tail_block
        while True:
            print(current_block)
            if not current_block.previous_block:
                break
            else:
                current_block = current_block.previous_block


blockchains = []

while True:
    user_input_1 = input("""---------- MENU ----------
1 - View Chains
2 - New Chain

Insert Command: """)
    print()
    # If user selects to view chains
    if user_input_1 == "1":
        # If no chains exist
        if not blockchains:
            print("There are no existing blockchains.\n")
        # If chains do exist
        else:
            for blockchain in blockchains:
                print(blockchain)
            user_input_2 = input("""---------- MENU ----------
1 - New Payment
2 - View Payments

Insert Command: """)
            print()
            if user_input_2 == "1":
                print("----- NEW PAYMENT -----")
                user_input_3 = input("Insert Your Name: ")
                user_input_4 = input("Insert Value: ")
                user_input_5 = input("Insert Recipient: ")
                tonicha.add_block(user_input_3, user_input_4, user_input_5)
                print()
            elif user_input_2 == "2":
                print("----- VIEW PAYMENTS -----\n")
                tonicha.view()
            else:
                print("Invalid Command.\n")
    # If User selects to create a new chain
    elif user_input_1 == "2":
        new_chain = Blockchain()
    
        
                       
