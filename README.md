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

# WGS ESC analysis

README

This workflow consists of two scripts, both as Jupyter notebooks: <br/> 

(1) WGS_align_to_hg19.ipynb <br/> 
(2) Filter_WGS_for_ESCs.ipynb <br/> 

## 1. WGS_align_to_hg19:

This script extracts FASTQ files from SRF or BAM files downloaded from the European Genome-phenome Archive (EGA) (https://ega-archive.org/), aligns them to the hg19 genome assembly using Bowtie2 and filters the resulting file for reads that originate from the immunoglobulin and T-cell receptor loci.

Requirements: <br/> 
Python 3 <br/> 
Jupyter notebook (pip install jupyter) <br/> 
Bowtie2 (should be installed and present in PATH, https://sourceforge.net/projects/bowtie-bio/files/bowtie2/) <br/> 
Human / hg19 bowtie2 index (Available at: https://benlangmead.github.io/aws-indexes/bowtie) <br/> 
Samtools (should be installed and present in PATH, https://sourceforge.net/projects/samtools/files/samtools/) <br/> 
Staden Package (Available at: https://sourceforge.net/projects/staden/) <br/> 

This workflow was run on an Ubuntu 18.04 LTS virtual machine running on a 2018 Intel Mac mini (Intel i7-8700B) with 32 GB RAM. Bowtie version 2.4.0, SAMtools version 1.10 and Staden Package version 2.0.0b11-2016 was used.

Usage:
Load the notebook file in Jupyter notebook

Modify the paths and arguments in cell 1 as appropriate: <br/> 
Line 15: folder path with patient SRF or BAM files (Downloaded from EGA) <br/> 
Line 20: folder path containing Bowtie2 hg19 index <br/> 
Line 22: number of CPU threads to use <br/> 
Line 25: amount of memory to use for alignment (total) <br/> 
Line 26: amount of memory to use for samtools (per thread) <br/> 

Run Cell 1 <br/> 
If SRF files are used as input, run cell 2 <br/> 
if BAM files are used as input, run cell 3 <br/> 
Run cell 4 to run Bowtie2 alignment (takes several hours, depending on hardware) <br/> 
Run cell 5 to run Samtools (to sort and index the aligned output from Bowtie2) <br/> 
Run cell 6 to extract reads only from the immunoglobulin and T-cell receptor loci <br/> 

Use the output BAM files as input for notebook 2 (Filter_WGS_for_ESCs)


## 2. Filter_WGS_for_ESCs

This script using the BAM files produced by notebook 1 (WGS_align_to_hg19). Reads are filtered for discordant reads that would be expected if paired end reads originated from an ESC, for example:
Expected paired end reads from the genome would align like this: 
---> ~500bp <--- with each read pointing towards each other with a ~500 bp gap in between

If an ESC was generated from deletional recombination, reads would be expected to point away from each other, with a much larger gap in between: <---- >1kb ----> 

Pysam/Samtools is used to extract paired reads with SAM flags 81 and 161 or SAM flags 97 and 145 (https://broadinstitute.github.io/picard/explain-flags.html) to extact discordant reads which would be indicative of an ESC


Requirements: <br/> 
Python 3 <br/> 
Jupyter notebook (pip install jupyter) <br/> 
pysam (tested with version v0.15.4, install using: 'pip install pysam', further information available at https://pysam.readthedocs.io/en/latest/ and https://github.com/pysam-developers/pysam/releases) <br/> 
blastn (tested with version 2.12.0, available from https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.12.0/) <br/> 
blast database of RSS regions in IG and TCR loci (files in blast_db folder in this repository) <br/> 

Usage:
Load the notebook file in Jupyter notebook

Modify the paths as appropriate: <br/> 
Cell 1, Line 14: Full path to blast database (blast_db/VDJ_RSS_extended.fasta) <br/> 
Cell 2, Line 2: Folder path containing input BAM files (output from notebook 1 (WGS_align_to_hg19.ipynb)) <br/>  

Run cells 1-3 in order. Output is a tsv (tab separated values) file containing reads that indicate potential ESCs. <br/> 


## License

**This project is licensed under the MIT License - see the LICENSE file for details.**







