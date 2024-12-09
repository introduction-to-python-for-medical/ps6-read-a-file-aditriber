def create_codon_dict(file_path):
    with open(file_path) as file:
        rows = file.readlines()
    
    d = {}
    for row in rows:
        cells = row.strip().split('\t')
        codon = cells[0]
        amino_acid = cells[2]
        d[codon] = amino_acid
        
    return d



