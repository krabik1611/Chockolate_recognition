import imagesAPI as api
import matplotlib.pyplot as plt
import os
import csv
import numpy.linalg as lin


def getState():
    global count
    global allCount
    proc = (count/allCount)*100
    stat = '[%s%s]' %("##"*(int(proc)//10),'--'*(10-(int(proc)//10)))
    string = 'Complete %22s %i%% %i/%i' %(stat,proc,count,allCount)
    print(string)

if __name__ == '__main__':
    data_dir = "Data/data_image/"
    action = api.MainActive()
    count = 1
    list_files = os.listdir(data_dir)
    allCount = len(list_files)
    # with open("data.csv", "w") as f:
    #     writer = csv.writer(f)
    #     for file in list_files:
    #         filename = data_dir + file
    #         img = action.getImage(filename)
    #         out = action.runNet(img)
    #         id = file[:file.find(".")]
    #         data_list = [id, filename, out]
    #         writer.writerow(data_list)
    #         getState()
    #         count += 1
    for file in list_files:

        if 1:
            filename = data_dir + file
            img = action.getImage(filename)
            out = action.runNet(img)
            # dict_data = {
            #             "id":file[:file.find('.')],
            #             "filename":filename,
            #             "data":out
            # }
            # action.writeDB(dict_data)
            # print(out.mean())
            # print(out)
            plt.plot(out)
            count +=1
        else:
            break
    plt.show()
        # getState()
        # count += 1
