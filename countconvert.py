import sys, os
from PIL import Image
import glob
import numpy as np
import math

def getarray(binaryname):
    file=open(binaryname,"r")
    print(binaryname)
    dataarray= np.zeros((3,3),dtype=np.float16)

    data=file.readline()
    try:
        for i in range(0,3):
            for j in range(0,3):
                dataarray[i][j]=data
                data=file.readline()

    except TypeError:
        pass
    dataarray=dataarray/dataarray.max()
#    dataarray=dataarray.mean(axis=1).reshape(len(dataarray),1)
    dataarray=dataarray*255
    dataarray=dataarray=np.floor(dataarray)
    print(dataarray)
    return dataarray

def createImage(binarydata,outputfilename):
    image = Image.fromarray(binarydata,'P')
    image = image.resize((256,256))
    imagename = outputfilename+".png"
    image.save(imagename)
    print (imagename + " image created")


if __name__ == "__main__":
    dir_full_path=sys.argv[1]
    path= os.path.dirname(dir_full_path)
    dir_list= os.listdir(path)
    for i in range(len(dir_list)):
        cnt_path=os.path.join(path+"/"+dir_list[i]+"/")
        os.system('rm ' +cnt_path+ '*.txt')
        image_path=os.path.join(path+"/png/"+dir_list[i]+"/")
        if not os.path.isdir(image_path):
            os.makedirs(image_path)
        file_list= os.listdir(cnt_path)
        for j in range(len(file_list)):
            base_name=os.path.splitext(os.path.basename(file_list[j]))[0]

            outputfilename= os.path.join(image_path,base_name)
            matrix = getarray(os.path.join(cnt_path,file_list[j]))
            createImage(matrix,outputfilename)
