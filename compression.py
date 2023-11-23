from gamma_coding import GammaCoding
import json


class Compress:
    def __init__(self, inverted_index: dict):
        self.inverted_index = inverted_index
        self.compressed_inverted_index = dict()

    def compress(self):
        for i in range(len(list(self.inverted_index.keys()))):
            self.compressed_inverted_index[list(self.inverted_index.keys())[i]] = \
                GammaCoding.encode_list(self.inverted_index[list(self.inverted_index.keys())[i]])

    def save_compress(self):
        with open('.\\Blocks\\compressed_index.txt', 'w') as f:
            json.dump(self.compressed_inverted_index, f)
