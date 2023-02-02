import hashlib
from datetime import datetime


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = datetime.now()
        self.data = data
        if previous_hash is None:
            self.previous_hash = 0
        else:
            self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next = None

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()


class LinkedList:

    def __init__(self):
        self.head = None  # Keep Track of head of chain
        # Tracking next block
        self.tail = None  # Keep Track of last Item in Chain

    def add_block(self, data, previous_hash=None):
        # Creating block of Data for chain
        block = Block(data, previous_hash)

        if self.head is None:
            self.head = block
            self.tail = self.head
            return

        current_node = self.head
        while current_node:
            current_node = current_node.next

        current_node = block
        self.tail = current_node
        return

    # This brings latest block hash which will become previous hash of new block
    def get_hash_previous_block(self):
        return self.tail.hash


if __name__ == '__main__':
    blockchain = LinkedList()
    # Adding First Block and printing
    blockchain.add_block('Some Information on Block 0')
    print('Head of blockchain', blockchain.head.data)
    print('Tail of blockchain', blockchain.tail.data)
    print('Previous hash', blockchain.tail.previous_hash)
    print('Hash', blockchain.tail.hash)
    print('-' * 50)
    # adding second block fo data
    blockchain.add_block('Some Information on Block 1', blockchain.get_hash_previous_block())
    print('Head of blockchain', blockchain.head.data)
    print('Tail of blockchain', blockchain.tail.data)
    print('Previous hash', blockchain.tail.previous_hash)
    print('Hash', blockchain.tail.hash)
    print('-' * 50)

    # Adding 3rd block of data
    blockchain.add_block('Some Information on Block 2', blockchain.get_hash_previous_block())
    print('Head of blockchain', blockchain.head.data)
    print('Tail of blockchain', blockchain.tail.data)
    print('Previous hash', blockchain.tail.previous_hash)
    print('Hash', blockchain.tail.hash)
    print('-' * 50)
