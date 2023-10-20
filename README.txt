This archive contains data on PC memberships at several TCS conferences (at the time of writing, SODA, STOC, and FOCS from 2017 through STOC 2024). 

Filenames include a two-digit year and a one-letter conference code (soDa, Stoc, Focs). 

The raw text files contain text copied from calls for papers. 

The processed text files contain one name per line with affiliations removed and spelling standardized according to the lists in the file equivalences.txt (each line in that file contains a group of equivalent names, with the first name in the list being the standard version). 

Currently, you have the ensure *manually* that the names in the processed files are standardized; otherwise, the spreadsheet may have more than one row per person. 

Running the command 
' python3 merge_and_sort.py processed_files/*.txt ' 
will generate a file called merged_and_sorted.txt with exactly one copy of each name, in sorted order (by first name). These names are taken from the processed files. 

Running the command
' python3 make-pc-members-csv.py processed_files/*.txt > output.csv '
will generate a file called output.csv with a spreadsheet, one row per name, which indicates which conference the person has been on the PC for. The process assumes that the input file names end in XYZ.txt where XYZ identifies the conference.

Notes: 

* equivalences.txt is just a list of corrections that were made manually. It could be used to help automate future duplicate removals.

* strip-parens.py is little script to remove affiliations in parentheses from a copied-and-pasted PC list. It currently assumes only one pair of parentheses per line of the input file. 


Adam Smith (building on work by Anupam Gupta)
October 2023




