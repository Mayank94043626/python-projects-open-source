#open the original DNA sequence .txt file
inputfile="DNA_sequence_original.txt" #make sure to put your file in the right directory
f=open(inputfile,"r")
seq=f.read()
# >>>seq   #check the DNA sequence
seq=seq.replace("\n","") #you will see "\n" characters messing with our DNA sequence, so we are cleaning them off the sequence.
seq=seq.replace("\r","")
# >>>seq   #check the DNA sequence
def translate(seq):
    """
    Translate a string containing a nucleotide sequence into a string containing the corresponding sequence of amino acids .
    Nucleotides are translated in triplets using the table dictionary; each amino acid 4 is encoded with a string of length 1.
    """
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  #this table dictionary is pre-created
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein=""
    if len(seq)%3==0:
        for i in range(0,len(seq),3):
            codon=seq[i:i+3]
            protein+=table[codon]
    return protein
def read_seq(inputfile):
    with open(inputfile,"r") as f:
        seq=f.read()
    seq=seq.replace("\n","")
    seq=seq.replace("\r","")
    return seq

prt = read_seq("amino_acid_sequence_original.txt")
dna = read_seq("DNA_sequence_original.txt")
# >>>translate(dna)
# >>>translate(dna[20:938])  #try translating the DNA sequence into a protein sequence
# >>>len(translate(dna[20:938]))%3 #check, now than the translated sequence is divisible by 3 since we classified the terminal & starting codon as well
# say p = translate(dna[20:938])  , try printing >>>p & >>>prt | p = amino acid sequence prepared by us & prt = amino acid sequence from the database of NCBI
# >>>p==prt  , # = False, since _ character is read by default as an end to the string in p
p=translate(dna[20:935]) #dna[20:938] --> dna[20:935] (since, each character = tri base pair)
p==prt # True , we got our analysis correct

'''
prt==p[:-1] #False
p=translate(dna[20:938])
prt==p[:-1] #True
'''