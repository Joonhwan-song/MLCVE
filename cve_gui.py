# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cve_gui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import subprocess
import docker
import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 750, 500))
        self.stackedWidget.setObjectName("stackedWidget")
        self.binary_page = QtWidgets.QWidget()
        self.binary_page.setObjectName("binary_page")
        self.textBrowser1 = QtWidgets.QTextBrowser(self.binary_page)
        self.textBrowser1.setGeometry(QtCore.QRect(300, 10, 300, 50))
        self.selectBinaryButton = QtWidgets.QPushButton(self.binary_page)
        self.selectBinaryButton.setGeometry(QtCore.QRect(600, 240, 111, 41))
        self.selectBinaryButton.setObjectName("selectBinaryButton")
        self.textEdit = QtWidgets.QTextEdit(self.binary_page)
        self.textEdit.setGeometry(QtCore.QRect(190, 240, 271, 41))
        self.textEdit.setObjectName("textEdit")
        self.goAlgoButton = QtWidgets.QPushButton(self.binary_page)
        self.goAlgoButton.setGeometry(QtCore.QRect(600, 300, 100, 30))
        self.goAlgoButton.setObjectName("goAlgoButton")
        self.stackedWidget.addWidget(self.binary_page)
        self.algorithm_page = QtWidgets.QWidget()
        self.algorithm_page.setObjectName("algorithm_page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.algorithm_page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 261, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.textBrowser2 = QtWidgets.QTextBrowser(self.algorithm_page)
        self.textBrowser2.setGeometry(QtCore.QRect(300, 10, 300, 50))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.goDataButton = QtWidgets.QPushButton(self.algorithm_page)
        self.goDataButton.setGeometry(QtCore.QRect(600, 300, 100, 30))
        self.goDataButton.setObjectName("goDataButton")
        self.stackedWidget.addWidget(self.algorithm_page)
        self.dataset_page = QtWidgets.QWidget()
        self.dataset_page.setObjectName("dataset_page")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.dataset_page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 30, 251, 301))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.textBrowser3 = QtWidgets.QTextBrowser(self.dataset_page)
        self.textBrowser3.setGeometry(QtCore.QRect(300, 10, 300, 50))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.resultButton = QtWidgets.QPushButton(self.dataset_page)
        self.resultButton.setGeometry(QtCore.QRect(600, 300, 100, 30))
        self.resultButton.setObjectName("resultButton")
        self.stackedWidget.addWidget(self.dataset_page)
        self.result_page = QtWidgets.QWidget()
        self.result_page.setObjectName("result_page")
        self.resultText = QtWidgets.QTextBrowser(self.result_page)
        self.resultText.setGeometry(QtCore.QRect(100, 200, 500,400))
        self.resultText.setObjectName("resultText")
        self.resultText.setText("NotSelect")
        self.textBrowser4 = QtWidgets.QTextBrowser(self.result_page)
        self.textBrowser4.setGeometry(QtCore.QRect(300, 10, 300, 50))
        self.stackedWidget.addWidget(self.result_page)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectBinaryButton.setText(_translate("MainWindow", "Select Binary"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Path</p></body></html>"))
        self.goAlgoButton.setText(_translate("MainWindow", "Next"))
        self.textBrowser1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select Binary File</p></body></html>"))
        self.textBrowser2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select Algorithm</p></body></html>"))
        self.textBrowser3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select Dataset</p></body></html>"))
        self.textBrowser4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">RESULT</p></body></html>"))

        self.goDataButton.setText(_translate("MainWindow", "Next"))
        self.resultButton.setText(_translate("MainWindow", "Next"))

    index = 0
    def nextWidgetWindow(self):
        self.index = self.index +1
        ui.stackedWidget.setCurrentIndex(self.index)

    def preWidgetWindow(self):
        self.index = self.index -1
        ui.stackedWidget.setCurrentIndex(self.index)

    def pushButtonClicked(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME')) 
        #self.label.setText(fname[0])

    def setBtnSignal(self):
        self.goAlgoButton.clicked.connect(self.nextWidgetWindow)
        self.goDataButton.clicked.connect(self.nextWidgetWindow)
        self.resultButton.clicked.connect(self.nextWidgetWindow)
        self.selectBinaryButton.clicked.connect(self.pushButtonClicked)
        
class MachineLearning():
    algo = []
    data = []
    def __init__(self, _ui):
        ui = _ui;

    def Select_Algo(self, list_algo,list_dataset):
        #Select Algorithm
        addAlgo = QtWidgets.QPushButton(ui.verticalLayoutWidget)
        addAlgo.setObjectName("Add_Algorithm")
        addAlgo.setText("Add_Algorithm")
        ui.verticalLayout.addWidget(addAlgo)

        for index,value in enumerate(list_algo,start=1):
            self.algo.append(QtWidgets.QPushButton(ui.verticalLayoutWidget))
            self.algo[index-1].setObjectName(value)
            self.algo[index-1].setText(value)
            self.algo[index-1].setCheckable(True)
            ui.verticalLayout.addWidget(self.algo[index-1])

        """
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
        """

    def Select_Dataset(self, list_algo,list_dataset,datasetpath):
        #Select Dataset
        addData = QtWidgets.QPushButton(ui.verticalLayoutWidget_2)
        addData.setObjectName("Add_dataset")
        addData.setText("Add_dataset")
        ui.verticalLayout_2.addWidget(addData)

        global data 
        for index,value in enumerate(list_dataset,start=1):
            self.data.append(QtWidgets.QPushButton(ui.verticalLayoutWidget_2))
            self.data[index-1].setObjectName(value)
            self.data[index-1].setText(value)
            self.data[index-1].setCheckable(True)
            ui.verticalLayout_2.addWidget(self.data[index-1])
   
        """
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
        """
    #1 - make algo -> all dataset to one container
    #Copy Host dataset to new_container
    def Copy_Dataset_algo(self, container_name):
        argument = 'docker cp ./dataset ' + container_name+ ':/dataset'    
        print(argument)
        subprocess.call(argument,shell=True)

    #2 - make dataset -> one dataset to all container
    def Copy_Dataset_data(self, dataset_name,list_algo):
        print("INSERT COPY_DATASET_DATA")
        print(list_algo)
        for algo in list_algo:
            argument = 'docker cp ./dataset/' + dataset_name + ' ' + algo + ':/dataset/'+dataset_name
            print(argument)
            subprocess.call(argument,shell=True)

    #Learn new algorithm with all dataset
    def Machine_Learn(self, name,list_dataset):
        #exec selected algorithm in container (need to fix run.py)
        for dataset in list_dataset:
            #Run Macine learning
            argument = 'docker exec ' + name + ' python3 run.py' + ' ' + dataset
            #subprocess.call(argument,shell=True)


    #Save each container name to list_algo[]
    def List_Algo(self):
        list_algo=[]
        client = docker.from_env()
        for container in client.containers.list():
                list_algo.append(container.name)
        return list_algo

    def List_Dataset(self, datasetpath):
        list_dataset = os.listdir(datasetpath)
        return list_dataset

    #Copy Result value container to host
    def Copy_Result(self, list_algo,list_dataset,select_algo,select_dataset,saveFilePath,saveHostPath):
        for algo in select_algo:
                for data in select_dataset:
                        argument = 'docker cp ' + list_algo[int(algo) -1] + ':' + saveFilePath + '/' +list_algo[int(algo)-1] + '_' + list_dataset[int(data)-1]  + ' ' + saveHostPath
                        subprocess.call(argument,shell=True)

    #Print result in host directory
    def Print_Result(self, saveHostPath):
        path_dir = saveHostPath
        file_lists = os.listdir(path_dir)
        str = "" 
        for file in file_lists:
                f = open(saveHostPath + '/' + file, "r")
                line = f.readline()
                str = str + line
                ui.resultText.setText(str)
                os.remove(saveHostPath + '/' + file)
                f.close()

    def Print_Result_Fun(self):
        datasetpath = "./dataset"
        list_algo = self.List_Algo() 
        list_dataset = self.List_Dataset(datasetpath) 
        select_algo = []
        for index, _algo in enumerate(self.algo):
            if(self.algo[index].isChecked()):
                select_algo.append(index+1)
        select_dataset = []
        for index, _data in enumerate(self.data):
            if(self.data[index].isChecked()):
                select_dataset.append(index+1)
        saveFilePath = "/saveResult"
        saveHostPath = "./result"
        self.Copy_Result(list_algo,list_dataset,select_algo,select_dataset,saveFilePath,saveHostPath)
        self.Print_Result(saveHostPath)

    def Start(self):
        list_algo = self.List_Algo()
        list_dataset = self.List_Dataset(datasetpath)

        self.Select_Algo(list_algo,list_dataset)
        self.Select_Dataset(list_algo,list_dataset,datasetpath)

        ui.resultButton.clicked.connect(self.Print_Result_Fun)


if __name__ == "__main__":
    #AlgoPath
    saveFilePath = "/saveResult"
    saveHostPath = "./result"
    datasetpath = "./dataset"

    #Program main
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setBtnSignal()
    machineLearning = MachineLearning(ui)
    MainWindow.show()
    machineLearning.Start()
    sys.exit(app.exec_())

