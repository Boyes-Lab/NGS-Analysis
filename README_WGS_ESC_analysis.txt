WGS ESC analysis

README

This workflow consists of two scripts, both as Jupyter notebooks:

(1) WGS_align_to_hg19.ipynb
(2) Filter_WGS_for_ESCs.ipynb

1. WGS_align_to_hg19:

This script extracts FASTQ files from SRF or BAM files downloaded from the European Genome-phenome Archive (EGA) (https://ega-archive.org/), aligns them to the hg19 genome assembly using Bowtie2 and filters the resulting file for reads that originate from the immunoglobulin and T-cell receptor loci.

Requirements:
Python 3
Jupyter notebook (pip install jupyter)
Bowtie2 (should be installed and present in PATH, https://sourceforge.net/projects/bowtie-bio/files/bowtie2/)
Human / hg19 bowtie2 index (Available at: https://benlangmead.github.io/aws-indexes/bowtie)
Samtools (should be installed and present in PATH, https://sourceforge.net/projects/samtools/files/samtools/)
Staden Package (Available at: https://sourceforge.net/projects/staden/)

This workflow was run on an Ubuntu 18.04 LTS virtual machine running on a 2018 Intel Mac mini (Intel i7-8700B) with 32 GB RAM. Bowtie version 2.4.0, SAMtools version 1.10 and Staden Package version 2.0.0b11-2016 was used.

Usage:
Load the notebook file in Jupyter notebook

Modify the paths and arguments in cell 1 as appropriate:
Line 15: folder path with patient SRF or BAM files (Downloaded from EGA)
Line 20: folder path containing Bowtie2 hg19 index
Line 22: number of CPU threads to use
Line 25: amount of memory to use for alignment (total)
Line 26: amount of memory to use for samtools (per thread)

Run Cell 1
If SRF files are used as input, run cell 2
if BAM files are used as input, run cell 3
Run cell 4 to run Bowtie2 alignment (takes several hours, depending on hardware)
Run cell 5 to run Samtools (to sort and index the aligned output from Bowtie2)
Run cell 6 to extract reads only from the immunoglobulin and T-cell receptor loci

Use the output BAM files as input for notebook 2 (Filter_WGS_for_ESCs)


2. Filter_WGS_for_ESCs

This script using the BAM files produced by notebook 1 (WGS_align_to_hg19). Reads are filtered for discordant reads that would be expected if paired end reads originated from an ESC, for example:
Expected paired end reads from the genome would align like this: 
---> ~500bp <--- with each read pointing towards each other with a ~500 bp gap in between

If an ESC was generated from deletional recombination, reads would be expected to point away from each other, with a much larger gap in between: <---- >1kb ----> 

Pysam/Samtools is used to extract paired reads with SAM flags 81 and 161 or SAM flags 97 and 145 (https://broadinstitute.github.io/picard/explain-flags.html) to extact discordant reads which would be indicative of an ESC


Requirements:
Python 3
Jupyter notebook (pip install jupyter)
pysam (tested with version v0.15.4, install using: 'pip install pysam', further information available at https://pysam.readthedocs.io/en/latest/ and https://github.com/pysam-developers/pysam/releases)
blastn (tested with version 2.12.0, available from https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.12.0/)
blast database of RSS regions in IG and TCR loci (files in blast_db folder in this repository)

Usage:
Load the notebook file in Jupyter notebook

Modify the paths as appropriate:
Cell 1, Line 14: Full path to blast database (blast_db/VDJ_RSS_extended.fasta)
Cell 2, Line 2: Folder path containing input BAM files (output from notebook 1 (WGS_align_to_hg19.ipynb))

Run cells 1-3 in order. Output is a tsv (tab separated values) file containing reads that indicate potential ESCs.
