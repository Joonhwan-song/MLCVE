import sys
import os
import subprocess
import docker
import shutil
import countconvert

datasetpath = "./dataset"
saveFilePath = "/cve/saveresult"
saveHostPath = "./result"

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
        Copy_Dataset_algo(name)
        Machine_Learn(name,list_dataset)
        list_algo=List_Algo()
        list_algo,select_algo=Select_Algo(list_algo,list_dataset)

    return list_algo,select_algo

def Select_Dataset(list_algo,list_dataset,datasetpath):
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
        Copy_Dataset_data(name,list_algo)
        list_dataset=List_Dataset(datasetpath)
        list_dataset,select_dataset=Select_Dataset(list_algo,list_dataset,datasetpath)
    return list_dataset,select_dataset

#1 - make algo -> all dataset to one container
#Copy Host dataset to new_container
def Copy_Dataset_algo(container_name):
    argument = 'docker cp ./dataset ' + container_name+ ':/cve/dataset/'    
    print(argument)
    subprocess.call(argument,shell=True)

#2 - make dataset -> one dataset to all container
def Copy_Dataset_data(dataset_name,list_algo):
    print("INSERT COPY_DATASET_DATA")
    print(list_algo)
    for algo in list_algo:
        argument = 'docker cp ./dataset/' + dataset_name + ' ' + algo + ':/cve/dataset/'+dataset_name
        print(argument)
        subprocess.call(argument,shell=True)

#Learn new algorithm with all dataset
def Machine_Learn(name,list_dataset):
    #exec selected algorithm in container (need to fix run.py)
    for dataset in list_dataset:
        #Run Macine learning
        argument = 'docker exec ' + name + ' python3 save.py ' + dataset
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

#select binaryfile to explore and transform like dataset
def Select_File(list_algo,list_dataset,select_algo,select_dataset):
    source_path = input('Insert File Path To Explore Vulnerabilities : ')
    save_path = './cnt'

    if not os.path.isdir(save_path):
        os.makedirs(save_path)
    
    outputfilename = save_path+'/New_Binary'

    os.system('rm ' + outputfilename)
    os.system('rm ' + outputfilename + '.txt')
    os.system('flawfinder --dataonly --quiet '+ source_path +" >>" + outputfilename+".txt")
    os.system('grep -c "78" '+ outputfilename+ ".txt >>"+ outputfilename)
    os.system('grep -c "120" '+ outputfilename+".txt >>"+ outputfilename)
    os.system('grep -c "126" '+ outputfilename+".txt >>"+ outputfilename)
    os.system('grep -c "134" '+ outputfilename+".txt >>"+ outputfilename)
    os.system('grep -c "190" '+ outputfilename+".txt >>"+ outputfilename)
    os.system('grep -c "327" '+ outputfilename+".txt >>"+ outputfilename)
    os.system('grep -c "377" '+ outputfilename+".txt >>"+ outputfilename)
    os.system('grep -c "676" '+ outputfilename+".txt >>"+ outputfilename)
    os.system('grep -c "785" '+ outputfilename+".txt >>"+ outputfilename)
   
    matrix=countconvert.getarray(outputfilename)
    countconvert.createImage(matrix,outputfilename)
   
    print("Copy NEWBINARY to select algorithm")
    for algo in select_algo:
        argument = 'docker cp ' + outputfilename + ' ' + list_algo[int(algo)-1] + ':/cve/newbinary/'
        subprocess.call(argument,shell=True)        
        argument = 'docker cp ' + outputfilename + '.png ' + list_algo[int(algo)-1] + ':/cve/newbinary/'
        subprocess.call(argument,shell=True)        
    
def Make_Result(list_algo,list_dataset,select_algo,select_dataset):
    for algo in select_algo:
        for data in select_dataset:
            argument = 'docket exec ' +list_algo[int(algo)-1] + ' python3 load.py ' + list_dataset[int(data)-1] 
            print(argument)
            #subprocess.call(argument,shell=True)        

def main():
    #Select Path
    #saveFilePath = "/cve/saveResult"
    #saveHostPath = "./result"
    #datasetPath

    list_algo=List_Algo()
    list_dataset=List_Dataset(datasetpath)

    list_algo,select_algo=Select_Algo(list_algo,list_dataset)
    list_dataset,select_dataset=Select_Dataset(list_algo,list_dataset,datasetpath)

    print("#select_Algo=",select_algo,"Dataset=",select_dataset)
    
    Select_File(list_algo,list_dataset,select_algo,select_dataset)
    
    Make_Result(list_algo,list_dataset,select_algo,select_dataset)    
    Copy_Result(list_algo,list_dataset,select_algo,select_dataset,saveFilePath,saveHostPath)
    Print_Result(saveHostPath)

if __name__ == '__main__':
    main()

            
