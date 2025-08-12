# L1Farm Database

![License](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Citation](https://img.shields.io/badge/Publication-In%20Preparation-lightgrey)](https://doi.org/YOUR_PAPER_DOI)

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
