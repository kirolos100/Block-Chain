import hashlib

class block():
    def __init__(self, data, prev_hash):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = hashlib.sha256()
        self.nonce = 0
    
    def __str__(self): #whenever you pass this object as a string this will be called
        return "{}{}{}".format(self.prev_hash.hexdigest(), self.data, self.nonce) #passing stream of bits 
    
    #block mining
    def mine(self, difficulty):

        self.hash.update(str(self).encode('utf-8')) #get the first value from the hash
        while int(self.hash.hexdigest(), 16) > 2**(256-difficulty): #This loop will run until it finds the suitable hash for the difficulty
            self.nonce += 1
            self.hash = hashlib.sha256() #reset
            self.hash.update(str(self).encode('utf-8'))