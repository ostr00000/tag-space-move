# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/tag_sorter.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TagSorter(object):
    def setupUi(self, TagSorter):
        TagSorter.setObjectName("TagSorter")
        TagSorter.resize(527, 519)
        self.gridLayout_2 = QtWidgets.QGridLayout(TagSorter)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(TagSorter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.maxFilesPerLevelSpinBox = QtWidgets.QSpinBox(TagSorter)
        self.maxFilesPerLevelSpinBox.setMinimum(1)
        self.maxFilesPerLevelSpinBox.setMaximum(10000)
        self.maxFilesPerLevelSpinBox.setProperty("value", 20)
        self.maxFilesPerLevelSpinBox.setObjectName("maxFilesPerLevelSpinBox")
        self.verticalLayout.addWidget(self.maxFilesPerLevelSpinBox)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(TagSorter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.loadTagsButton = QtWidgets.QToolButton(TagSorter)
        icon = QtGui.QIcon.fromTheme("document-open")
        self.loadTagsButton.setIcon(icon)
        self.loadTagsButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.loadTagsButton.setObjectName("loadTagsButton")
        self.horizontalLayout.addWidget(self.loadTagsButton)
        self.saveButton = QtWidgets.QToolButton(TagSorter)
        icon = QtGui.QIcon.fromTheme("document-save-as")
        self.saveButton.setIcon(icon)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.removeTagButton = QtWidgets.QToolButton(TagSorter)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.removeTagButton.setIcon(icon)
        self.removeTagButton.setObjectName("removeTagButton")
        self.horizontalLayout.addWidget(self.removeTagButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(TagSorter)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 5, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(TagSorter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toLineEdit = QtWidgets.QLineEdit(TagSorter)
        self.toLineEdit.setReadOnly(True)
        self.toLineEdit.setObjectName("toLineEdit")
        self.horizontalLayout_3.addWidget(self.toLineEdit)
        self.toButton = QtWidgets.QToolButton(TagSorter)
        self.toButton.setObjectName("toButton")
        self.horizontalLayout_3.addWidget(self.toButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 2, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(TagSorter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fromLineEdit = QtWidgets.QLineEdit(TagSorter)
        self.fromLineEdit.setReadOnly(True)
        self.fromLineEdit.setObjectName("fromLineEdit")
        self.horizontalLayout_2.addWidget(self.fromLineEdit)
        self.fromButton = QtWidgets.QToolButton(TagSorter)
        self.fromButton.setObjectName("fromButton")
        self.horizontalLayout_2.addWidget(self.fromButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 294, QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 2, 1, 1)
        self.moveFilesButton = QtWidgets.QPushButton(TagSorter)
        self.moveFilesButton.setObjectName("moveFilesButton")
        self.gridLayout_2.addWidget(self.moveFilesButton, 3, 2, 1, 1)

        self.retranslateUi(TagSorter)
        QtCore.QMetaObject.connectSlotsByName(TagSorter)

    def retranslateUi(self, TagSorter):
        _translate = QtCore.QCoreApplication.translate
        TagSorter.setWindowTitle(_translate("TagSorter", "Form"))
        self.label_2.setText(_translate("TagSorter", "Max files per level:"))
        self.label.setText(_translate("TagSorter", "Tag order:"))
        self.loadTagsButton.setText(_translate("TagSorter", "Load tag library"))
        self.saveButton.setText(_translate("TagSorter", "..."))
        self.removeTagButton.setText(_translate("TagSorter", "Remove"))
        self.label_4.setText(_translate("TagSorter", "To folder:"))
        self.toButton.setText(_translate("TagSorter", "..."))
        self.label_3.setText(_translate("TagSorter", "From folder:"))
        self.fromButton.setText(_translate("TagSorter", "..."))
        self.moveFilesButton.setText(_translate("TagSorter", "Move files"))
