import pandas as pd
from collections import defaultdict
import os

# Input filtered FASTA file path
filtered_file = 
# Output Excel file path
output_excel_file = os.path.splitext(filtered_file)[0] + "_output.xlsx"

# Define the two motifs you want to search for
motif1 = ""
motif2 = ""

# Function to extract sequences between motifs
def extract_sequences_between_motifs(sequence):
    sequences = []
    start = 0
    while True:
        start = sequence.find(motif1, start)
        if start == -1:
            break
        end = sequence.find(motif2, start)
        if end == -1:
            break
        sequences.append(sequence[start + len(motif1):end])
        start = end + len(motif2)
    return sequences

# Initialize a dictionary to count unique sequences
sequence_counts = defaultdict(int)

# Read the filtered FASTA file and process sequences
with open(filtered_file, "r") as f:
    current_sequence = ""
    for line in f:
        if line.startswith(">"):
            # New header, process the previous sequence
            if current_sequence:
                sequences_between_motifs = extract_sequences_between_motifs(current_sequence)
                for seq in sequences_between_motifs:
                    sequence_counts[seq] += 1
            current_sequence = ""
        else:
            current_sequence += line.strip()

# Process the last sequence in the file
if current_sequence:
    sequences_between_motifs = extract_sequences_between_motifs(current_sequence)
    for seq in sequences_between_motifs:
        sequence_counts[seq] += 1

# Create a DataFrame to store the results
result_df = pd.DataFrame({
    "Sequence": list(sequence_counts.keys()),
    "Frequency": [sequence_counts[seq] for seq in sequence_counts.keys()]
})

# Write the DataFrame to an Excel file
result_df.to_excel(output_excel_file, index=False)

print(f"Results saved to {output_excel_file}")
