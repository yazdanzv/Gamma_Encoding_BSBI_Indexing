from preprocessing import PreProcess
from bsbi_indexing import BSBI_Indexer
from gamma_coding import GammaCoding
from compression import Compress

a = PreProcess()  # Instance of PreProcess class
print(a.tokens_with_elimination)  # Tokens with elimination (Stop words removed)
print(len(a.tokens_with_elimination))  # Length of the doc ids
print(sum(len(row) for row in a.tokens_with_elimination))  # Length of the tokens with replacements
b = BSBI_Indexer(a.tokens_with_elimination)  # Instance of BSBI_Indexer
b.block_builder()  # Builds the blocks and saves them on disk
print(b.block_paths)  # Path of the blocks
f = b.merge_blocks()  # Merge the blocks by reading them from disk and saves the final version on disk again
c = GammaCoding()  # Encode posting lists by gamma encoding method
d, e = c.decode('1110001110101011111101101111011')  # Test of decode method
print(d, e)  # Binary list and Decimal list (Compare the decimal list with the list below, results are the same)
print(c.encode_list([9, 6, 3, 59, 7]))  # Test the list encoding method
print(f)  # Print the final version of merged block
g = Compress(f)  # Instance of Compress class
g.compress()  # Compress the final version of merged block
print(g.compressed_inverted_index)  # Show the compressed inverted index
g.save_compress()  # saves the compressed inverted index on the disk

