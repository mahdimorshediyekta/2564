from Bio import SeqIO

def gbank_to_fasta(gbank_file, fasta_file):
    """
    Converts a GenBank file to a FASTA file.

    Parameters:
        gbank_file (str): Path to the input GenBank file.
        fasta_file (str): Path to the output FASTA file.
    """
    # Open the GenBank file and parse it
    with open(gbank_file, 'r') as gbk_handle, open(fasta_file, 'w') as fasta_handle:
        # Parse GenBank file and convert to FASTA
        for record in SeqIO.parse(gbk_handle, "genbank"):
            # Write the FASTA file
            SeqIO.write(record, fasta_handle, "fasta")
    print(f"Conversion complete! FASTA file saved as {fasta_file}")

# Example usage
gbank_file = "example.gbk"  # Replace with your GenBank file
fasta_file = "output.fasta"  # Replace with the desired output FASTA file
gbank_to_fasta(gbank_file, fasta_file)
