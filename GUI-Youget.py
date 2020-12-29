#!/usr/bin/env python
# coding: utf-8

import sys
import re
import os
from PySide2.QtWidgets import QApplication, QMainWindow,QLabel,QProgressBar
from PySide2.QtCore import Slot,QProcess
from Ui import Ui_GUIDownload



class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.ui = Ui_GUIDownload()
        self.ui.setupUi(self)
        self.setWindowTitle("Gui for you-get")
        self.ui.inputUrl.setText("请输入视频地址")
        self.ui.outputPath.setText("./")
        self.ui.kernelYouget.setChecked(True)
        self.ui.kernelDl.setChecked(False)
        
        self.radiokernelStatus="you-get"
        #self.statusBar().showMessage('下载进度：')
        self.progressBar = QProgressBar()
        self.label = QLabel()
        #self.label2 = QLabel()
        #self.label.setText("准备下载: ")        
        #self.statusBar().addPermanentWidget(self.label)        
        self.statusBar().addPermanentWidget(self.progressBar)
        self.progressBar.setGeometry(0, 0, 100, 5)
        self.progressBar.setRange(0, 100) # 设置进度条的范围
        self.progressBar.setValue(0)
        
        # QProcess object for external app
        self.process = QProcess(self)
        # QProcess emits `readyRead` when there is data to be read
        self.process.readyReadStandardError.connect(self.errorAccur)
        self.process.readyReadStandardOutput.connect(self.progress)
        # Just to prevent accidentally running multiple times
        # Disable the button when process starts, and enable it when it finishes
        self.process.started.connect(lambda:self.ui.downloadButton.setEnabled(False) )
        self.process.finished.connect(self.progressEnd)
        
        self.ui.kernelYouget.toggled.connect(self.radioButtonStatus)
        self.ui.kernelDl.toggled.connect(self.radioButtonStatus)
        self.ui.kernelYougetCustom.toggled.connect(self.radioButtonStatus)
        self.ui.kernelDlCustom.toggled.connect(self.radioButtonStatus)
        
        self.ui.downloadButton.clicked.connect(self.downloadVideo)
    @Slot()
    def radioButtonStatus(self):
        if self.ui.kernelYouget.isChecked():
            self.radiokernelStatus="you-get"
            self.setWindowTitle("Gui for you-get")
            self.ui.label.setText("视频网址")
            self.ui.inputUrl.setText("请输入视频地址")
            self.ui.outputPath.setText("./")
            self.ui.outputPath.setEnabled(True)
            
        if self.ui.kernelDl.isChecked():
            self.radiokernelStatus="youtube-dl"
            self.setWindowTitle("Gui for youtube-dl")
            self.ui.label.setText("视频网址")
            self.ui.inputUrl.setText("请输入视频地址")
            self.ui.outputPath.setText("./")
            self.ui.outputPath.setEnabled(True)
        
        if self.ui.kernelYougetCustom.isChecked():
            self.radiokernelStatus="you-getCustom"
            self.setWindowTitle("Gui for you-get Custom")
            self.ui.label.setText("下载命令")
            self.ui.inputUrl.setText("请输入下载命令")
            self.ui.outputPath.setText("存储路径禁止编辑，请在命令中指定路径")            
            self.ui.outputPath.setEnabled(False)
        
        if self.ui.kernelDlCustom.isChecked():
            self.radiokernelStatus="youtube-dlCustom"
            self.setWindowTitle("Gui for youtube-dl Custom")
            self.ui.label.setText("下载命令")
            self.ui.inputUrl.setText("请输入下载命令")
            self.ui.outputPath.setText("存储路径禁止编辑，请在命令中指定路径")            
            self.ui.outputPath.setEnabled(False)
    
    
    @Slot()
    def progressEnd(self):
        self.ui.downloadButton.setEnabled(True)
        #self.statusBar().showMessage('合并完成')        
        self.ui.kernelDl.setEnabled(True)
        self.ui.kernelDlCustom.setEnabled(True)            
        self.ui.kernelYougetCustom.setEnabled(True)
        self.ui.kernelYouget.setEnabled(True)
        
    @Slot()
    def errorAccur(self):
        data=str(self.process.readAllStandardError().data().decode('gbk')).strip()
        data=data.replace("[33m"," ").replace("[0m"," ")
        print(data)
        if "oops" in data:
            #self.label.setText("出现了一些错误,请检查下载链接")
            self.statusBar().showMessage("出现了一些错误,请检查下载链接")
        elif "exists" in data:
            #self.label.setText("该视频已存在于下载目录下")
            self.statusBar().showMessage("该视频已存在于下载目录下")
        elif "Unsupported URL" in data:
            self.statusBar().showMessage("不支持该网站，请更换下载核心")
        elif "Permission"  in data:
            self.statusBar().showMessage("存储路径权限不足，请检查路径")
        elif "load_cookies" in data:
            self.statusBar().showMessage("不支持的cookie文件格式")
        
        
        with open("./errorlog.txt","a+") as f:
            f.write(data)
        
    @Slot()
    def progress(self):       
        if "you-get" in self.radiokernelStatus:
            dataOutput=str(self.process.readAllStandardOutput().data().decode('utf-8')).strip()
            #dataOutput=dataOutput.replace("[33m","").replace("[0m","")
            #print(dataOutput)   
            p = re.compile(r'%.*[(](.*?)/(.*?)MB[)]', re.S)
            p1= re.compile(r'[]](.*?/s)', re.S)
            speed=re.findall(p1,dataOutput)
            #print("speed is :",speed)
            #p = re.compile(r'(.\d+)%', re.S)
            processBarValue = re.findall(p,dataOutput)
            if len(speed)!= 0 :
                #self.label.setText('正在下载:')
                #print(processBarValue[0])
                dlSize=float(processBarValue[0][0])
                totalSize=float(processBarValue[0][1])
                ProcessValue=dlSize/totalSize*100            
                if ProcessValue==100:
                    self.statusBar().showMessage("下载完成")
                else:
                    self.statusBar().showMessage("正在下载:%s 共 %.2f MB,已下载 %.2f MB"%(speed[0],totalSize,dlSize))
                self.progressBar.setValue(ProcessValue)
        elif "youtube-dl" in self.radiokernelStatus:
            dataOutput=str(self.process.readAllStandardOutput().data().decode('gbk')).strip()
            #dataOutput=dataOutput.replace("[33m","").replace("[0m","")
            #print(dataOutput)   
            p = re.compile(r'[]](.*?)%', re.S)
            processBarValue = re.findall(p,dataOutput)
            p1 = re.compile(r'at(.*?/s)',re.S)
            speed=re.findall(p1,dataOutput)
            p2 = re.compile(r'of(.*?)at',re.S)
            totalSize= re.findall(p2,dataOutput)
            
            #print(processBarValue)
            if len(speed)!= 0 :
                #self.label.setText('正在下载:')
                #print(processBarValue[0])
                ProcessValue=float(processBarValue[0])  
                if ProcessValue==100:
                    self.statusBar().showMessage("下载完成")
                else:
                    self.statusBar().showMessage("正在下载:%s 共 %s"%(speed[0],totalSize[0]))
                self.progressBar.setValue(ProcessValue)
            
        #QMessageBox.warning(self,"程序出错",data)    
    @Slot()
    def downloadVideo(self):
        #import subprocess
        #command="you-get "+self.ui.inputUrl.text() +" -o "+self.ui.outputPath.text()
        if self.radiokernelStatus == "you-get":
            if self.ui.cookiePath.text() != "":
                command=[self.ui.inputUrl.text(),'-o',self.ui.outputPath.text(),"-c",self.ui.cookiePath.text()]
            else:
                command=[self.ui.inputUrl.text(),'-o',self.ui.outputPath.text()]
            abspath=  os.path.abspath(self.ui.outputPath.text())              
            self.process.start('./you-get.exe',command)
            self.progressBar.setValue(0)
            self.ui.outputPath.setText(abspath)
            self.ui.outputPath.setReadOnly(True)
            self.ui.kernelDl.setEnabled(False)
            self.ui.kernelDlCustom.setEnabled(False)            
            self.ui.kernelYougetCustom.setEnabled(False)
            self.ui.kernelYouget.setEnabled(True)
            
        elif self.radiokernelStatus == "youtube-dl":
            if self.ui.cookiePath.text() != "":
                command=[self.ui.inputUrl.text(),'-o',os.path.join(self.ui.outputPath.text() ,"%(title)s.%(ext)s"),\
                         "--cookies",self.ui.cookiePath.text()]
            else:
                command=[self.ui.inputUrl.text(),'-o',os.path.join(self.ui.outputPath.text() ,"%(title)s.%(ext)s")]
            
            abspath=  os.path.abspath(self.ui.outputPath.text())          
            self.process.start('./youtube-dl.exe',command)
            self.progressBar.setValue(0)
            self.ui.outputPath.setText(abspath)
            self.ui.outputPath.setReadOnly(True)
            self.ui.kernelDl.setEnabled(True)
            self.ui.kernelDlCustom.setEnabled(False)            
            self.ui.kernelYougetCustom.setEnabled(False)
            self.ui.kernelYouget.setEnabled(False)
        
        elif self.radiokernelStatus == "youtube-dlCustom":
            UserInput = self.ui.inputUrl.text()
            command=UserInput.split(' ')
            for i in range(len(command)):
                if command[i]=="-o":
                    abspath=os.path.abspath(command[i+1])
                    self.ui.outputPath.setText(abspath)
            
            self.process.start('./youtube-dl.exe',command[1:])
            self.progressBar.setValue(0)
            self.ui.kernelDl.setEnabled(False)
            self.ui.kernelDlCustom.setEnabled(True)            
            self.ui.kernelYougetCustom.setEnabled(False)
            self.ui.kernelYouget.setEnabled(False)
        
        elif self.radiokernelStatus == "you-getCustom":
            UserInput = self.ui.inputUrl.text()
            command=UserInput.split(' ')
            for i in range(len(command)):
                if command[i]=="-o":
                    abspath=os.path.abspath(command[i+1])
                    self.ui.outputPath.setText(abspath)
            #if "-o" in command:
                #self.ui.outputPath.setText(command[-1])
            self.process.start('./you-get.exe',command[1:])
            self.progressBar.setValue(0)
            
            self.ui.kernelDl.setEnabled(False)
            self.ui.kernelDlCustom.setEnabled(False)            
            self.ui.kernelYougetCustom.setEnabled(True)
            self.ui.kernelYouget.setEnabled(False)
        

        
if __name__ == "__main__":
    app=QApplication([])

    window = Gui()
    window.show()

    sys.exit(app.exec_())


# In[ ]:




