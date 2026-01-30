# L1Farm Database

![License](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Citation](https://img.shields.io/badge/Publication-Human%20Gene-darkgreen)](https://doi.org/10.1016/j.humgen.2026.201529)


**L1Farm** is a comprehensive and complementary database for the annotation of LINE-1 (L1) retrotransposons. It was designed to provide a higher level of detail than standard repeat annotation tools.

### Key Features

*   **Detailed Annotations:** Provides a complete analysis of 18 distinct L1 subfamilies.
*   **Multi-Genome Coverage:** Includes annotations for the human reference genome (GRCh38/hg38) and, uniquely, for two individual diploid genomes (Asian and Caucasian).
*   **High-Resolution Data:** All annotations are provided at both allele-level and nucleotide-level resolution.
*   **Functional Ranking:** L1 elements are annotated with their precise genomic *loci* and ranked by their full-length content and similarity to consensus sequences, helping to identify potentially active elements.

---

## Database Description

The L1Farm database is organized into 12 tab-separated value (`.tsv`) files. The naming convention for each file follows a consistent structure to help you identify its content:

**`L1Farm_[Dataset]_[Cutoff]_[Genome].tsv`**

### File Naming Convention

#### 1. Dataset Type (`[Dataset]`)
This indicates the type of annotation provided in the file:
-   **`RG-L1`**: **R**egions in **G**enome. Annotations of individual L1 regions (5'UTR, ORF1, Spacer, ORF2, 3'UTR) found in the **hg38 reference genome**.
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

## Data Formats and Structure

To ensure maximum compatibility with a wide range of bioinformatics tools and workflows, the L1Farm database is provided in three distinct formats, organized into separate directories within this repository:

### 1. **TSV Format** (`/` directory)

This is the original, full-detail data format. These tab-separated files contain all 12 columns of metadata and are ideal for loading into data analysis environments like R, Python (with pandas), or spreadsheet software.

**Columns (TSV):**

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

### 2. **BED Format** (`/BED` directory)

This format is optimized for high-performance interval-based analysis with gold-standard tools like **`bedtools`** and for visualization in genome browsers (e.g., UCSC Genome Browser, IGV). It contains the core positional information in 6 columns.

**Columns (BED):**
1.  `chrom`: Chromosome
2.  `chromStart`: Start position (0-based)
3.  `chromEnd`: End position
4.  `name`: A composite name (e.g., `L1HS_ORF1`)
5.  `score`: Sequence identity, scaled to 0-1000
6.  `strand`: Strand (+ or -)

### 3. **GFF3 Format** (`/GFF3` directory)

This is a rich, standardized annotation format that preserves all the metadata from the original TSV files in a structured way. It is the most comprehensive format for integration with annotation software and advanced analysis pipelines. All metadata is stored in the 9th column (attributes).

---

## How to Download

You can download the entire database by:
1.  Clicking the green **`Code`** button and selecting **`Download ZIP`**.
2.  Or, if you have Git installed, cloning the repository:
    ```sh
    git clone https://github.com/your-username/l1farm.git
    ```

---

## Usage Example: extracting L1 sequences with a Python script

A common task in genomics is to move from annotation to sequence-level analysis. This example demonstrates how to use the L1Farm database to extract the actual DNA sequences of specific L1 elements from a reference genome FASTA file.

This script will answer the question: **"What are the nucleotide sequences of the first 5 full-length, highly conserved (HC) L1HS elements on the X chromosome?"**

### Prerequisites
-   **Python 3** with the following libraries installed:
    -   `pandas`: For easy data manipulation (`pip install pandas`).
    -   `pysam`: A powerful library for reading genomic data files (`pip install pysam`).
-   A **reference genome file** in FASTA format (e.g., `hg38.fa`).
-   The FASTA file must be **indexed** by `samtools faidx` (`samtools faidx hg38.fa`), which creates a corresponding `.fai` file.

### Step 1: Download the Script and Data

To begin, you need the example script and the L1Farm data files on your local machine.

1.  Click the green **`Code`** button at the top of this page and select **`Download ZIP`**.
2.  Unzip the downloaded file. This will create a folder containing all the L1Farm `.tsv` files and the Python script `extract_l1_sequences.py`.

Alternatively, if you have Git installed, you can clone the repository:
```sh
git clone https://github.com/ferrasa/l1farm.git
```
Navigate into the `l1farm` directory.

### Step 2: Configure the Script

Before running the script, you may need to edit its configuration variables to match your file names and analysis parameters.

Open the `extract_l1_sequences.py` file in a text editor and check the following variables at the top:

```python
# --- Configuration ---
L1FARM_FILE = 'L1Farm_FLL1_HC_HG38.tsv'
GENOME_FASTA = 'hg38.fa'
TARGET_CHROMOSOME = 'chrX'
TARGET_SUBFAMILY = 'L1HS'
LIMIT = 5 
```
-   Ensure `L1FARM_FILE` points to the correct L1Farm dataset you want to analyze.
-   Ensure `GENOME_FASTA` matches the name of your indexed reference genome file.
-   You can change `TARGET_CHROMOSOME`, `TARGET_SUBFAMILY`, and `LIMIT` to customize your analysis.

### Step 3: Run the Script and Interpret the Output

Once the script is configured, execute it from your terminal from within the repository's directory:
```bash
python extract_l1_sequences.py
```
The script will produce output in FASTA format, ready to be saved to a file or piped into other bioinformatics tools (like BLAST, MEME for motif discovery, etc.).

**Example Output:**

```

Found 5 elements to extract. Retrieving sequences...

>L1HS_element_1 | location=chrX:141421229-141427248
attatactctaagttttagggtacatgtgcacattgtgcaggttagttacatatgtatac
atgtgccatgctggtgcgctgcacccactaatgtgtcatctagcattaggtatatctccc
...

>L1HS_element_2 | location=chrX:11707248-11713267
Ggggggaggagccaagatggccgaataggaacagctccggtctacagctcccagcgtgag
cgacgcagaagacggtgatttctgcatttccatctgaggtaccgggttcatctcactagg
...

(Output will continue for all 5 elements)
```

This example clearly demonstrates how the coordinate information in the L1Farm database can be programmatically used to perform powerful, sequence-level analyses.


---

## Associated Software

The L1Farm datasets were generated using our custom bioinformatics pipeline, **`L1Screening`**. The software is being prepared for a separate publication and will be available at:

[**github.com/ferrasa/l1screening**](https://github.com/ferrasa/l1screening)

---

## Citation

If you use the L1Farm database in your research, please cite our paper:

> In preparation.

---

## License

This data is distributed under the permissive MIT License, which allows for free use, modification, and redistribution for both academic and commercial purposes.
