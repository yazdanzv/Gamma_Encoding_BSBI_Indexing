from preprocessing import PreProcess
from bsbi_indexing import BSBI_Indexer
from gamma_coding import GammaCoding

a = PreProcess()
print(a.tokens_with_elimination)
print(len(a.tokens_with_elimination))
print(sum(len(row) for row in a.tokens_with_elimination))
b = BSBI_Indexer(a.tokens_with_elimination)
b.block_builder()
print(b.block_paths)
b.merge_blocks()
c = GammaCoding()
d, e = c.decode('1110001110101011111101101111011')
