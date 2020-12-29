# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GUIDownload(object):
    def setupUi(self, GUIDownload):
        if not GUIDownload.objectName():
            GUIDownload.setObjectName(u"GUIDownload")
        GUIDownload.resize(639, 481)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GUIDownload.sizePolicy().hasHeightForWidth())
        GUIDownload.setSizePolicy(sizePolicy)
        GUIDownload.setMaximumSize(QSize(639, 512))
        self.verticalLayoutWidget = QWidget(GUIDownload)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 40, 561, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 10)
        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayoutWidget_2 = QWidget(self.groupBox)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(29, 40, 491, 111))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.kernelYougetCustom = QRadioButton(self.gridLayoutWidget_2)
        self.kernelYougetCustom.setObjectName(u"kernelYougetCustom")

        self.gridLayout_2.addWidget(self.kernelYougetCustom, 1, 0, 1, 1)

        self.kernelDlCustom = QRadioButton(self.gridLayoutWidget_2)
        self.kernelDlCustom.setObjectName(u"kernelDlCustom")

        self.gridLayout_2.addWidget(self.kernelDlCustom, 1, 1, 1, 1)

        self.kernelYouget = QRadioButton(self.gridLayoutWidget_2)
        self.kernelYouget.setObjectName(u"kernelYouget")

        self.gridLayout_2.addWidget(self.kernelYouget, 0, 0, 1, 1)

        self.kernelDl = QRadioButton(self.gridLayoutWidget_2)
        self.kernelDl.setObjectName(u"kernelDl")

        self.gridLayout_2.addWidget(self.kernelDl, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayoutWidget = QWidget(self.groupBox_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 40, 511, 111))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.outputPath = QLineEdit(self.gridLayoutWidget)
        self.outputPath.setObjectName(u"outputPath")

        self.gridLayout.addWidget(self.outputPath, 1, 1, 1, 1)

        self.inputUrl = QLineEdit(self.gridLayoutWidget)
        self.inputUrl.setObjectName(u"inputUrl")

        self.gridLayout.addWidget(self.inputUrl, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.cookiePath = QLineEdit(self.gridLayoutWidget)
        self.cookiePath.setObjectName(u"cookiePath")

        self.gridLayout.addWidget(self.cookiePath, 2, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.downloadButton = QPushButton(self.verticalLayoutWidget)
        self.downloadButton.setObjectName(u"downloadButton")

        self.verticalLayout.addWidget(self.downloadButton)


        self.retranslateUi(GUIDownload)

        QMetaObject.connectSlotsByName(GUIDownload)
    # setupUi

    def retranslateUi(self, GUIDownload):
        GUIDownload.setWindowTitle(QCoreApplication.translate("GUIDownload", u"Gui-Download", None))
        self.groupBox.setTitle(QCoreApplication.translate("GUIDownload", u"\u4e0b\u8f7d\u6838\u5fc3", None))
        self.kernelYougetCustom.setText(QCoreApplication.translate("GUIDownload", u"you-get\uff08\u9ad8\u7ea7\u6a21\u5f0f\uff09", None))
        self.kernelDlCustom.setText(QCoreApplication.translate("GUIDownload", u"youtube-dl(\u9ad8\u7ea7\u6a21\u5f0f)", None))
        self.kernelYouget.setText(QCoreApplication.translate("GUIDownload", u"you-get(\u7b80\u6613\u6a21\u5f0f)", None))
        self.kernelDl.setText(QCoreApplication.translate("GUIDownload", u"youtube-dl\uff08\u7b80\u6613\u6a21\u5f0f\uff09", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("GUIDownload", u"\u89c6\u9891\u7f51\u5740", None))
        self.label.setText(QCoreApplication.translate("GUIDownload", u"\u89c6\u9891\u5730\u5740", None))
        self.label_2.setText(QCoreApplication.translate("GUIDownload", u"\u5b58\u50a8\u8def\u5f84", None))
        self.outputPath.setText("")
        self.label_3.setText(QCoreApplication.translate("GUIDownload", u"cookie\u8def\u5f84", None))
        self.downloadButton.setText(QCoreApplication.translate("GUIDownload", u"\u5f00\u59cb\u4e0b\u8f7d", None))
    # retranslateUi

