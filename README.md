# HPC-Assignment
Solutions to this exercise-HPC

HPC-ASSIGNMENT
            |
            |---QUESTION_1 
            |        |
            |        |---bash_script.sh
            |        |---python_script.py
            |
            |       
            |---QUESTION_2
                     |
                     |---split.py 
                     |---split_files
                     |---count_line.sh
                     |---count_nucleotide.py
                     |---nucleotides_count_summary.txt
                     |---HighestGC_content.py
                     |---combine_results.py
                     |---combined_result.csv



Question 1: Sum of First 10 Million Integers
1. A Bash script to calculate the sum of the first 10 million integers.
    - This script is found at the directory named QUESTION-1, the name of the script is bash_script.sh
    - The code in this script has:
        - #!/bin/bash  - A shebang. It specifies that the script should be executed using the Bash shell.
        - sum=0   - This initializes a variable named sum to 0.
        - for ((i=1; i<=10000000; i++)); do - The loop iterates over integers from 1 to 10,000,000.
        - sum=$((sum + i))  - this line updates the sum variable by adding the current value of i to it.
        - echo "Sum of first 10 million integers: $sum"  - This prints the result to the terminal.
              C:\Users\fmariita\Desktop\HPC_SCREENSHOT\bash_script.png

2. A Python script to calculate the sum of the first 10 million integers.
   - This script is at directory QUESTION-1,the script is named python_script.py.
   - The code in this script has:
       - #!/usr/bin/env python3.8 - A shebang,system to execute the script using the python3.8
       - import time - Imports the time module, which provides functions for working with time.
       - The time.time() function will be used to measure the execution time of the calculation.
       - start_time = time.time() - Records the time just before the calculation begins.
       - n = 10000000 - Sets the value of which represents the number of integers to sum (from 1 to 10,000,000).
       - sum_integers = n * (n + 1) // 2 - Computes the sum of integers from 1 to n to avoid float.The sum is stored in the sum_integers variable.
       - end_time = time.time() - Records the time immediately after the calculation.
       - print(f"Sum of first 10 million integers: {sum_integers}") - Outputs the computed sum.
              C:\Users\fmariita\Desktop\HPC_SCREENSHOT\python_script.png      

3. Comparing the execution time of both scripts and note the results.
      - This is the screenshot that compares the diffrence of execution time of both script:
              C:\Users\fmariita\Desktop\HPC_SCREENSHOT\Execution_time.png

Question 2: File Operations with HIV Reference Genome:
1. Split the File into 50 Random Parts:
   - This python script is called split.py and its fpuns in the QUESTION-2 directory.
   - The script contains code that has:
       - #!/usr/bin/env python3.8 - A shebang,Specifies that the script should be executed using Python3.8.
       - import random - Provides functions for generating random numbers and shuffling lists.
       - import os - Provides functions for interacting with the operating system,example creating directories.
       - input_file = "HIV_ref_genome.fasta" - Defines the name of the input file.
       - with open(input_file, 'r') as f: - Opens the file in read mode ('r'),(with) ensures file is properly closed after reading.
       - lines = f.readlines() - Reads all lines of the file into a list called lines.
       - if lines and lines[0].startswith('>'): - Identifies if the FASTA header line.
       - header = lines.pop(0) - If a header is found, it’s removed from lines.
       - else: header = None: - If no header is found, header is set to None.
       - total_lines = len(lines): - Counts the number of lines in the lines list.
       - num_files = 50: - Specifies that the lines will be split into 50 separate files.
       - line_counts = []: - Initializes an empty list to store the number of lines for each file.
       - remaining_lines = total_lines: - Tracks the number of lines still available to distribute.
       - for i in range(num_files - 1) - iterates 49 times (for files 1 to 49).
       - max_lines = remaining_lines - (num_files - i - 1): - Calculates the maximum number of lines the current file can take.
       - count = random.randint(1, max_lines): - Generates a random number of lines (between 1 and max_lines) for the current file.
       - line_counts.append(count): - Adds the random count to line_counts.
       - remaining_lines -= count: - Subtracts the assigned lines from remaining_lines.
       - line_counts.append(remaining_lines): - Assigns all remaining lines to the 50th file, ensuring all lines are used.
       - random.shuffle(lines): - Shuffles the list in place, ensuring that the sequence data is distributed randomly across the output files.
       - output_dir = "split_files": - Specifies the name of the output directory.
       - os.makedirs(output_dir, exist_ok=True): - Creates the directory split_files if it doesn’t exist.
       - start = 0: - Initializes a variable to track the starting index in the lines list.
       - for i, count in enumerate(line_counts): - Iterates over line_counts, where i is the index (0 to 49).
       - output_file = os.path.join(output_dir, f"split_{i+1}.fasta"): - Constructs the path for the output file
       - os.path.join - ensures the path is correctly formatted for the operating system.
       - with open(output_file, 'w') as f: - Opens the output file in write mode ('w').
       - if header: f.write(header): - If a header was found, writes it to the output file.
       - f.writelines(lines[start:start + count]): - Writes a slice of the lines list (from index start to start + count) to the file.
       - start += count: - Updates the start index to the next position in lines for the next file.
       - print(f"Split {total_lines} lines into 50 files in {output_dir}") - Informs the user that the script has completed successfully.
              C:\Users\fmariita\Desktop\HPC_SCREENSHOT\split.py.png

 2. Count the Number of Lines in Each Split File
       - This script bash script is called count_line.sh and is found at the QUESTION_2 directory.
       - The code in this script include:
          - #!/bin/bash - specifies that the script should be executed using the Bash shell.
          - echo "File Name        | Line Count" - his serves as the header row of the table, labeling two columns.
          - echo "-----------------|-----------" - distinguish the header from the data rows.
          - for file in split_files/split_*.fasta; do - This initiates a for loop that iterates over files matching the pattern split_files/split_*.fasta.
          - lines=$(wc -l < "$file") - reads the file, counts the number of lines,then stores the output.
          - printf "%-16s | %d\n" "$(basename "$file")" "$lines" - this formats and prints a row in the table for the current file.
              C:\Users\fmariita\Desktop\HPC_SCREENSHOT\countline.sh.png                   
              C:\Users\fmariita\Desktop\HPC_SCREENSHOT\countline2.sh.png

 3. Count Nucleotides in Each File
       - The python script for this is called count_nucleotide.py and is found in the 	QUESTION_2 directory.
       - The code for this script icludes:
           - #!/usr/bin/env python3.8 - specifies that the script should be executed using Python 3.8.
           - import os - specifically list files in a directory and construct file paths.
           - output_file = "nucleotide_counts_summary.txt" - The name of the output file where the nucleotide counts will be saved.
           - split_dir = "split_files" - The directory (split_files) containing the input FASTA files to be processed.
           - with open(output_file, 'w') as out - A file named nucleotide_counts_summary.txt is opened in write mode ('w').
           - out.write("File Name\tA\tT\tC\tG\n") - A header line is written to the output file with column names.
           - r file in sorted(os.listdir(split_dir)) - lists all files in the split_files directory,ensures the files are processed in alphabetical order,Each file name is assigned to the variable file in the loop
           - if file.endswith(".fasta") - The script only processes files with the .fasta extension, ignoring other file types in the directory.
           - path = os.path.join(split_dir, file) - os.path.join combines the directory name (split_files) and the file name to create the full file path.
           - counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0} - dictionary counts is created to store the count of each nucleotide (A, T, C, G), initialized to 0.
           - with open(path, 'r') as f: - The FASTA file is opened in read mode ('r') using a with statement.
           - lines = f.readlines() - readlines() reads all lines of the file into a list called lines.
           - for line in lines[1:]: - Skip header of the FASTA file.
           - for char in line.upper(): - converts the line to uppercase to ensure consistent counting.
           - if char in counts:counts[char] += 1 - If the character is one of the nucleotides,its corresponding count in the counts dictionary is incremented.
           - out.write(f"{file}\t{counts['A']}\t{counts['T']}\t{counts['C']}\t{counts['G']}\n") - writes a line to the output file,line includes the file name and the counts for A, T, C, and G, separated by tabs.
           - print(f"Nucleotide counts saved to {output_file}") - a message is printed confirming that the results have been saved to nucleotide_counts_summary.txt.
                 C:\Users\fmariita\Desktop\HPC_SCREENSHOT\count_nucleotide.png

 4. Identify the File with the Highest GC Content
       - This python script is calles HighestGC_content.py and is found on the QUESTION_2 directory.
       - The code in this script includes;
           - #!/usr/bin/env python3.8 - specifies that the script should be executed using Python3.8.
           - import os - to list files in a directory and construct file paths.
           - split_dir = "split_files" - Specifies the directory (split_files) containing the FASTA files to be analyzed.
           - max_gc = 0 - Tracks the highest GC content found, initialized to 0.
           - max_file = "" - : Stores the name of the file with the highest GC content, initialized as an empty string.  
           - for file in sorted(os.listdir(split_dir)): - The loop iterates over each file in the directory.
           - if file.endswith(".fasta"): - Checks if the file has a .fasta extension to process only FASTA files, ignoring other file types.
           - path = os.path.join(split_dir, file) - Combines the directory name (split_files) and the file name to create the full file path.
           - counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0} - Creates a dictionary to count occurrences of each nucleotide ('A', 'T', 'C', 'G'), initialized to 0.
           - with open(path, 'r') as f: - Opens the FASTA file in read mode ('r') and reads all lines into the lines list.
           - lines = f.readlines() - FASTA files typically have a header line (starting with '>') followed by sequence lines.
           - for line in lines[1:] - skips the header line if any.
           - for char in line.upper() - Converts the line to uppercase to handle any lowercase nucleotides.
           - if char in counts - Checks if the character is one of 'A', 'T', 'C', or 'G
           - counts[char] += 1 - If so, increments its count in the counts dictionary.
           - total = sum(counts.values()) - Sums the counts of all nucleotides ('A', 'T', 'C', 'G') to get the total number of valid bases.
           - if total > 0: - Ensures division by zero is avoided if the file has no valid nucleotides.
           - gc_content = (counts['C'] + counts['G']) / total * 100 - Calculates the GC content as a percentage.
           - if gc_content > max_gc:,max_gc = gc_content,max_file = file - If the current file’s gc_content is higher than max_gc, updates max_gc with the new value and max_file with the current file’s name.
           - print(f"File with highest GC content: {max_file} ({max_gc:.2f}%)") - prints the name of the file with the highest GC content and its GC percentage, formatted to two decimal places.
                  C:\Users\fmariita\Desktop\HPC_SCREENSHOT\HighestGC-content.png

 5. Combine Results
      - This script is named combine_result.py and is at the QUESTION_2 directory.
      - The code for this script icludes;
          - #!/usr/bin/env python3.8 - ensures the script runs with Python3.8.
          - import os - listing files in a directory.
          - import csv - For writing the results to a CSV file.
          - split_dir = "split_files" - Specifies the directory (split_files) containing the FASTA files to process.
          - output_file = "combined_results.csv" - Specifies the name of the output CSV file (combined_results.csv) where results will be saved.
          - results = [] - An empty list to store the analysis results for each FASTA file.
          - for file in sorted(os.listdir(split_dir)) - Lists all files in the split_files directory,Ensuring files are processed in alphabetical order.
          - if file.endswith(".fasta"): - Filters for files with the .fasta extension.
          - path = os.path.join(split_dir, file) - Constructs the full file path for each FASTA file.
          - with open(path, 'r') as f - Opens each FASTA file in read mode ('r').
          - lines = len(f.readlines()) - Reads all lines into a list,Counts the total number of lines in the file,This count is stored.
          - counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
              with open(path, 'r') as f:
                  for line in f.readlines()[1:]:  # Skip header
                     for char in line.upper():
                          if char in counts:
                              counts[char] += 1 ( this code  reads a file (skipping the first line), iterates through each character in the remaining lines (converting them to uppercase), and counts the occurrences of 'A', 'T', 'C', and 'G', storing these counts in the counts dictionary.
          - total = sum(counts.values()) - Calculates the total number of nucleotides by summing the counts of A, T, C, and G.
          - gc_content = (counts['C'] + counts['G']) / total * 100 if total > 0 else 0 - Calculates the GC content as a percentage.
          - results.append({
              'File Name': file,
              'Line Count': lines,
              'Total Nucleotides': total,
              'A': counts['A'],
              'T': counts['T'],
              'C': counts['C'],
              'G': counts['G'],
              'GC Content (%)': gc_content
            })  - takes calculated data (filename, line count, nucleotide counts, GC content) and organizes it into a dictionary, then adds this dictionary as a new entry to the results list.
           - with open(output_file, 'w', newline='') as f: - Opens the output CSV file (combined_results.csv) in write mode ('w').
           - writer = csv.DictWriter(f, fieldnames=['File Name', 'Line Count', 'Total Nucleotides', 'A', 'T', 'C', 'G', 'GC Content (%)']) - Creates a CSV writer that maps dictionary keys to CSV columns,Specifies the column headers for the CSV.
           - writer.writeheader(): - Writes the column headers to the CSV.
           - writer.writerows(results): - Writes each dictionary in the results list as a row in the CSV.
           - print(f"Combined results saved to {output_file}") - Prints a confirmation message indicating that the results have been saved to combined_results.csv
                      C:\Users\fmariita\Desktop\HPC_SCREENSHOT\combined-results.png
              
                 
- Compressing and zipping.
     - tar -czf HPC-Assignment.tar.gz HPC-Assignment
- File Transfer to my repository
     - scp gkamunge@hpc01.icipe:/home/gkamunge/HPC-Assignment.tar.gz /mnt/c/fmariita/HPC-Assignment
     - scp  -r gkamunge@hpc01.icipe:/home/gkamunge/HPC-Assignment/ /mnt/c/fmariita/HPC-Assignment
         
