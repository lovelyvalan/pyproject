import csv

filename = input("Enter filename: ")
header = input("Enter header row (comma separated): ").split(",")

with open(filename, 'w', newline='') as file:

    writer = csv.writer(file)
    writer.writerow(header)
    while True:
        row = input("Enter row (comma separated) or type 'stop' to exit: ")
        if row.lower() == 'stop':
            break
        writer.writerow(row.split(","))

print("CSV file created successfully!")


f = open('loops.py','r')
print('name of the file: ',f.name)
print('mode of the file: ',f.mode)
print('file is closed or not : ',f.closed)
f.close()
print('file is closed or not : ',f.closed)

"""
python attributes
1.name
2.mode
3.closed
4.softspace
"""



f1 = open('newcsv','w',newline='')
