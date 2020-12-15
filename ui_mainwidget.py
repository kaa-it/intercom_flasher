# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(800, 600)
        MainWidget.setMinimumSize(QSize(800, 600))
        self.gridLayout = QGridLayout(MainWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(MainWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.refreshButton = QPushButton(MainWidget)
        self.refreshButton.setObjectName(u"refreshButton")

        self.horizontalLayout.addWidget(self.refreshButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.devicesView = QTableView(MainWidget)
        self.devicesView.setObjectName(u"devicesView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.devicesView.sizePolicy().hasHeightForWidth())
        self.devicesView.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.devicesView)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Intercom Flasher", None))
        self.label.setText(QCoreApplication.translate("MainWidget", u"\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWidget", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
    # retranslateUi

