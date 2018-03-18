import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self._timestamp = timestamp
        self._data = data
        self._previous_hash = previous_hash
        
        string = "{timestamp}{data}{previous_hash}".format(
                timestamp=self._timestamp,
                data=self._data,
                previous_hash=self._previous_hash
            )

        sha = hashlib.sha256()
        sha.update(string.encode("utf8"))
        self._hash = sha.hexdigest()

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
    Time Stamp : {timestamp}
    Hash Value : {hash_value}
    Data : {data}
    '''.format(
                timestamp=self._timestamp,
                hash_value=self._hash,
                data=self._data
            )


class BlockChain:
    def __init__(self, root_hash=None):
        self._root_hash = None
        if root_hash is not None:
            self._root_hash = root_hash

        self.blockchains = list()
        
    def add_block(self, data):
        timestamp = datetime.datetime.now()
        previous_hash = self._root_hash
        block = Block(
            timestamp=timestamp,
            data=data,
            previous_hash=previous_hash
        )

        self.blockchains.append(block)
        self._root_hash = block.get_hash()

    def __str__(self):
        n_blocks = len(self.blockchains)
        root_hash = self._root_hash
        string = ""
        for index in range(n_blocks):
            for i in range(n_blocks):
                if self.blockchains[i].get_hash()==root_hash:
                    string += "\n\rBlockChain Index : {index}".format(index=index)
                    string += self.blockchains[i].to_string()
                    root_hash = self.blockchains[i].get_previous_hash()
                    break
        return string