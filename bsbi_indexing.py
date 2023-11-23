import copy
import json


class BSBI_Indexer:
    def __init__(self, doc_tokens: list, block_size: int = 20):
        self.block_size = block_size
        self.doc_tokens = doc_tokens
        self.block_paths = []

    def block_builder(self):
        doc_tokens_size = sum(len(lst) for lst in self.doc_tokens)
        count1 = 0
        count2 = 0
        block = dict()
        for i in range(len(self.doc_tokens)):
            for j in range(len(self.doc_tokens[i])):
                count1 += 1
                if count1 >= doc_tokens_size:
                    break
                if self.doc_tokens[i][j] in block.keys():
                    block[self.doc_tokens[i][j]].append(i + 1)
                else:
                    block[self.doc_tokens[i][j]] = [i + 1]
                count2 += 1
                if count2 >= self.block_size:
                    temp = copy.deepcopy(block)
                    block_number = len(self.block_paths) + 1
                    path = f'.\\Blocks\\Block_no{block_number}.txt'
                    with open(path, 'w') as f:
                        f.write("")
                    with open(path, 'w') as f:
                        json.dump(temp, f)
                    self.block_paths.append(path)
                    block.clear()
                    count2 = 0

    def merge_blocks(self):
        merged_block = dict()
        for i in range(len(self.block_paths)):
            with open(self.block_paths[i], 'r') as f:
                temp_dic: dict = json.load(f)
                for j in range(len(list(temp_dic.keys()))):
                    if list(temp_dic.keys())[j] in merged_block.keys():
                        merged_block[list(temp_dic.keys())[j]].extend(temp_dic[list(temp_dic.keys())[j]])
                    else:
                        merged_block[list(temp_dic.keys())[j]] = temp_dic[list(temp_dic.keys())[j]]
        for i in range(len(list(temp_dic.keys()))):
            temp_dic[list(temp_dic.keys())[i]].sort()
        with open(".\\Blocks\\MergedBlock.txt", 'w') as f:
            json.dump(merged_block, f)
        return merged_block

