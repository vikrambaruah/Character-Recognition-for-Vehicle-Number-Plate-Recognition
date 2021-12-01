import csv
fields = ['Registration no.', 'State', 'Time of Entry']
filename = "car_records.csv" 
with open(filename, 'w') as csvfile: 
    csvwriter = csv.writer(csvfile)   
    csvwriter.writerow(fields) 