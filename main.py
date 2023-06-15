from block import block
from chain import chain

difficulty = 20

chain = chain(difficulty)
it = 0

while(1):
    data =input("Enter smth to the chain: ")
    chain.add_to_pool(data)
    chain.mine()
    if it % 5 == 0:
        print(chain.blockslist[it])
    it += 1