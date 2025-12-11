codon_table = {
    "ATG": "Methionine",
    "GCG": "Alanine",
    "TCC": "Serine",
    "TAT": "Tyrosine",
    "CGT": "Arginine"
}
dna_sequence = "ATGCGTTATGCG"
def dna_seq(table, dna_sequence):
    
    protein_list = []
    code_list = []

    for i in range(0, len(dna_sequence), 3):
        code_list.append(dna_sequence[i:i+3])

    for code in code_list:
        if code in table:
            protein_list.append(table[code])
    print(f"Sequence: {dna_sequence}")
    print(f"Protein: {"-".join(protein_list)}")

dna_seq(codon_table, dna_sequence)
