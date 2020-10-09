import pandas as pd
import os


image_folder = "../Data/image/"
files = os.listdir(image_folder)
df = pd.read_csv("data.csv")
for file in files:
    filename = image_folder+file
    id = int(file[:-4])

    if df[df["id"]==id]["Orientation"].tolist()[0] == "Vertical":
        os.system("cp {} {}".format(filename,"Image/Vertical"))
    elif df[df["id"]==id]["Orientation"].tolist()[0] == "Horizontal":
        os.system("cp {} {}".format(filename,"Image/Horizontal"))
    # print(df[df["id"]==id]["Orientation"].tolist()[0])
    
