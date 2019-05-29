import sys
import os
import subprocess
import docker
import shutil

def Select_Algo(list_algo,list_dataset):
    #Select Algorithm
    print("#Select Machinelearning Algorithms(Select 0 if you want to add an algorithm)")
    print("0 : Add Algorithm")
   
    for index,value in enumerate(list_algo,start=1):
        print(index,":",value)
    select_algo=input('Select Numbers:').split(',')

    if select_algo[0] =='0':
        print("#ADD NEW ALGORITHM")
        name = input('#Name:')
        image = input('#Image(ex.ubuntu, tensorflow/tensorflow):')
        argument = 'docker run -i -t -d --name ' + name + ' ' + image + ' /bin/bash'
        subprocess.call(argument,shell=True)
        argument = 'docker ps'
        subprocess.call(argument,shell=True)
        Machine_Learn(name,list_dataset)
        list_algo=List_Algo()
        select_algo=Select_Algo(list_algo,list_dataset)
    
    return select_algo

def Select_Dataset(list_dataset,datasetpath):
    #Select Dataset
    print("#Select Datasets(Select 0 if you want to add an dataset)")
    print("0 : Add dataset")
 
    for index,value in enumerate(list_dataset,start=1):
        print(index,":",value)
    select_dataset=input('Select Numbers:').split(',')
   
    if select_dataset[0] == '0':
        print("#ADD NEW DATASET")
        name = input('#Name:')
        path = input('#Path:')
        destination = datasetpath + '/' + name 
        shutil.copytree(path,destination)
        list_dataset=List_Dataset(datasetpath)
        list_dataset,select_dataset=Select_Dataset(list_dataset,datasetpath)
    return list_dataset, select_dataset

#Learn new algorithm with all dataset
def Machine_Learn(name,list_dataset):
    #exec selected algorithm in container (need to fix run.py)
    for dataset in list_dataset:
        argument = 'docker exec ' + name + ' python3 run.py' + ' ' + dataset
        print(argument)
        #subprocess.call(argument,shell=True)


#Save each container name to list_algo[]
def List_Algo():
    list_algo=[]
    client = docker.from_env()
    for container in client.containers.list():
            list_algo.append(container.name)
    return list_algo

def List_Dataset(datasetpath):
    list_dataset = os.listdir(datasetpath)
    print("DATASET LIST =",list_dataset)
    return list_dataset

#Copy Result value container to host
def Copy_Result(list_algo,list_dataset,select_algo,select_dataset,saveFilePath,saveHostPath):
    for algo in select_algo:
            for data in select_dataset:
                    argument = 'docker cp ' + list_algo[int(algo) -1] + ':' + saveFilePath + '/' +list_algo[int(algo)-1] + '_' + list_dataset[int(data)-1]  + ' ' + saveHostPath
                    subprocess.call(argument,shell=True)

#Print result in host directory
def Print_Result(saveHostPath):
    path_dir = saveHostPath
    file_lists = os.listdir(path_dir)
    print("RESULT")
    for file in file_lists:
            f = open(saveHostPath + '/' + file, "r")
            line = f.readline()
            print(line)
            os.remove(saveHostPath + '/' + file)
            f.close()

def main():
    #Select Path
    saveFilePath = "/saveResult"
    saveHostPath = "./result"
    datasetpath = "./dataset"

    list_algo=List_Algo()
    list_dataset=List_Dataset(datasetpath)

    select_algo=Select_Algo(list_algo,list_dataset)
    list_dataset,select_dataset=Select_Dataset(list_dataset,datasetpath)

    print("#Algo=",select_algo,"Dataset=",select_dataset)

    Copy_Result(list_algo,list_dataset,select_algo,select_dataset,saveFilePath,saveHostPath)
    Print_Result(saveHostPath)

if __name__ == '__main__':
    main()

