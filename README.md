# Clonotype_analysis_code1.py

This Python script filters sequences from a FASTQ file based on the presence of two specified motifs. If both motifs are present in a sequence, the sequence is written to a new FASTA file.

## Prerequisites

- Python 3.x

## Usage

1. Ensure you have Python installed on your system.
2. Prepare your input FASTQ file.
3. Define the motifs you want to search for in the script.
4. Provide the path to the input FASTQ file.
5. Run the script.

### Script Parameters

- `motif1`: The first motif to search for in the sequences.
- `motif2`: The second motif to search for in the sequences.
- `input_file`: Path to the input FASTQ file.

### Example

If your input file is `sample.fastq` and you are looking for motifs `AGCT` and `TCGA`, you should set `motif1 = "AGCT"` and `motif2 = "TCGA"`, and `input_file = "sample.fastq"`. For clonotype identifcation, these motifs will be the reference 5 bp sequence in the IGLJ region of interest and the reference 5 bp sequence in the IGLV region of interest, around 20 bp away from where the V-J Junction will be. 

### Output

The script will output a new FASTA file in the same directory as the input FASTQ file, with `_filtered` appended to the original file name.

For example, if your input file is `sample.fastq`, the output file will be `sample_filtered.fasta`.

### Running the Script

1. Modify the script to set `motif1`, `motif2`, and `input_file`.
2. Run the script:

```bash```
Clonotype_analysis_code1.py


# Clonotype_analysis_code2.py

**This Python script extracts sequences between specified motifs from a filtered FASTA file and counts their occurrences. It then saves the results in an Excel file.**

## Requirements

**- Python 3.x**
**- pandas**
**- collections.defaultdict**

## Usage

**1. Input:**
   - Place your filtered FASTA file (`filtered.fasta`) in the same directory as `Clonotype_analysis_code2.py`.
   - Specify the motifs `motif1` and `motif2` in the script that you want to search for.

**2. Running the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing `Clonotype_analysis_code2.py`.
   - Run the script using Python:
     ```bash
      Clonotype_analysis_code2.py
     ```

**3. Output:**
   - The script will generate an Excel file (`filtered_output.xlsx`) containing two columns:
     - `Sequence`: Extracted sequences between `motif1` and `motif2`.
     - `Frequency`: Number of occurrences of each sequence.

**4. Example:**
   - Suppose `motif1 = "START"` and `motif2 = "END"`. The script will find all sequences between these motifs in your FASTA file and count their occurrences. For clonotype identifcation, these motifs will be the reference 5 bp sequence in the IGLJ region of interest and the reference 5 bp sequence in the IGLV region of interest, around 20 bp away from where the V-J Junction will be

**5. Notes:**
   - Ensure the filtered FASTA file (`filtered.fasta`) is correctly formatted and contains sequences with headers starting with `>`.
   - Modify `motif1` and `motif2` variables in the script according to your specific motifs of interest.

## License

**This project is licensed under the MIT License - see the LICENSE file for details.**







