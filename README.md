# L1Farm Database

![License](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Citation](https://img.shields.io/badge/Publication-In%20Preparation-lightgrey)](https://doi.org/PAPER_DOI)

This repository contains the official datasets for **L1Farm**, a comprehensive database of LINE-1 (L1) retrotransposon annotations. These datasets were generated as part of the study published in the *Journal of Genetics and Genomics*.

L1Farm provides high-resolution annotations of L1 elements across the human reference genome (hg38) and two individual diploid genomes, aiming to overcome the limitations of standard repeat annotation methods.

---

## Database Description

The L1Farm database is organized into 12 tab-separated value (`.tsv`) files. The naming convention for each file follows a consistent structure to help you identify its content:

**`L1Farm_[Dataset]_[Cutoff]_[Genome].tsv`**

### File Naming Convention

#### 1. Dataset Type (`[Dataset]`)
This indicates the type of annotation provided in the file:
-   **`RG-L1`**: **R**egions in **G**enome. Annotations of individual L1 regions (5'UTR, ORF1, intron, ORF2, 3'UTR) found in the **hg38 reference genome**.
-   **`FL-L1`**: **F**ull-**L**ength in **G**enome. Annotations of assembled, full-length L1 elements found in the **hg38 reference genome**.
-   **`AR-L1`**: **A**llele-level **R**egions. Annotations of individual L1 regions found in **individual diploid genomes**.
-   **`AF-L1`**: **A**llele-level **F**ull-length. Annotations of assembled, full-length L1 elements found in **individual diploid genomes**.

#### 2. Quality Cut-off (`[Cutoff]`)
This defines the minimum sequence identity used for filtering the annotations:
-   **`BC`**: **B**est **C**onserved. L1 elements with a sequence identity of **≥ 70%** compared to the consensus sequence.
-   **`HC`**: **H**ighly **C**onserved. L1 elements with a sequence identity of **≥ 99%**.

#### 3. Genome Origin (`[Genome]`)
This specifies the source genome for the annotations:
-   **`HG38`**: Human Reference Genome (GRCh38/hg38).
-   **`Asian`**: Individual Korean Genome (assembly KOREF_20090224).
-   **`Caucasian`**: Individual Caucasian Genome (J. Craig Venter; assembly HuRef).

---

## Data Structure and Columns

All `.tsv` files share a similar structure. The following 12 columns describe the annotations for the region-level datasets (`RG-L1` and `AR-L1`). Full-length datasets (`FL-L1` and `AF-L1`) contain a subset of these columns, primarily describing the overall element.

| Column | Header (Implied) | Description                                                  |
|:------:|:-----------------|:-------------------------------------------------------------|
| 1      | Chromosome       | Chromosome name.                                             |
| 2      | Start            | Starting position of the feature in the chromosome (1-based).|
| 3      | End              | Ending position of the feature in the chromosome.            |
| 4      | Subfamily        | Name of the L1 subfamily (e.g., L1HS, L1PA2).                |
| 5      | Region           | Name of the L1 subfamily region (5'UTR, ORF1, etc.).         |
| 6      | Strand           | Strand (+ or -).                                             |
| 7      | Mismatches       | Number of mismatches in base pairs (bp).                     |
| 8      | Deletions        | Number of deletions in base pairs (bp).                      |
| 9      | Insertions       | Number of insertions in base pairs (bp).                     |
| 10     | Locus Length     | Length of the annotated locus in base pairs (bp).            |
| 11     | Identity         | Sequence identity (0.70-1.00 or 0.99-1.00).                  |
| 12     | Similarity       | Sequence similarity (0.90-1.00).                             |

---

## How to Download

You can download the entire database by:
1.  Clicking the green **`Code`** button and selecting **`Download ZIP`**.
2.  Or, if you have Git installed, cloning the repository:
    ```sh
    git clone https://github.com/your-username/l1farm.git
    ```

---

## Usage Example: Extracting L1 Sequences with a Python Script

A common task in genomics is to move from annotation to sequence-level analysis. This example demonstrates how to use the L1Farm database to extract the actual DNA sequences of specific L1 elements from a reference genome FASTA file.

This script will answer the question: **"What are the nucleotide sequences of the first 5 full-length, highly conserved (HC) L1HS elements on the X chromosome?"**

### Prerequisites
-   **Python 3** with the following libraries installed:
    -   `pandas`: For easy data manipulation (`pip install pandas`).
    -   `pysam`: A powerful library for reading genomic data files like FASTA and BAM (`pip install pysam`).
-   A **reference genome file** in FASTA format (e.g., `hg38.fa`).
-   The FASTA file must be **indexed** by `samtools faidx` (`samtools faidx hg38.fa`), which creates an `.fai` file.

### Step 1: Prepare Your Environment

Ensure you have the L1Farm TSV file (`L1Farm_FLL1_HC_HG38.tsv`) and your indexed genome (`hg38.fa` and `hg38.fa.fai`) in your working directory.

### Step 2: Python Script to Extract Sequences

Create a Python script named `extract_l1_sequences.py` with the following content:

```python
import pandas as pd
import pysam

# --- Configuration ---
L1FARM_FILE = 'L1Farm_FLL1_HC_HG38.tsv'
GENOME_FASTA = 'hg38.fa'
TARGET_CHROMOSOME = 'chrX'
TARGET_SUBFAMILY = 'L1HS'
LIMIT = 5 # Number of sequences to extract

# --- Column names for the FL-L1 dataset ---
# A simplified list for this example
COLUMN_NAMES = ['Chromosome', 'Start', 'End', 'Subfamily']

def extract_l1_sequences():
    """
    Loads L1Farm data, filters it, and extracts corresponding DNA sequences
    from a reference FASTA file.
    """
    # 1. Load the L1Farm data
    try:
        df = pd.read_csv(L1FARM_FILE, sep='\t', header=None, usecols=, names=COLUMN_NAMES)
    except FileNotFoundError:
        print(f"Error: L1Farm file not found at '{L1FARM_FILE}'")
        return

    # 2. Filter for the L1 elements of interest
    filtered_df = df[
        (df['Chromosome'] == TARGET_CHROMOSOME) &
        (df['Subfamily'] == TARGET_SUBFAMILY)
    ].head(LIMIT)

    if filtered_df.empty:
        print(f"No elements found for {TARGET_SUBFAMILY} on {TARGET_CHROMOSOME}.")
        return

    print(f"Found {len(filtered_df)} elements to extract. Retrieving sequences...")

    # 3. Open the indexed genome FASTA file
    try:
        fasta_file = pysam.FastaFile(GENOME_FASTA)
    except FileNotFoundError:
        print(f"Error: Genome FASTA file not found at '{GENOME_FASTA}'.")
        print("Please ensure the file exists and is indexed (`samtools faidx`).")
        return

    # 4. Iterate through the filtered elements and fetch sequences
    for index, row in filtered_df.iterrows():
        chrom = row['Chromosome']
        start = row['Start'] - 1  # Convert to 0-based index for pysam
        end = row['End']
        
        # Fetch the sequence
        sequence = fasta_file.fetch(chrom, start, end)
        
        # Prepare a FASTA header for the output
        fasta_header = f">L1HS_element_{index+1} | location={chrom}:{start+1}-{end}"
        
        print("\n" + fasta_header)
        # Print sequence in lines of 60 characters for readability
        for i in range(0, len(sequence), 60):
            print(sequence[i:i+60])

    # Clean up
    fasta_file.close()

if __name__ == '__main__':
    extract_l1_sequences()
```

### Step 3: Run the Script and Interpret the Output

Execute the script from your terminal:
```bash
python extract_l1_sequences.py
```

The script will produce output in FASTA format, ready to be saved to a file or piped into other bioinformatics tools (like BLAST, MEME for motif discovery, etc.).

**Example Output:**

```
Found 5 elements to extract. Retrieving sequences...

>L1HS_element_1 | location=chrX:18568102-18574120
GGAGTTCCGCGTCCTCAGCCGGGAGTTCACCGGTCGCTGGAGTTCGAGGACAGCCTGGGC
AACGTGGTGAAACCCCGTCTCTACTAAAAATACAAAAAATTAGCCGGGTGTGGTGGCGGG
...

>L1HS_element_2 | location=chrX:22497880-22503901
CCTGGGTGACAGAGCGAGACCCTGTCTCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
GCTGGAGTGCGGTGGCGCGATCTCGGCTCACTGCAACCTCCGCCTCCTGGGTTCAAGCGA
...

(Output will continue for all 5 elements)
```

This example clearly demonstrates how the coordinate information in the L1Farm database can be programmatically used to perform powerful, sequence-level analyses.

## Associated Software

The L1Farm datasets were generated using our custom bioinformatics pipeline, **`L1Screening`**. The software is being prepared for a separate publication and will be available at:

[**github.com/ferrasa/l1screening**](https://github.com/ferrasa/l1screening)

---

## Citation

If you use the L1Farm database in your research, please cite our paper:

> In preparation.

---

## License

This data is distributed under the MIT License. See the `LICENSE.md` file for more details.
