#!/usr/bin/env python3.8
# Split HIV_ref_genome.fasta into 50 parts with random line counts
import random
import os

# Read the input file
input_file = "HIV_ref_genome.fasta"
with open(input_file, 'r') as f:
    lines = f.readlines()

# Remove header line if present (starts with '>')
if lines and lines[0].startswith('>'):
    header = lines.pop(0)
else:
    header = None

total_lines = len(lines)
num_files = 50

# Generate random line counts for each file
line_counts = []
remaining_lines = total_lines
for i in range(num_files - 1):
    # Ensure each file gets at least 1 line
    max_lines = remaining_lines - (num_files - i - 1)
    count = random.randint(1, max_lines)
    line_counts.append(count)
    remaining_lines -= count
line_counts.append(remaining_lines)  # Last file gets remaining lines

# Shuffle lines to ensure randomness
random.shuffle(lines)

# Create output directory
output_dir = "split_files"
os.makedirs(output_dir, exist_ok=True)

# Write to 50 files
start = 0
for i, count in enumerate(line_counts):
    output_file = os.path.join(output_dir, f"split_{i+1}.fasta")
    with open(output_file, 'w') as f:
        if header:
            f.write(header)  # Write header to each file
        f.writelines(lines[start:start + count])
    start += count

print(f"Split {total_lines} lines into 50 files in {output_dir}")
