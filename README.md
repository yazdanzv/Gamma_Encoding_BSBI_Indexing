# Gamma_Encoding_BSBI_Indexing

## Code guide

`main.py` demonstrates block-based inverted indexing and compression. `preprocessing.py` normalizes documents, `bsbi_indexing.py` creates and merges index blocks, `gamma_coding.py` encodes integer lists, and `compression.py` gap-encodes posting lists before gamma coding. `document_collection_builder.py` creates the sample documents. Run from the repository root after preparing the `Documents/` and `Blocks/` directories expected by the scripts. Some file paths use Windows separators and may need adjustment on other operating systems.
