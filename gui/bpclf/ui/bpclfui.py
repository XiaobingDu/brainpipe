# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bpclf.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_bpui(object):
    def setupUi(self, bpui):
        bpui.setObjectName(_fromUtf8("bpui"))
        bpui.resize(1296, 890)
        self.centralwidget = QtGui.QWidget(bpui)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(550, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(600, 16777215))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabData = QtGui.QWidget()
        self.tabData.setObjectName(_fromUtf8("tabData"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabData)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_3 = QtGui.QGroupBox(self.tabData)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.loadFile1 = QtGui.QPushButton(self.groupBox_3)
        self.loadFile1.setObjectName(_fromUtf8("loadFile1"))
        self.horizontalLayout_4.addWidget(self.loadFile1)
        self.loadFile2 = QtGui.QPushButton(self.groupBox_3)
        self.loadFile2.setObjectName(_fromUtf8("loadFile2"))
        self.horizontalLayout_4.addWidget(self.loadFile2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_6 = QtGui.QGroupBox(self.tabData)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.d1Panel = QtGui.QWidget(self.groupBox_6)
        self.d1Panel.setObjectName(_fromUtf8("d1Panel"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.d1Panel)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.groupBox_7 = QtGui.QGroupBox(self.d1Panel)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_9 = QtGui.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_15.addWidget(self.label_9)
        self.d1Name = QtGui.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.d1Name.setFont(font)
        self.d1Name.setText(_fromUtf8(""))
        self.d1Name.setObjectName(_fromUtf8("d1Name"))
        self.horizontalLayout_15.addWidget(self.d1Name)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.verticalLayout_12.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_7 = QtGui.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_9.addWidget(self.label_7)
        self.d1Shape = QtGui.QLabel(self.groupBox_7)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.d1Shape.setFont(font)
        self.d1Shape.setText(_fromUtf8(""))
        self.d1Shape.setObjectName(_fromUtf8("d1Shape"))
        self.horizontalLayout_9.addWidget(self.d1Shape)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.d1Fce = QtGui.QListWidget(self.groupBox_7)
        self.d1Fce.setObjectName(_fromUtf8("d1Fce"))
        self.verticalLayout_12.addWidget(self.d1Fce)
        self.verticalLayout_14.addWidget(self.groupBox_7)
        self.verticalLayout_7.addWidget(self.d1Panel)
        self.d2Panel = QtGui.QWidget(self.groupBox_6)
        self.d2Panel.setObjectName(_fromUtf8("d2Panel"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.d2Panel)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.groupBox_8 = QtGui.QGroupBox(self.d2Panel)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.verticalLayout_13 = QtGui.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.label_12 = QtGui.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_18.addWidget(self.label_12)
        self.d2Name = QtGui.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.d2Name.setFont(font)
        self.d2Name.setText(_fromUtf8(""))
        self.d2Name.setObjectName(_fromUtf8("d2Name"))
        self.horizontalLayout_18.addWidget(self.d2Name)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem4)
        self.verticalLayout_13.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_8 = QtGui.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_13.addWidget(self.label_8)
        self.d2Shape = QtGui.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.d2Shape.setFont(font)
        self.d2Shape.setText(_fromUtf8(""))
        self.d2Shape.setObjectName(_fromUtf8("d2Shape"))
        self.horizontalLayout_13.addWidget(self.d2Shape)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem5)
        self.verticalLayout_13.addLayout(self.horizontalLayout_13)
        self.d2Fce = QtGui.QListWidget(self.groupBox_8)
        self.d2Fce.setObjectName(_fromUtf8("d2Fce"))
        self.verticalLayout_13.addWidget(self.d2Fce)
        self.verticalLayout_15.addWidget(self.groupBox_8)
        self.verticalLayout_7.addWidget(self.d2Panel)
        self.verticalLayout_5.addWidget(self.groupBox_6)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem7)
        self.resetData = QtGui.QPushButton(self.tabData)
        self.resetData.setObjectName(_fromUtf8("resetData"))
        self.horizontalLayout_14.addWidget(self.resetData)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.tabWidget.addTab(self.tabData, _fromUtf8(""))
        self.tabSF = QtGui.QWidget()
        self.tabSF.setObjectName(_fromUtf8("tabSF"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tabSF)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox = QtGui.QGroupBox(self.tabSF)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.SFfce = QtGui.QComboBox(self.groupBox)
        self.SFfce.setObjectName(_fromUtf8("SFfce"))
        self.horizontalLayout_2.addWidget(self.SFfce)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.clfGrp = QtGui.QGroupBox(self.tabSF)
        self.clfGrp.setObjectName(_fromUtf8("clfGrp"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.clfGrp)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.groupBox_4 = QtGui.QGroupBox(self.clfGrp)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_7.addWidget(self.label_2)
        self.SFclf = QtGui.QComboBox(self.groupBox_4)
        self.SFclf.setObjectName(_fromUtf8("SFclf"))
        self.SFclf.addItem(_fromUtf8(""))
        self.SFclf.addItem(_fromUtf8(""))
        self.SFclf.addItem(_fromUtf8(""))
        self.SFclf.addItem(_fromUtf8(""))
        self.SFclf.addItem(_fromUtf8(""))
        self.horizontalLayout_7.addWidget(self.SFclf)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.knnW = QtGui.QWidget(self.groupBox_4)
        self.knnW.setObjectName(_fromUtf8("knnW"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.knnW)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_5 = QtGui.QLabel(self.knnW)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_11.addWidget(self.label_5)
        self.knnN = QtGui.QSpinBox(self.knnW)
        self.knnN.setMinimum(1)
        self.knnN.setMaximum(100)
        self.knnN.setProperty("value", 10)
        self.knnN.setObjectName(_fromUtf8("knnN"))
        self.horizontalLayout_11.addWidget(self.knnN)
        self.gridLayout.addWidget(self.knnW, 0, 1, 1, 1)
        self.svmW = QtGui.QWidget(self.groupBox_4)
        self.svmW.setObjectName(_fromUtf8("svmW"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.svmW)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_4 = QtGui.QLabel(self.svmW)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_10.addWidget(self.label_4)
        self.svmRBF = QtGui.QRadioButton(self.svmW)
        self.svmRBF.setChecked(True)
        self.svmRBF.setObjectName(_fromUtf8("svmRBF"))
        self.horizontalLayout_10.addWidget(self.svmRBF)
        self.svmLin = QtGui.QRadioButton(self.svmW)
        self.svmLin.setObjectName(_fromUtf8("svmLin"))
        self.horizontalLayout_10.addWidget(self.svmLin)
        self.label_4.raise_()
        self.svmLin.raise_()
        self.svmRBF.raise_()
        self.gridLayout.addWidget(self.svmW, 0, 0, 1, 1)
        self.rfW = QtGui.QWidget(self.groupBox_4)
        self.rfW.setObjectName(_fromUtf8("rfW"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.rfW)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_6 = QtGui.QLabel(self.rfW)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_12.addWidget(self.label_6)
        self.rfNtree = QtGui.QSpinBox(self.rfW)
        self.rfNtree.setMinimum(10)
        self.rfNtree.setMaximum(10000000)
        self.rfNtree.setProperty("value", 100)
        self.rfNtree.setObjectName(_fromUtf8("rfNtree"))
        self.horizontalLayout_12.addWidget(self.rfNtree)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.gridLayout.addWidget(self.rfW, 0, 2, 1, 1)
        self.verticalLayout_10.addLayout(self.gridLayout)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem12)
        self.clfConf = QtGui.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clfConf.setFont(font)
        self.clfConf.setText(_fromUtf8(""))
        self.clfConf.setObjectName(_fromUtf8("clfConf"))
        self.horizontalLayout_19.addWidget(self.clfConf)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem13)
        self.verticalLayout_10.addLayout(self.horizontalLayout_19)
        self.verticalLayout_8.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.clfGrp)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_3 = QtGui.QLabel(self.groupBox_5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_8.addWidget(self.label_3)
        self.cvType = QtGui.QComboBox(self.groupBox_5)
        self.cvType.setObjectName(_fromUtf8("cvType"))
        self.cvType.addItem(_fromUtf8(""))
        self.cvType.addItem(_fromUtf8(""))
        self.cvType.addItem(_fromUtf8(""))
        self.cvType.addItem(_fromUtf8(""))
        self.horizontalLayout_8.addWidget(self.cvType)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_37 = QtGui.QHBoxLayout()
        self.horizontalLayout_37.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_37.setObjectName(_fromUtf8("horizontalLayout_37"))
        self.label_26 = QtGui.QLabel(self.groupBox_5)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_37.addWidget(self.label_26)
        self.cvNfold = QtGui.QSpinBox(self.groupBox_5)
        self.cvNfold.setMinimum(3)
        self.cvNfold.setMaximum(10000)
        self.cvNfold.setProperty("value", 10)
        self.cvNfold.setObjectName(_fromUtf8("cvNfold"))
        self.horizontalLayout_37.addWidget(self.cvNfold)
        spacerItem15 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem15)
        self.verticalLayout_11.addLayout(self.horizontalLayout_37)
        self.horizontalLayout_36 = QtGui.QHBoxLayout()
        self.horizontalLayout_36.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_36.setObjectName(_fromUtf8("horizontalLayout_36"))
        self.label_25 = QtGui.QLabel(self.groupBox_5)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_36.addWidget(self.label_25)
        self.cvRep = QtGui.QSpinBox(self.groupBox_5)
        self.cvRep.setMinimum(1)
        self.cvRep.setMaximum(10)
        self.cvRep.setObjectName(_fromUtf8("cvRep"))
        self.horizontalLayout_36.addWidget(self.cvRep)
        spacerItem16 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_36.addItem(spacerItem16)
        self.verticalLayout_11.addLayout(self.horizontalLayout_36)
        self.horizontalLayout_35 = QtGui.QHBoxLayout()
        self.horizontalLayout_35.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_35.setObjectName(_fromUtf8("horizontalLayout_35"))
        spacerItem17 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem17)
        self.cvConf = QtGui.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cvConf.setFont(font)
        self.cvConf.setText(_fromUtf8(""))
        self.cvConf.setObjectName(_fromUtf8("cvConf"))
        self.horizontalLayout_35.addWidget(self.cvConf)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_35.addItem(spacerItem18)
        self.verticalLayout_11.addLayout(self.horizontalLayout_35)
        self.verticalLayout_8.addWidget(self.groupBox_5)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_6.addWidget(self.clfGrp)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem19 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem19)
        self.runSF = QtGui.QPushButton(self.tabSF)
        self.runSF.setObjectName(_fromUtf8("runSF"))
        self.horizontalLayout_6.addWidget(self.runSF)
        spacerItem20 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem20)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        spacerItem21 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem21)
        self.tabWidget.addTab(self.tabSF, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_20 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_20.setObjectName(_fromUtf8("verticalLayout_20"))
        self.groupBox_9 = QtGui.QGroupBox(self.tab)
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.horizontalLayout_17 = QtGui.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        spacerItem22 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem22)
        self.barBut = QtGui.QRadioButton(self.groupBox_9)
        self.barBut.setChecked(True)
        self.barBut.setObjectName(_fromUtf8("barBut"))
        self.horizontalLayout_16.addWidget(self.barBut)
        spacerItem23 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem23)
        self.topoBut = QtGui.QRadioButton(self.groupBox_9)
        self.topoBut.setObjectName(_fromUtf8("topoBut"))
        self.horizontalLayout_16.addWidget(self.topoBut)
        spacerItem24 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem24)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)
        self.verticalLayout_20.addWidget(self.groupBox_9)
        self.barW = QtGui.QWidget(self.tab)
        self.barW.setObjectName(_fromUtf8("barW"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.barW)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.groupBox_2 = QtGui.QGroupBox(self.barW)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_21 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_21.setObjectName(_fromUtf8("verticalLayout_21"))
        self.horizontalLayout_38 = QtGui.QHBoxLayout()
        self.horizontalLayout_38.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_38.setObjectName(_fromUtf8("horizontalLayout_38"))
        self.label_27 = QtGui.QLabel(self.groupBox_2)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_38.addWidget(self.label_27)
        self.daUpper = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.daUpper.setMaximum(100.0)
        self.daUpper.setObjectName(_fromUtf8("daUpper"))
        self.horizontalLayout_38.addWidget(self.daUpper)
        spacerItem25 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem25)
        self.verticalLayout_21.addLayout(self.horizontalLayout_38)
        self.verticalLayout_16.addWidget(self.groupBox_2)
        self.verticalLayout_20.addWidget(self.barW)
        self.topoW = QtGui.QWidget(self.tab)
        self.topoW.setObjectName(_fromUtf8("topoW"))
        self.verticalLayout_18 = QtGui.QVBoxLayout(self.topoW)
        self.verticalLayout_18.setObjectName(_fromUtf8("verticalLayout_18"))
        self.groupBox_10 = QtGui.QGroupBox(self.topoW)
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.groupBox_10)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        spacerItem26 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem26)
        self.label_10 = QtGui.QLabel(self.groupBox_10)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_20.addWidget(self.label_10)
        self.vminSpin = QtGui.QDoubleSpinBox(self.groupBox_10)
        self.vminSpin.setProperty("value", 50.0)
        self.vminSpin.setObjectName(_fromUtf8("vminSpin"))
        self.horizontalLayout_20.addWidget(self.vminSpin)
        spacerItem27 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem27)
        self.label_11 = QtGui.QLabel(self.groupBox_10)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_20.addWidget(self.label_11)
        self.vmaxSpin = QtGui.QDoubleSpinBox(self.groupBox_10)
        self.vmaxSpin.setMaximum(100.0)
        self.vmaxSpin.setProperty("value", 100.0)
        self.vmaxSpin.setObjectName(_fromUtf8("vmaxSpin"))
        self.horizontalLayout_20.addWidget(self.vmaxSpin)
        spacerItem28 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem28)
        self.label_13 = QtGui.QLabel(self.groupBox_10)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_20.addWidget(self.label_13)
        self.cmapCombo = QtGui.QComboBox(self.groupBox_10)
        self.cmapCombo.setObjectName(_fromUtf8("cmapCombo"))
        self.horizontalLayout_20.addWidget(self.cmapCombo)
        spacerItem29 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem29)
        self.verticalLayout_19.addLayout(self.horizontalLayout_20)
        self.verticalLayout_18.addWidget(self.groupBox_10)
        self.verticalLayout_20.addWidget(self.topoW)
        self.horizontalLayout_39 = QtGui.QHBoxLayout()
        self.horizontalLayout_39.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_39.setObjectName(_fromUtf8("horizontalLayout_39"))
        spacerItem30 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem30)
        self.updatePlot = QtGui.QPushButton(self.tab)
        self.updatePlot.setObjectName(_fromUtf8("updatePlot"))
        self.horizontalLayout_39.addWidget(self.updatePlot)
        spacerItem31 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem31)
        self.verticalLayout_20.addLayout(self.horizontalLayout_39)
        spacerItem32 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_20.addItem(spacerItem32)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.userMsg = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.userMsg.setFont(font)
        self.userMsg.setObjectName(_fromUtf8("userMsg"))
        self.verticalLayout.addWidget(self.userMsg)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.mplwindow = QtGui.QWidget(self.centralwidget)
        self.mplwindow.setMinimumSize(QtCore.QSize(600, 0))
        self.mplwindow.setObjectName(_fromUtf8("mplwindow"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.mplwindow)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, 20)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.mplbox = QtGui.QVBoxLayout()
        self.mplbox.setObjectName(_fromUtf8("mplbox"))
        self.verticalLayout_4.addLayout(self.mplbox)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.mplwindow)
        bpui.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(bpui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1296, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFiles = QtGui.QMenu(self.menubar)
        self.menuFiles.setObjectName(_fromUtf8("menuFiles"))
        self.menuMode = QtGui.QMenu(self.menubar)
        self.menuMode.setObjectName(_fromUtf8("menuMode"))
        bpui.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(bpui)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        bpui.setStatusBar(self.statusbar)
        self.actionAdvanced = QtGui.QAction(bpui)
        self.actionAdvanced.setCheckable(True)
        self.actionAdvanced.setObjectName(_fromUtf8("actionAdvanced"))
        self.menuMode.addAction(self.actionAdvanced)
        self.menubar.addAction(self.menuFiles.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())

        self.retranslateUi(bpui)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(bpui)

    def retranslateUi(self, bpui):
        bpui.setWindowTitle(_translate("bpui", "brainpipe - classification", None))
        self.groupBox_3.setTitle(_translate("bpui", "Files", None))
        self.loadFile1.setText(_translate("bpui", "File 1", None))
        self.loadFile2.setText(_translate("bpui", "File 2", None))
        self.groupBox_6.setTitle(_translate("bpui", "Summarize", None))
        self.groupBox_7.setTitle(_translate("bpui", "File 1", None))
        self.label_9.setText(_translate("bpui", "Data 1:", None))
        self.label_7.setText(_translate("bpui", "Data 1 shape :", None))
        self.groupBox_8.setTitle(_translate("bpui", "File 2", None))
        self.label_12.setText(_translate("bpui", "Data 2:", None))
        self.label_8.setText(_translate("bpui", "Data 2 shape :", None))
        self.resetData.setText(_translate("bpui", "Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabData), _translate("bpui", "Load", None))
        self.groupBox.setTitle(_translate("bpui", "Frequency", None))
        self.label.setText(_translate("bpui", "Frequency", None))
        self.clfGrp.setTitle(_translate("bpui", "Classification", None))
        self.groupBox_4.setTitle(_translate("bpui", "Classifier", None))
        self.label_2.setText(_translate("bpui", "Classifier", None))
        self.SFclf.setItemText(0, _translate("bpui", "lda", None))
        self.SFclf.setItemText(1, _translate("bpui", "svm", None))
        self.SFclf.setItemText(2, _translate("bpui", "knn", None))
        self.SFclf.setItemText(3, _translate("bpui", "nb", None))
        self.SFclf.setItemText(4, _translate("bpui", "rf", None))
        self.label_5.setText(_translate("bpui", "n_knn", None))
        self.label_4.setText(_translate("bpui", "Kernel", None))
        self.svmRBF.setText(_translate("bpui", "RBF", None))
        self.svmLin.setText(_translate("bpui", "Linear", None))
        self.label_6.setText(_translate("bpui", "n_tree", None))
        self.groupBox_5.setTitle(_translate("bpui", "Cross-validation", None))
        self.label_3.setText(_translate("bpui", "Cross-validation", None))
        self.cvType.setItemText(0, _translate("bpui", "kfold", None))
        self.cvType.setItemText(1, _translate("bpui", "skfold", None))
        self.cvType.setItemText(2, _translate("bpui", "ss", None))
        self.cvType.setItemText(3, _translate("bpui", "sss", None))
        self.label_26.setText(_translate("bpui", "N folds", None))
        self.label_25.setText(_translate("bpui", "Repetitions", None))
        self.runSF.setText(_translate("bpui", "Classify", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSF), _translate("bpui", "Classification", None))
        self.groupBox_9.setTitle(_translate("bpui", "Plot type", None))
        self.barBut.setText(_translate("bpui", "Bar plot", None))
        self.topoBut.setText(_translate("bpui", "Topo plot", None))
        self.groupBox_2.setTitle(_translate("bpui", "Filter", None))
        self.label_27.setText(_translate("bpui", "Display only features with a DA upper to", None))
        self.groupBox_10.setTitle(_translate("bpui", "Plot control", None))
        self.label_10.setText(_translate("bpui", "vmin", None))
        self.label_11.setText(_translate("bpui", "vmax", None))
        self.label_13.setText(_translate("bpui", "Colormap", None))
        self.updatePlot.setText(_translate("bpui", "Update plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("bpui", "Plot", None))
        self.userMsg.setText(_translate("bpui", "TextLabel", None))
        self.menuFiles.setTitle(_translate("bpui", "Files", None))
        self.menuMode.setTitle(_translate("bpui", "Mode", None))
        self.actionAdvanced.setText(_translate("bpui", "Advanced", None))

