#!/usr/bin/env python3.8
# Combine line counts, nucleotide counts, and GC content into a CSV
import os
import csv

split_dir = "split_files"
output_file = "combined_results.csv"

results = []
for file in sorted(os.listdir(split_dir)):
    if file.endswith(".fasta"):
        path = os.path.join(split_dir, file)
        # Count lines
        with open(path, 'r') as f:
            lines = len(f.readlines())
        # Count nucleotides
        counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        with open(path, 'r') as f:
            for line in f.readlines()[1:]:  # Skip header
                for char in line.upper():
                    if char in counts:
                        counts[char] += 1
        total = sum(counts.values())
        gc_content = (counts['C'] + counts['G']) / total * 100 if total > 0 else 0
        results.append({
            'File Name': file,
            'Line Count': lines,
            'Total Nucleotides': total,
            'A': counts['A'],
            'T': counts['T'],
            'C': counts['C'],
            'G': counts['G'],
            'GC Content (%)': gc_content
        })

# Write to CSV
with open(output_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['File Name', 'Line Count', 'Total Nucleotides', 'A', 'T', 'C', 'G', 'GC Content (%)'])
    writer.writeheader()
    writer.writerows(results)

print(f"Combined results saved to {output_file}")
