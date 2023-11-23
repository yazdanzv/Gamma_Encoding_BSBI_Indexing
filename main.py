from preprocessing import PreProcess
from bsbi_indexing import BSBI_Indexer

a = PreProcess()
print(a.tokens_with_elimination)
print(len(a.tokens_with_elimination))
print(sum(len(row) for row in a.tokens_with_elimination))
b = BSBI_Indexer(a.tokens_with_elimination)
b.block_builder()
print(b.block_paths)
b.merge_blocks()
