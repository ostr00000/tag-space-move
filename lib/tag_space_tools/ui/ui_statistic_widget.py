# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/statistic_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StatisticWidget(object):
    def setupUi(self, StatisticWidget):
        StatisticWidget.setObjectName("StatisticWidget")
        StatisticWidget.resize(631, 441)
        self.verticalLayout = QtWidgets.QVBoxLayout(StatisticWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(StatisticWidget)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.libraryPlaceholder = QtWidgets.QPushButton(StatisticWidget)
        self.libraryPlaceholder.setObjectName("libraryPlaceholder")
        self.verticalLayout.addWidget(self.libraryPlaceholder)

        self.retranslateUi(StatisticWidget)
        QtCore.QMetaObject.connectSlotsByName(StatisticWidget)

    def retranslateUi(self, StatisticWidget):
        _translate = QtCore.QCoreApplication.translate
        StatisticWidget.setWindowTitle(_translate("StatisticWidget", "Statistics"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("StatisticWidget", "Tag name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("StatisticWidget", "Tag number"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("StatisticWidget", "Files"))
        self.libraryPlaceholder.setText(_translate("StatisticWidget", "Library placeholder"))
