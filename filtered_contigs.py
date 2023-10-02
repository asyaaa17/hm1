def filter_by_length(input_fasta, output_fasta, min_length):
    with open(input_fasta, 'r') as input_file, open(output_fasta, 'w') as output_file:
        record = ""
        for line in input_file:
            if line.startswith('>'):
                if len(record) >= min_length:
                    output_file.write(record)
                record = line
            else:
                record += line
        if len(record) >= min_length:
            output_file.write(record)

def main():
    input_fasta = "spades_scaffolds.fasta"
    output_fasta = "filtered_contigs.fa"
    min_length = 3000

    filter_by_length(input_fasta, output_fasta, min_length)

if __name__ == "__main__":
    main()
