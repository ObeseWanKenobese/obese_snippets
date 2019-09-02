# WORK IN PROGRESS
# Having issues with the datetime.strptime line outputting datetime.datetime.... wtf

import csv
import time
from datetime import datetime

path = "C:\Users\Viola\Documents\Python\data\wind_study_cropped.csv"
file = open(path, 'r')
reader = csv.reader(file)

header = next(reader) 

data = []
for row in reader:
    # row = [Time Step, Date_Time, Temperature]
    timeStep = int(row[0])
    date = datetime.strptime(row[1], "%b %d, %Y %H:%M:%S")
    temperature = float(row[2])
    
    data.append([timeStep, date, temperature])

print(data[0])

# write out the delta Temperature

returns_path = "C:\Users\Viola\Documents\Python\data\wind_study_deltaT.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(["Return"])

for i in range(len(data) - 1):
    TempRow = data[i]
    TempInitial = TempRow[0]
    TempRowNext = data[i+1]
    TempNext = TempRowNext[1]
    
    deltaTemp = (TempNext - TempInitial) / TempNext
    write.writerow([deltaTemp])