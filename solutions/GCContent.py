from Bio import SeqIO
from Bio.SeqUtils import GC

seqid = ""
maxcount = 0
for seq_record in SeqIO.parse("data.txt", "fasta"):
    if maxcount < GC(seq_record.seq):
        maxcount = GC(seq_record.seq)
        seqid = seq_record.id

print(seqid + "\n" + str(round(maxcount, 6)))