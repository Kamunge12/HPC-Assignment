#!/bin/bash
# Count lines in each split file and display in a table

echo "File Name        | Line Count"
echo "-----------------|-----------"
for file in split_files/split_*.fasta; do
    lines=$(wc -l < "$file")
    printf "%-16s | %d\n" "$(basename "$file")" "$lines"
done
