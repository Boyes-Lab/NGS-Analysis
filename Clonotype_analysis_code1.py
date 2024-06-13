import re
import os

# Define the two motifs you want to search for
motif1 = ""
motif2 = ""

# Function to check if both motifs are present in a sequence
def has_motifs(sequence):
    return re.search(motif1, sequence) and re.search(motif2, sequence)

# Input FASTQ file path
input_file = 

# Determine the output file path in the same directory as the input file
output_file = os.path.splitext(input_file)[0] + "_filtered.fasta"

# Open the input FASTQ file for reading
with open(input_file, "r") as f:
    lines = f.readlines()

# Initialize variables to store sequence data
current_header = ""
current_sequence = ""
output_sequences = []

# Iterate through the FASTQ file
for line in lines:
    line = line.strip()
    if line.startswith("@"):
        # This is a header line
        current_header = line
    elif current_header and not line.startswith("+"):
        # This is a sequence line
        current_sequence += line
    elif line.startswith("+") and current_sequence:
        # This is a quality line
        if has_motifs(current_sequence):
            output_sequences.append((current_header, current_sequence))
        # Reset sequence data
        current_header = ""
        current_sequence = ""

# Write the sequences with both motifs to a new FASTA file in the same directory
with open(output_file, "w") as f:
    for header, sequence in output_sequences:
        f.write(f">{header}\n{sequence}\n")

print(f"Found {len(output_sequences)} sequences with both motifs. Saved to {output_file}")
