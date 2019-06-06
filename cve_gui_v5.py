# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cve_gui_v4.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import subprocess
import docker
import shutil
import countconvert
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    index = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(625, 395)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 591, 407))
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.pushButton = QtWidgets.QPushButton(self.main_page)
        self.pushButton.setGeometry(QtCore.QRect(130, 300, 341, 61))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.main_page)
        self.textBrowser_5.setGeometry(QtCore.QRect(80, 30, 441, 241))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.stackedWidget.addWidget(self.main_page)
        self.binary_page = QtWidgets.QWidget()
        self.binary_page.setObjectName("binary_page")
        self.selectBinaryButton = QtWidgets.QPushButton(self.binary_page)
        self.selectBinaryButton.setGeometry(QtCore.QRect(440, 270, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.selectBinaryButton.setFont(font)
        self.selectBinaryButton.setObjectName("selectBinaryButton")
        self.binaryPath = QtWidgets.QTextEdit(self.binary_page)
        self.binaryPath.setGeometry(QtCore.QRect(60, 270, 371, 80))
        self.binaryPath.setObjectName("binaryPath")
        self.goAlgoBtn = QtWidgets.QPushButton(self.binary_page)
        self.goAlgoBtn.setGeometry(QtCore.QRect(450, 340, 99, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.goAlgoBtn.setFont(font)
        self.goAlgoBtn.setObjectName("goAlgoBtn")
        self.textBrowser = QtWidgets.QTextBrowser(self.binary_page)
        self.textBrowser.setGeometry(QtCore.QRect(150, 20, 300, 45))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.binary_page)
        self.textBrowser_7.setGeometry(QtCore.QRect(60, 201, 371, 51))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.stackedWidget.addWidget(self.binary_page)
        self.algorithm_page = QtWidgets.QWidget()
        self.algorithm_page.setObjectName("algorithm_page")
        self.goDataBtn = QtWidgets.QPushButton(self.algorithm_page)
        self.goDataBtn.setGeometry(QtCore.QRect(450, 340, 99, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.goDataBtn.setFont(font)
        self.goDataBtn.setObjectName("goDataBtn")
        self.BackBinaryBtn = QtWidgets.QPushButton(self.algorithm_page)
        self.BackBinaryBtn.setGeometry(QtCore.QRect(340, 340, 99, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BackBinaryBtn.setFont(font)
        self.BackBinaryBtn.setObjectName("BackBinaryBtn")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.algorithm_page)
        self.textBrowser_2.setGeometry(QtCore.QRect(150, 20, 300, 45))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.scrollArea = QtWidgets.QScrollArea(self.algorithm_page)
        self.scrollArea.setGeometry(QtCore.QRect(30, 100, 550, 200))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 548, 198))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.addAlgoWidgetContent = QtWidgets.QWidget(self.algorithm_page)
        self.addAlgoWidgetContent.setGeometry(QtCore.QRect(30, 80, 550, 250))
        self.addAlgoWidgetContent.setObjectName("addAlgoWidgetContent")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.addAlgoWidgetContent)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.addAlgoArea = QtWidgets.QScrollArea(self.addAlgoWidgetContent)
        self.addAlgoArea.setWidgetResizable(True)
        self.addAlgoArea.setObjectName("addAlgoArea")
        self.addAlgowidget = QtWidgets.QWidget()
        self.addAlgowidget.setGeometry(QtCore.QRect(0, 0, 530, 230))
        self.addAlgowidget.setObjectName("addAlgowidget")
        self.addAlgoPath = QtWidgets.QTextEdit(self.addAlgowidget)
        self.addAlgoPath.setGeometry(QtCore.QRect(130, 170, 261, 41))
        self.addAlgoPath.setObjectName("addAlgoPath")
        self.addAlgoText = QtWidgets.QTextBrowser(self.addAlgowidget)
        self.addAlgoText.setGeometry(QtCore.QRect(10, 70, 381, 41))
        self.addAlgoText.setObjectName("addAlgoText")
        self.addAgloBtn = QtWidgets.QPushButton(self.addAlgowidget)
        self.addAgloBtn.setGeometry(QtCore.QRect(400, 70, 81, 81))
        self.addAgloBtn.setObjectName("addAgloBtn")
        self.addAlgoName = QtWidgets.QTextEdit(self.addAlgowidget)
        self.addAlgoName.setGeometry(QtCore.QRect(130, 120, 261, 41))
        self.addAlgoName.setObjectName("addAlgoName")
        self.addAlgoWidgetContent.hide()
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.addAlgowidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(20, 120, 101, 41))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.addAlgowidget)
        self.textBrowser_9.setGeometry(QtCore.QRect(20, 170, 101, 41))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.addAlgoArea.setWidget(self.addAlgowidget)
        self.gridLayout_4.addWidget(self.addAlgoArea, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.algorithm_page)
        self.dataset_page = QtWidgets.QWidget()
        self.dataset_page.setObjectName("dataset_page")
        self.goResultBtn = QtWidgets.QPushButton(self.dataset_page)
        self.goResultBtn.setGeometry(QtCore.QRect(450, 340, 99, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.goResultBtn.setFont(font)
        self.goResultBtn.setObjectName("goResultBtn")
        self.BackAlgoBtn = QtWidgets.QPushButton(self.dataset_page)
        self.BackAlgoBtn.setGeometry(QtCore.QRect(340, 340, 99, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BackAlgoBtn.setFont(font)
        self.BackAlgoBtn.setObjectName("BackAlgoBtn")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.dataset_page)
        self.textBrowser_4.setGeometry(QtCore.QRect(150, 20, 300, 45))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.dataset_page)
        self.scrollArea_2.setGeometry(QtCore.QRect(30, 100, 550, 200))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 548, 198))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.addDataWidgetContent = QtWidgets.QWidget(self.dataset_page)
        self.addDataWidgetContent.setGeometry(QtCore.QRect(30, 70, 550, 250))
        self.addDataWidgetContent.setObjectName("addDataWidgetContent")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.addDataWidgetContent)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.addDataArea = QtWidgets.QScrollArea(self.addDataWidgetContent)
        self.addDataArea.setWidgetResizable(True)
        self.addDataArea.setObjectName("addDataArea")
        self.addDatawidget = QtWidgets.QWidget()
        self.addDatawidget.setGeometry(QtCore.QRect(0, 0, 530, 230))
        self.addDatawidget.setObjectName("addDatawidget")
        self.addDataName = QtWidgets.QTextEdit(self.addDatawidget)
        self.addDataName.setGeometry(QtCore.QRect(150, 120, 241, 41))
        self.addDataName.setObjectName("addDataName")
        self.addDataText = QtWidgets.QTextBrowser(self.addDatawidget)
        self.addDataText.setGeometry(QtCore.QRect(10, 70, 381, 41))
        self.addDataText.setObjectName("addDataText")
        self.addDataBtn = QtWidgets.QPushButton(self.addDatawidget)
        self.addDataBtn.setGeometry(QtCore.QRect(400, 70, 81, 81))
        self.addDataBtn.setObjectName("addDataBtn")
        self.addDataPath = QtWidgets.QTextEdit(self.addDatawidget)
        self.addDataPath.setGeometry(QtCore.QRect(150, 170, 241, 41))
        self.addDataPath.setObjectName("addDataPath")
        self.addDataWidgetContent.hide()
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.addDatawidget)
        self.textBrowser_10.setGeometry(QtCore.QRect(20, 120, 101, 41))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.addDatawidget)
        self.textBrowser_11.setGeometry(QtCore.QRect(20, 170, 101, 41))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.addDataArea.setWidget(self.addDatawidget)
        self.gridLayout_5.addWidget(self.addDataArea, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.dataset_page)
        self.result_page = QtWidgets.QWidget()
        self.result_page.setObjectName("result_page")
        self.resultText = QtWidgets.QTextEdit(self.result_page)
        self.resultText.setGeometry(QtCore.QRect(10, 70, 581, 261))
        self.resultText.setObjectName("resultText")
        self.pushButton_4 = QtWidgets.QPushButton(self.result_page)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 340, 99, 27))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.result_page)
        self.textBrowser_3.setGeometry(QtCore.QRect(150, 20, 300, 45))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.widget = QtWidgets.QWidget(self.result_page)
        self.widget.setGeometry(QtCore.QRect(0, 10, 601, 331))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_6.hide()
        self.gridLayout_3.addWidget(self.textBrowser_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.result_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.setBtnSignal()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">ML - CVE</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Machine Learning</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Collaborative Vulnerability Explorer</span></p></body></html>"))
        self.selectBinaryButton.setText(_translate("MainWindow", "Find"))
        self.binaryPath.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.goAlgoBtn.setText(_translate("MainWindow", "Next"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Select Binary File</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Set Binary File Path</p></body></html>"))
        self.goDataBtn.setText(_translate("MainWindow", "Next"))
        self.BackBinaryBtn.setText(_translate("MainWindow", "Back"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Select Algorithm</span></p></body></html>"))
        self.addAlgoText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Please image name and specify the path</span></p></body></html>"))
        self.addAgloBtn.setText(_translate("MainWindow", "OK"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Name</p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Image</p></body></html>"))
        self.goResultBtn.setText(_translate("MainWindow", "Next"))
        self.BackAlgoBtn.setText(_translate("MainWindow", "Back"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Select Dataset</span></p></body></html>"))
        self.addDataText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Please specify the path to the Dataset</span></p></body></html>"))
        self.addDataBtn.setText(_translate("MainWindow", "OK"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Name</p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Data</p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "EXIT"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">RESULT</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Produce Results....</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">.....</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">....</span></p></body></html>"))

    def nextWidgetWindow(self):
        self.index = self.index +1
        ui.stackedWidget.setCurrentIndex(self.index)

    def preWidgetWindow(self):
        self.index = self.index -1
        ui.stackedWidget.setCurrentIndex(self.index)

    def exitProgram(self):
       sys.exit()

    def pushButtonClicked(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        #self.label.setText(fname[0])

    def addAlgoFun(self):
        self.addAlgoWidgetContent.show()

    def closeAddAlgo(self):
        self.addAlgoWidgetContent.hide()

    def addDataFun(self):
        self.addDataWidgetContent.show()

    def closeAddData(self):
        self.addAlgoWidgetContent.hide()

    def addBinaryBtn(self):
        filename = QFileDialog.getOpenFileName()
        self.binaryPath.setText(filename[0])

    def setBtnSignal(self):
        self.pushButton.clicked.connect(self.nextWidgetWindow)
        self.goAlgoBtn.clicked.connect(self.nextWidgetWindow)
        self.goDataBtn.clicked.connect(self.nextWidgetWindow)
        self.goResultBtn.clicked.connect(self.nextWidgetWindow)
        self.BackBinaryBtn.clicked.connect(self.preWidgetWindow)
        self.BackAlgoBtn.clicked.connect(self.preWidgetWindow)
        self.pushButton_4.clicked.connect(self.exitProgram)
        self.selectBinaryButton.clicked.connect(self.addBinaryBtn)

class CollaborateSystem():
    algo = []
    data = []
    def __init__(self, _ui):
        ui = _ui;

    def Select_File(self, list_algo,list_dataset,select_algo,select_dataset):
        source_path = ui.binaryPath.toPlainText() 
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
        datasetpath = "./dataset"
        list_dataset = self.List_Dataset(datasetpath)
        name = ui.addAlgoName.toPlainText() 
        image = ui.addAlgoPath.toPlainText() 
        argument = 'docker run -i -t -d --name ' + name + ' ' + image + ' /bin/bash'
        subprocess.call(argument, shell = True)
        argument = 'docker ps'
        subprocess.call(argument,shell= True)
        self.Copy_Dataset_algo(name)
        self.Machine_Learn(name,list_dataset)
        self.algo.append(QtWidgets.QPushButton(ui.scrollAreaWidgetContents_2))
        self.algo[-1].setObjectName(name)
        self.algo[-1].setText(name)
        self.algo[-1].setCheckable(True)
        ui.gridLayout.addWidget(self.algo[-1], len(self.algo), 0, 1, 1)
        ui.addAlgoWidgetContent.hide()

    def closeAddData(self):
        datasetpath = "./dataset" 
        list_algo = self.List_Algo()
        name = ui.addDataName.toPlainText() 
        path = ui.addDataPath.toPlainText()
        destination = datasetpath + '/' + name
        shutil.copytree(path,destination)
        self.Copy_Dataset_data(name,list_algo)
        self.data.append(QtWidgets.QPushButton(ui.scrollAreaWidgetContents_3))
        self.data[-1].setObjectName(name)
        self.data[-1].setText(name)
        self.data[-1].setCheckable(True)
        ui.gridLayout_2.addWidget(self.data[-1], len(self.data), 0, 1, 1)
        ui.addDataWidgetContent.hide()


    def Select_Algo(self, list_algo):
        #Select Algorithm
        for index,value in enumerate(list_algo,start=0):
            self.algo.append(QtWidgets.QPushButton(ui.scrollAreaWidgetContents_2))
            self.algo[index].setObjectName(value)
            self.algo[index].setText(value)
            self.algo[index].setCheckable(True)
            ui.gridLayout.addWidget(self.algo[index], index, 0, 1, 1)

        addAlgo = QtWidgets.QPushButton(ui.scrollAreaWidgetContents_2)
        addAlgo.setObjectName("Add_Algorithm")
        addAlgo.setText("Add_Algorithm")
        ui.gridLayout.addWidget(addAlgo)
        addAlgo.clicked.connect(ui.addAlgoFun)
        ui.addAgloBtn.clicked.connect(self.closeAddAlgo)


    def Select_Dataset(self, list_dataset):
        #Select Dataset
        for index,value in enumerate(list_dataset,start=0):
            self.data.append(QtWidgets.QPushButton(ui.scrollAreaWidgetContents_3))
            self.data[index].setObjectName(value)
            self.data[index].setText(value)
            self.data[index].setCheckable(True)
            ui.gridLayout_2.addWidget(self.data[index], index, 0, 1, 1)

        addData = QtWidgets.QPushButton(ui.scrollAreaWidgetContents_2)
        addData.setObjectName("Add_dataset")
        addData.setText("Add_dataset")
        ui.gridLayout_2.addWidget(addData)
        addData.clicked.connect(ui.addDataFun)
        ui.addDataBtn.clicked.connect(self.closeAddData)

    def Clicked_Algo(self, algo):
        clicked_algo = []
        for index, value in enumerate(algo):
            if(value.isChecked()):
                #clicked_algo.append(value.text())
                clicked_algo.append(index+1)
        return clicked_algo

    def Clicked_Data(self, data):
        clicked_data = []
        for index, value in enumerate(data):
            if(value.isChecked()):
                #clicked_data.append(value.text())
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
        for file in file_lists:
            f = open(saveHostPath + '/' + file, "r")
            line = f.readline()
            ui.resultText.append(line)
            os.remove(saveHostPath + '/' + file)
            f.close()

    def Click_Print_Result(self):
        saveHostPath = "./result"
        saveFilePath = "/cve/saveresult"
        datasetpath = "./dataset"
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
                    argument = 'docker cp ' + list_algo[int(algo) -1] + ':' + saveFilePath + '/' +list_algo[int(algo)-1] + '_' + list_dataset[int(data)-1]  + ' ' + saveHostPath
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    cs = CollaborateSystem(ui)
    cs.setUP()
    MainWindow.show()
    ui.goResultBtn.clicked.connect(cs.Click_Print_Result)
    sys.exit(app.exec_())
