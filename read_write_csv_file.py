import csv
with open(r'C:\temp\test.csv') as f:
    readfile = csv.DictReader(f)
    for line in readfile:
        with open(r'C:\temp\test1.csv','w') as f1:

            writefile = csv.DictWriter(f)
            writefile.writerow(line['ï»¿Company Name'])