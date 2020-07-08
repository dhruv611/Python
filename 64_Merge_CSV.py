import csv

def mergeCSV(csv_list, output_path):
    fieldnames = list()
    for file in csv_list:
        with open(file,'r') as input_csv:
            fn = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(x for x in fn if x not in fieldnames)

    with open(output_path,'w',newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames = fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file,'r') as input_csv:
                reader = csv.DictReader(input_csv)
                for roe in reader:
                    writer.writerow(row)

def main():
    csv_list = ['file1.csv','file2.csv']
    output_path = 'output.csv'
    mergeCSV(csv_list,output_path)

if __name__ == "__main__": main()
