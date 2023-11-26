from gamma_coding import GammaCoding
import json
import copy


class Compress:
    def __init__(self, inverted_index: dict):
        self.inverted_index = inverted_index  # Inverted index dictionary
        self.compressed_inverted_index = dict()  # Compressed version of inverted index
        self.gap_index = dict()  # Gap Inverted Index

    def build_gap_index(self):
        for i in range(len(list(self.inverted_index.keys()))):
            # Build Gap Inverted Index
            self.gap_index[list(self.inverted_index.keys())[i]] = [self.inverted_index[list(self.inverted_index.keys())[i]][0]]
            for j in range(1, len(self.inverted_index[list(self.inverted_index.keys())[i]])):
                gap = self.inverted_index[list(self.inverted_index.keys())[i]][j] - self.inverted_index[list(self.inverted_index.keys())[i]][j-1]
                self.gap_index[list(self.inverted_index.keys())[i]].append(copy.deepcopy(gap))

    def compress(self):  # Method to compress the inverted index
        for i in range(len(list(self.inverted_index.keys()))):
            # Convert the list of integral numbers to the code by gamma coding method
            self.compressed_inverted_index[list(self.inverted_index.keys())[i]] = \
                GammaCoding.encode_list(self.inverted_index[list(self.inverted_index.keys())[i]])

    def save_compress(self):  # Saves the compressed version of inverted index on disk
        with open('.\\Blocks\\compressed_index.txt', 'w') as f:
            json.dump(self.compressed_inverted_index, f)
