import sys
sys.path.append("..")

from shibainu import blockchain

if __name__=="__main__":
    blockchain_demo = blockchain.BlockChain()
    n_blocks = 10
    for index in range(n_blocks):
        blockchain_demo.add_block(data="Hello BlockChain {index}".format(index=index))
    print(blockchain_demo)