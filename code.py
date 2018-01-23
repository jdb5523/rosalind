from Bio import SeqIO
from decimal import *

seqid = ""
seq = ""
maxcount = 0
for seq_record in SeqIO.parse("data.txt", "fasta"):
    var = str(seq_record.seq).count("C")
    var += str(seq_record.seq).count("G")
    if var > maxcount:
        maxcount = var / len(str(seq_record.seq))
        seqid = seq_record.id
        seq = seq_record.seq

maxcount = float(maxcount * 100)
format(maxcount, '.2f')
print(seqid + "\n" + str(maxcount))
