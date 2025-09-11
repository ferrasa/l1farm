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
        df = pd.read_csv(L1FARM_FILE, sep='\t', header=None, usecols=[0, 1, 2, 3], names=COLUMN_NAMES, comment='#')
    except FileNotFoundError:
        print(f"Error: L1Farm file not found at '{L1FARM_FILE}'")
        return

    # 2. Filter for the L1 elements of interest
    filtered_df = df[
        (df['Chromosome'] == TARGET_CHROMOSOME) &
        (df['Subfamily'] == TARGET_SUBFAMILY)
    ].head(LIMIT)
    filtered_df = filtered_df.reset_index(drop=True)

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
        fasta_header = f">{row['Subfamily']}_element_{index+1} | location={chrom}:{start+1}-{end}"

        print("\n" + fasta_header)
        # Print sequence in lines of 60 characters for readability
        for i in range(0, len(sequence), 60):
            print(sequence[i:i+60])

    # Clean up
    fasta_file.close()

if __name__ == '__main__':
    extract_l1_sequences()
