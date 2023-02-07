import os
import csv

voting_data = os.path.join("Resources", "election_data.csv")
Voting_Report = os.path.join("Analysis", "Voting_Report.txt")

voters = 1
charles = 1
diana = 0
raymon = 0
winner = ()

with open(voting_data) as votes:
    reader = csv.reader(votes, delimiter=',')
    titles = next(reader)
    numbers = next(reader)
    for row in reader:
        voters += 1
        if str(row[2]) == 'Charles Casper Stockham':
            charles += 1
        if str(row[2]) == 'Diana DeGette':
            diana += 1
        if str(row[2]) == 'Raymon Anthony Doane':
            raymon += 1

pcharles = (charles/voters)*100
pdiana = (diana/voters)*100
praymon = (raymon/voters)*100

if diana > charles and raymon:
    winner = 'Diana DeGette'
if charles > diana and raymon:
    winner = 'Charles Casper Stockham'
if raymon > charles and diana:   
    winner = 'Raymon Anthony Doane'

report = (
f"Election Results\n"
f"---------------------------\n"
f"Total Voters: {voters}\n"
f"---------------------------\n"
f'Charles Casper Stockham: % {pcharles:.3f} ({charles})\n'
f"Diana DeGette: % {pdiana:.3f} ({diana})\n"
f'Raymon Anthony Doane: % {praymon:.3f} ({raymon})\n'
f"---------------------------\n"
f'Winner: {winner}\n'
f"---------------------------\n"
)

print(report)

with open(Voting_Report, 'w') as txt_file:
    txt_file.write(report)