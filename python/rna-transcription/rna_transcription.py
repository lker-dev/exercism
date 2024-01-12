def to_rna(dna_strand: str) -> str:
    substitutions = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return ''.join([substitutions[nucleo] for nucleo in dna_strand])
