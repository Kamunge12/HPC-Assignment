#!/usr/bin/env python3.8
# Count nucleotides (A, T, C, G) in each split file
import os

output_file = "nucleotide_counts_summary.txt"
split_dir = "split_files"

with open(output_file, 'w') as out:
    out.write("File Name\tA\tT\tC\tG\n")
    for file in sorted(os.listdir(split_dir)):
        if file.endswith(".fasta"):
            path = os.path.join(split_dir, file)
            counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
            with open(path, 'r') as f:
                lines = f.readlines()
                for line in lines[1:]:  # Skip header
                    for char in line.upper():
                        if char in counts:
                            counts[char] += 1
            out.write(f"{file}\t{counts['A']}\t{counts['T']}\t{counts['C']}\t{counts['G']}\n")

print(f"Nucleotide counts saved to {output_file}")
