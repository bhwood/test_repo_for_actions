def dna_pairs(dna_string):
    pairs = {"G": "C", "C": "G", "T": "A", "A": "T"}
    return [[check, pairs[check]] for check in dna_string.upper() if check in pairs]
