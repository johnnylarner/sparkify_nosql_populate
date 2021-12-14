import os
import glob
import csv


def get_files():
    """
    Traverses event_data folder and returns file paths as list.
    """
    filepath = os.getcwd() + '/event_data'

    for root, dirs, files in os.walk(filepath):
        file_path_list = glob.glob(os.path.join(root,'*'))

    return file_path_list


def create_event_csv(file_path_list):
    """
    Creates CSV file that compilies all event_data csv files.

    Args:
    -   file_path_list: list generated by the get_files function.
    """
    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = [] 
        
    # for every filepath in the file path list 
    for f in file_path_list:

    # reading csv file 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            next(csvreader)
            
    # extracting each data row one by one and append it        
            for line in csvreader:
                #print(line)
                full_data_rows_list.append(line) 

    # creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into the \
    # Apache Cassandra tables
    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                    'level','location','sessionId','song','userId'])
        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))

    # check the number of rows in your csv file
    with open('event_datafile_new.csv', 'r', encoding = 'utf8') as f:
        print("Number of records in CSV: ", sum(1 for line in f))

if __name__ == "__main__":
    files = get_files()
    create_event_csv(files)