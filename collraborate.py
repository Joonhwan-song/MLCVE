from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import subprocess
import docker
import shutil
import countconvert
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QFileDialog


class CollaborateSystem():
    algo = []
    data = []
    def __init__(self, _ui):
        self.ui = _ui;

    def Select_File(self, list_algo,list_dataset,select_algo,select_dataset):
        source_path = self.ui.binaryPath.toPlainText()
        save_path = './cnt'

        if not os.path.isdir(save_path):
            os.makedirs(save_path)

        outputfilename = save_path+'/NewBINARY'

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


    def Copy_Dataset_algo(self, container_name):
        argument = 'docker cp ./dataset ' + container_name+ ':/cve/'
        print(argument)
        subprocess.call(argument,shell=True)

    #2 - make dataset -> one dataset to all container
    def Copy_Dataset_data(self, dataset_name,list_algo):
        print("INSERT COPY_DATASET_DATA")
        print(list_algo)
        for algo in list_algo:
            argument = 'docker cp ./dataset/' + dataset_name + ' ' + algo + ':/cve/dataset/'+dataset_name
            print(argument)
            subprocess.call(argument,shell=True)
            argument = 'docker exec ' + algo + ' python3 save.py ' + dataset_name
            print(argument)
            subprocess.call(argument,shell=True)


    #Learn new algorithm with all dataset
    def Machine_Learn(self, name,list_dataset):
        #exec selected algorithm in container (need to fix run.py)
        for dataset in list_dataset:
            #Run Macine learning
            argument = 'docker exec ' + name + ' python3 save.py ' + dataset
            print(argument)
            subprocess.call(argument,shell=True)

    def closeAddAlgo(self):
        self.ui.waitLearning.show()
        datasetpath = "./dataset"
        list_dataset = self.List_Dataset(datasetpath)
        name = self.ui.addAlgoName.toPlainText()
        image = self.ui.addAlgoPath.toPlainText()
        argument = 'docker run -i -t -d --name ' + name + ' ' + image + ' /bin/bash'
        subprocess.call(argument, shell = True)
        argument = 'docker ps'
        subprocess.call(argument,shell= True)
        self.Copy_Dataset_algo(name)
        self.Machine_Learn(name,list_dataset)
        self.algo.append(QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents_2))
        self.algo[-1].setObjectName(name)
        self.algo[-1].setText(name)
        self.algo[-1].setCheckable(True)
        self.ui.gridLayout.addWidget(self.algo[-1], len(self.algo), 0, 1, 1)
        self.ui.waitLearning.hide()
        self.ui.addAlgoWidgetContent.hide()

    def closeAddData(self):
        datasetpath = "./dataset"
        list_algo = self.List_Algo()
        name = self.ui.addDataName.toPlainText()
        path = self.ui.addDataPath.toPlainText()
        destination = datasetpath + '/' + name
        shutil.copytree(path,destination)
        self.Copy_Dataset_data(name,list_algo)
        self.data.append(QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents_3))
        self.data[-1].setObjectName(name)
        self.data[-1].setText(name)
        self.data[-1].setCheckable(True)
        self.ui.gridLayout_2.addWidget(self.data[-1], len(self.data), 0, 1, 1)
        self.ui.addDataWidgetContent.hide()

    def Select_Algo(self, list_algo):
        #Select Algorithm
        for index,value in enumerate(list_algo,start=0):
            self.algo.append(QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents_2))
            self.algo[index].setObjectName(value)
            self.algo[index].setText(value)
            self.algo[index].setCheckable(True)
            self.ui.gridLayout.addWidget(self.algo[index], index, 0, 1, 1)

        print("start")
        addAlgo = QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents_2)
        addAlgo.setObjectName("Add_Algorithm")
        addAlgo.setText("Add_Algorithm")
        self.ui.gridLayout.addWidget(addAlgo)
        addAlgo.clicked.connect(self.ui.addAlgoFun)
        self.ui.addAgloBtn.clicked.connect(self.closeAddAlgo)


    def Select_Dataset(self, list_dataset):
        #Select Dataset
        for index,value in enumerate(list_dataset,start=0):
            self.data.append(QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents_3))
            self.data[index].setObjectName(value)
            self.data[index].setText(value)
            self.data[index].setCheckable(True)
            self.ui.gridLayout_2.addWidget(self.data[index], index, 0, 1, 1)

        addData = QtWidgets.QPushButton(self.ui.scrollAreaWidgetContents_2)
        addData.setObjectName("Add_dataset")
        addData.setText("Add_dataset")
        self.ui.gridLayout_2.addWidget(addData)
        addData.clicked.connect(self.ui.addDataFun)
        self.ui.addDataBtn.clicked.connect(self.closeAddData)

    def Clicked_Algo(self, algo):
        clicked_algo = []
        for index, value in enumerate(algo):
            if(value.isChecked()):
                clicked_algo.append(index+1)
        return clicked_algo

    def Clicked_Data(self, data):
        clicked_data = []
        for index, value in enumerate(data):
            if(value.isChecked()):
                clicked_data.append(index+1)
        return clicked_data

    def List_Algo(self):
        list_algo=[]
        client = docker.from_env()
        for container in client.containers.list():
                list_algo.append(container.name)
        return list_algo

    def List_Dataset(self, datasetpath):
        list_dataset = os.listdir(datasetpath)
        return list_dataset

    def Print_Result(self, saveHostPath):
        path_dir = saveHostPath
        file_lists = os.listdir(path_dir)
        x = []
        y = []
        for file in file_lists:
            f = open(saveHostPath + '/' + file, "r")
            line = f.readline()
            li = line.split(' ')
            xstr = li[0] + '\n' + li[2]
            x.append(xstr)
            ystr = li[1]
            y.append(int(ystr[:2]))
            self.ui.resultText.append(line)
            os.remove(saveHostPath + '/' + file)
            f.close()
        index = np.arange(len(y))
        plt.bar(index,y)
        plt.xticks(index,x)
        plt.show()
        self.ui.textBrowser_6.hide()


    def Click_Print_Result(self):
        saveHostPath = "./result"
        saveFilePath = "/cve/saveresult"
        datasetpath = "./dataset"
        print('result')
        self.ui.ResultWidget.show()
        list_algo = self.List_Algo()
        list_dataset = self.List_Dataset(datasetpath)
        select_algo = self.Clicked_Algo(self.algo)
        select_dataset = self.Clicked_Data(self.data)
        self.Select_File(list_algo, list_dataset, select_algo, select_dataset)
        self.Make_Result(list_algo,list_dataset,select_algo,select_dataset)
        self.Copy_Result(list_algo,list_dataset,select_algo,select_dataset,saveFilePath,saveHostPath)
        self.Print_Result(saveHostPath)

    def Copy_Result(self, list_algo,list_dataset,select_algo,select_dataset,saveFilePath,saveHostPath):
        for algo in select_algo:
            for data in select_dataset:
                    argument = 'docker cp ' + list_algo[int(algo) -1] + ':' + saveFilePath + '/' + list_algo[int(algo)-1] + '_' + list_dataset[int(data)-1]  + ' ' + saveHostPath
                    print(argument)
                    subprocess.call(argument,shell=True)


    def Make_Result(self, list_algo,list_dataset,select_algo,select_dataset):
        for algo in select_algo:
            for data in select_dataset:
                argument = 'docker exec ' +list_algo[int(algo)-1] + ' python3 load.py ' + list_dataset[int(data)-1]
                print(argument)
                subprocess.call(argument,shell=True)


    def setUP(self):
        datasetpath = "./dataset"
        self.Select_Algo(self.List_Algo())
        self.Select_Dataset(self.List_Dataset(datasetpath))

