import copy
import json


class BSBI_Indexer:
    def __init__(self, doc_tokens: list,
                 block_size: int = 20):  # Input parameters are size of block and the list of tokens in documents
        self.block_size = block_size
        self.doc_tokens = doc_tokens
        self.block_paths = []  # Path of the blocks

    def block_builder(self):
        doc_tokens_size = sum(len(lst) for lst in self.doc_tokens)
        count1 = 0  # Counter to break when all tokens iterated
        count2 = 0  # Counter to save the block with size given by user
        block = dict()  # Dictionary that holds block as a dictionary
        for i in range(len(self.doc_tokens)):  # Iterate on all documents
            for j in range(len(self.doc_tokens[i])):  # Iterate on all tokens
                count1 += 1
                if count1 >= doc_tokens_size:  # Reach at the end of the tokens
                    break
                if self.doc_tokens[i][j] in block.keys():  # Add corresponding doc id to the posting list
                    block[self.doc_tokens[i][j]].append(i + 1)
                else:
                    block[self.doc_tokens[i][j]] = [i + 1]
                count2 += 1
                if count2 >= self.block_size:  # Check when we should go into the next block
                    temp = copy.deepcopy(block)
                    block_number = len(self.block_paths) + 1
                    path = f'.\\Blocks\\Block_no{block_number}.txt'  # Path to saves blocks on the disk
                    with open(path, 'w') as f:
                        f.write("")
                    with open(path, 'w') as f:
                        json.dump(temp, f)
                    self.block_paths.append(path)  # Append the path to the list of paths
                    block.clear()
                    count2 = 0

    def merge_blocks(self):
        merged_block = dict()  # Final merged inverted index
        for i in range(len(self.block_paths)):  # Reads all the blocks from disk
            with open(self.block_paths[i], 'r') as f:
                temp_dic: dict = json.load(f)
                for j in range(len(list(temp_dic.keys()))):  # Merge them together in merged_blocks
                    if list(temp_dic.keys())[j] in merged_block.keys():
                        merged_block[list(temp_dic.keys())[j]].extend(temp_dic[list(temp_dic.keys())[j]])
                    else:
                        merged_block[list(temp_dic.keys())[j]] = temp_dic[list(temp_dic.keys())[j]]
        for i in range(len(list(temp_dic.keys()))):  # Sort the posting lists
            temp_dic[list(temp_dic.keys())[i]].sort()
        with open(".\\Blocks\\MergedBlock.txt", 'w') as f:  # Saves the final merged version on disk
            json.dump(merged_block, f)
        return merged_block
