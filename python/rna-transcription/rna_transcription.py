# Given a DNA strand, its transcribed RNA strand is formed by replacing
# each nucleotide with its complement:
#
# * `G` -> `C`
# * `C` -> `G`
# * `T` -> `A`
# * `A` -> `U`
#
# Your function will nee:d to be able to handle invalid inputs by raising a `ValueError` with a meaningful message.
dna_nucleotides = ['G', 'C', 'T', 'A']
rna_nucleotides = ['C', 'G', 'A', 'U']
dna_to_rna = dict(zip(dna_nucleotides, rna_nucleotides))

def to_rna(dna_strand):
    try:
        return ''.join([dna_to_rna[x] for x in dna_strand])
    except KeyError:
        "The DNA strand contains other nucleotides than G, C, T or A."
