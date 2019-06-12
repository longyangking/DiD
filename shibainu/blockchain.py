import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self._index = index
        self._timestamp = timestamp
        self._data = data
        self._previous_hash = previous_hash
        
        string = "{index}{timestamp}{data}{previous_hash}".format(
                index=self._index,
                timestamp=self._timestamp,
                data=self._data,
                previous_hash=self._previous_hash
            )

        sha = hashlib.sha256()
        sha.update(string.encode("utf8"))
        self._hash = sha.hexdigest()

    def get_index(self):
        return self._index

    def get_timestamp(self):
        return self._timestamp

    def get_data(self):
        return self._data
    
    def get_previous_hash(self):
        return self._previous_hash

    def get_hash(self):
        return self._hash

    def to_string(self):
        return '''
Block:
    Index : {index}
    Time Stamp : {timestamp}
    Hash Value : {hash_value}
    Data : {data}
    '''.format(
                index=self._index,
                timestamp=self._timestamp,
                hash_value=self._hash,
                data=self._data
            )


class BlockChain:
    def __init__(self, root_hash=None):
        self._root_hash = None
        if root_hash is not None:
            self._root_hash = root_hash

        self.blockchain = list()
        
    def add_block(self, data):
        timestamp = datetime.datetime.now()
        previous_hash = self._root_hash
        index = len(self.blockchain)
        block = Block(
            index=index,
            timestamp=timestamp,
            data=data,
            previous_hash=previous_hash
        )

        self.blockchain.append(block)
        self._root_hash = block.get_hash()

    def find_block(self,hash_value):
        n_blocks = len(self.blockchain)
        for i in range(n_blocks):
            if self.blockchain[i].get_hash() == hash_value:
                return self.blockchain[i]
                
    def __str__(self):
        n_blocks = len(self.blockchain)
        root_hash = self._root_hash
        string = ""
        for index in range(n_blocks):
            block = self.find_block(hash_value=root_hash)
            string += block.to_string()
            root_hash = block.get_previous_hash()
        return string