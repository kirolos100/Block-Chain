import hashlib
from block import block

class chain():
    def __init__(self, difficulty):

        self.difficulty = difficulty
        self.blockslist = [] #as we mine blocks it will be added to list
        self.pool = [] #The waiting lobby before getting mined then going to the blocklist
        self.create_init_block()

    #test if the block satisfy the rules
    def block_test(self, block):

        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        x = (self.blockslist[-1].hash) == block.prev_hash
        return block.hash.hexdigest() == hash.hexdigest() and int(hash.hexdigest(), 16) < 2**(256 - self.difficulty) and x
    
    def add_to_chain(self, block):
        if(self.block_test(block)):
            self.blockslist.append(block)
    
    #add data to the pool
    def add_to_pool(self, data):
        self.pool.append(data)

    def create_init_block(self):
        h = hashlib.sha256()
        h.update(''.encode('utf-8'))
        origin = block("origin", h)
        origin.mine(self.difficulty)
        self.blockslist.append(origin)


    def mine(self):
        if len(self.pool) > 0:
            data = self.pool.pop()
            nblock = block(data, self.blockslist[-1].hash)
            nblock.mine(self.difficulty)
            self.add_to_chain(nblock)
        

