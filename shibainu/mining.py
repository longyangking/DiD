import numpy as np 
import sys
from multiprocessing.dummy import Pool

class Worker:
    def __init__(self, block, cores=4):
        self.block = block

    def start(self):
        num = -sys.maxsize


        

    def mine(self,num):
        string = "{index}{timestamp}{data}{previous_hash}{num}".format(
                index=self.block.get_index(),
                timestamp=self.block.get_timestamp(),
                data=self.block.get_data(),
                previous_hash=self.block.get_previous_hash(),
                num=num
            )

        sha = hashlib.sha256()
        sha.update(string.encode("utf8"))
        _hash = sha.hexdigest()
    
