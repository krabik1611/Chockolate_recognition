import os
import csv


new_folder = "data_image"
count = 1
with open("data.csv","r") as f:
    reader = csv.reader(f)
    with open("new_data.csv","w") as f1:
        writer = csv.writer(f1)
        for row in reader:
            filename = row[0]
            new_file = "{}/{}.jpg".format(new_folder,count)
            description = row[1]
            command = "cp {} {}".format(filename,new_file)
            count +=1
            new_row = [new_file,description]
            writer.writerow(new_row)
            os.system(command)
