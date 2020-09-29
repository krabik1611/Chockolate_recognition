import pandas as pd
import os
import torch
import torch.nn as nn
import csv


csv_folder = "../chockolate_scrapping_script/csv/"
files = os.listdir(csv_folder)

for file in files:
    filename = csv_folder+ file
    with open(filename,"r") as f:
        # print(f.readlines()[7:-3])
        with open("csv/{}".format(file),"w") as w:
            w.writelines(f.readlines()[7:-3])
    if files.index(file) == 0:
        df = pd.read_csv("csv/{}".format(file),sep=",")

        Total = df.drop(['Catalog Codes',"WeightUnit","Print run","Variant","Score","Accuracy"],axis="columns")
        # Total = Total.rename()

    else:
        try:
            df = pd.read_csv("csv/{}".format(file),sep=",")
            df = df.drop(['Catalog Codes',"WeightUnit","Print run","Variant","Score","Accuracy"],axis="columns")
            Total = Total.append(df)
        except :
            print("error")
    os.remove("csv/{}".format(file))
Total = Total.reset_index(drop=True)
Total.to_csv("data.csv",index=True,sep=',',encoding="utf-8")
