import csv 

csv_file = 'masterclass/read_csv/file.csv'
sql_file = 'masterclass/read_csv/sql_file.txt'

with open (csv_file) as rf:
    csvRead = csv.reader(rf, delimiter=',')
    line_count = 0
    with open(sql_file, 'a') as wf:
        for row in csvRead:
            print(row)
            if line_count == 0:
                wf.write(f"INSERT INTO myTable({','.join(row)}) VALUES \n")
            else:
                wf.write(f"('{row[0]}','{row[1]}','{row[2]}','{row[3]}'),\n")
            line_count += 1

    print(f'Processed lines: {line_count}')