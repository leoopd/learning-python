# Challenge #1
# Using the CSV module write each element of the list (which is another list) into a CSV file called people1.csv
# After writing to the file, read and print out the file contents.

import csv
people = [['Dan', 34, 'Bucharest'],['Andrei',21, 'London'],['Maria', 45, 'Paris']]
with open('python/challenges/files/people1.txt', 'w') as f:
    writer = csv.writer(f, lineterminator='\n')
    for row in people:
        writer.writerow(row)

with open('python/challenges/files/people1.txt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Challenge #2
# Change the solution from the previous challenge and use : (colon) as the delimiter.

import csv
people = [['Dan', 34, 'Bucharest'],['Andrei',21, 'London'],['Maria', 45, 'Paris']]
with open('python/challenges/files/people2.txt', 'w') as f:
    writer = csv.writer(f, lineterminator='\n', delimiter=':')
    for row in people:
        writer.writerow(row)

with open('python/challenges/files/people2.txt') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
