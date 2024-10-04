import csv
try:
    with open(r'C:\temp\test.csv') as f:
        readfile = csv.DictReader(f)
        for line in readfile:
            with open(r'C:\temp\test1.csv','w') as f1:

                writefile = csv.DictWriter(f)
                writefile.writerow(line['ï»¿Company Name'])

except Exception as e:
    print(e)

finally:
    print('Program ended')