#!/usr/bin/env python3.8
# Calculate GC content for each split file and find the highest
import os

split_dir = "split_files"
max_gc = 0
max_file = ""

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
        total = sum(counts.values())
        if total > 0:
            gc_content = (counts['C'] + counts['G']) / total * 100
            if gc_content > max_gc:
                max_gc = gc_content
                max_file = file

print(f"File with highest GC content: {max_file} ({max_gc:.2f}%)")
