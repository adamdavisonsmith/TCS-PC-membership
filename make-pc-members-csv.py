import sys

# takes names from the names.txt file
# and then reads off files given as arguments
# and outputs a csv file 
# each line gives a name and the filenames that contain that name. 
# 
# warning: some names are duplicates.
# also, create name list by something like
# cat *.txt | sort | uniq | sort > new-names.txt
#

Names = {}

file = open("merged_and_sorted.txt", "r")
for line in file:
    sline = line.strip()
    Names[sline] = ""
PCs = dict(Names) # makes a copy of Names

for f in sys.argv[1:]:
    file = open(f, "r")
    conf_acronym = f[-7:-4] 
    for name in PCs:
        PCs[name] = PCs[name] + ","
    for line in file:
        sline = line.strip()
        PCs[sline] = PCs[sline] + conf_acronym

#print Names
for name in PCs:
    print(name + ", " + PCs[name])
