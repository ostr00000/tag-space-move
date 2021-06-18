# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/duplicate_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DuplicateWidget(object):
    def setupUi(self, DuplicateWidget):
        DuplicateWidget.setObjectName("DuplicateWidget")
        DuplicateWidget.resize(520, 360)
        self.horizontalLayout = QtWidgets.QHBoxLayout(DuplicateWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(DuplicateWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.tableView = QtWidgets.QTableView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pathPlaceholder = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathPlaceholder.sizePolicy().hasHeightForWidth())
        self.pathPlaceholder.setSizePolicy(sizePolicy)
        self.pathPlaceholder.setAlignment(QtCore.Qt.AlignCenter)
        self.pathPlaceholder.setObjectName("pathPlaceholder")
        self.verticalLayout.addWidget(self.pathPlaceholder)
        self.findDuplicatesButton = QtWidgets.QPushButton(self.widget)
        self.findDuplicatesButton.setObjectName("findDuplicatesButton")
        self.verticalLayout.addWidget(self.findDuplicatesButton)
        self.selectCandidatesButton = QtWidgets.QPushButton(self.widget)
        self.selectCandidatesButton.setObjectName("selectCandidatesButton")
        self.verticalLayout.addWidget(self.selectCandidatesButton)
        self.removeSelectedButton = QtWidgets.QPushButton(self.widget)
        self.removeSelectedButton.setObjectName("removeSelectedButton")
        self.verticalLayout.addWidget(self.removeSelectedButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(DuplicateWidget)
        QtCore.QMetaObject.connectSlotsByName(DuplicateWidget)

    def retranslateUi(self, DuplicateWidget):
        _translate = QtCore.QCoreApplication.translate
        DuplicateWidget.setWindowTitle(_translate("DuplicateWidget", "Remove duplicated files"))
        self.findDuplicatesButton.setText(_translate("DuplicateWidget", "Find duplicates"))
        self.selectCandidatesButton.setText(_translate("DuplicateWidget", "Select candidates"))
        self.removeSelectedButton.setText(_translate("DuplicateWidget", "Remove selected"))
