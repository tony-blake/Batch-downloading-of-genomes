
from Bio import SeqIO

# Read all accession numbers into the list.
accession_numbers = [line.strip() for line in open('clipped')]

# Iterate over each genbank record.
fh = open('all.gb')
for gb_record in SeqIO.parse(fh,'genbank'):
    acc = gb_record.annotations['accessions'][0]
    organism = gb_record.annotations['organism']
    tax_line = ("; ").join(gb_record.annotations['taxonomy'])
    if acc in accession_numbers:
        print acc, organism, tax_line
