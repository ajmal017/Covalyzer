# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uaclient/mainwindow_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import Misc.const
from Misc.globals import globvars
from View.PositionViewer import PositionViewer
from View.DockWidgets.Graph import  getGraphDockWidget
from View.DockWidgets.Log import  getLogDockWidget
from View.DockWidgets.Addr import  getAddrDockWidget
from View.DockWidgets.Sub import  getSubDockWidget
from View.DockWidgets.Ref import  getRefDockWidget
from View.DockWidgets.Positions import  getPositionsWidget
from View.DockWidgets.Chain import  getChainDockWidget

class UiMainWindow(object):

    def getCandleWidthSelectCbx(self):
        ret = QComboBox()
        ret.addItem("1 min")
        ret.addItem("5 min")
        ret.addItem("60 min")
        return ret

    def changeCandleWidth(self):
        curCandleWidthText = self.candleWidthSelectorCombo.currentText()
        globvars.logger.info("Candlewidth changed to %s", curCandleWidthText)
        if curCandleWidthText == "1 min":
            globvars.controller.model.candleWidth = Misc.const.CANDLEWIDTH1
        elif curCandleWidthText == "5 min":
            globvars.controller.model.candleWidth = Misc.const.CANDLEWIDTH5
        elif curCandleWidthText == "60 min":
            globvars.controller.model.candleWidth = Misc.const.CANDLEWIDTH60

    def dockSetup(self,mw):
        self.addrDockWidget  = getAddrDockWidget(self,mw)
        self.subDockWidget   = getSubDockWidget(self,mw)
        self.refDockWidget   = getRefDockWidget(self,mw)
        self.posDockWidget   = getPositionsWidget(self,mw)
        self.chainDockWidget = getChainDockWidget(self,mw)
        self.logDockWidget   = getLogDockWidget(self,mw)
        self.graphDockWidget = getGraphDockWidget(self,mw)

        mw.addDockWidget(Qt.DockWidgetArea(4), self.addrDockWidget)
        mw.addDockWidget(Qt.DockWidgetArea(2), self.subDockWidget)
        mw.addDockWidget(Qt.DockWidgetArea(2), self.refDockWidget)
        mw.addDockWidget(Qt.DockWidgetArea(2), self.posDockWidget)
        mw.addDockWidget(Qt.DockWidgetArea(2), self.chainDockWidget)
        mw.addDockWidget(Qt.DockWidgetArea(8), self.logDockWidget)
        mw.addDockWidget(Qt.DockWidgetArea(2), self.graphDockWidget)

    def actionSetup(self, mw):
        self.actionConnect = QAction(mw)
        self.actionDisconnect = QAction(mw)
        self.actionSubscribeDataChange = QAction(mw)
        self.actionUnsubscribeDataChange = QAction(mw)
        self.actionSubscribeEvent = QAction(mw)
        self.actionUnsubscribeEvents = QAction(mw)
        self.actionCopyPath = QAction(mw)
        self.actionCopyNodeId = QAction(mw)
        self.actionAddToGraph = QAction(mw)
        self.actionRemoveFromGraph = QAction(mw)
        self.actionCall = QAction(mw)

        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionSubscribeDataChange.setObjectName("actionSubscribeDataChange")
        self.actionUnsubscribeDataChange.setObjectName("actionUnsubscribeDataChange")
        self.actionSubscribeEvent.setObjectName("actionSubscribeEvent")
        self.actionUnsubscribeEvents.setObjectName("actionUnsubscribeEvents")
        self.actionCopyPath.setObjectName("actionCopyPath")
        self.actionCopyNodeId.setObjectName("actionCopyNodeId")
        self.actionAddToGraph.setObjectName("actionAddToGraph")
        self.actionRemoveFromGraph.setObjectName("actionRemoveFromGraph")
        self.actionCall.setObjectName("actionCall")

        self.menuOPC_UA_Client.addAction(self.actionConnect)
        self.menuOPC_UA_Client.addAction(self.actionDisconnect)
        self.menuOPC_UA_Client.addAction(self.actionCopyPath)
        self.menuOPC_UA_Client.addAction(self.actionCopyNodeId)
        self.menuOPC_UA_Client.addAction(self.actionSubscribeDataChange)
        self.menuOPC_UA_Client.addAction(self.actionUnsubscribeDataChange)
        self.menuOPC_UA_Client.addAction(self.actionSubscribeEvent)
        self.menuOPC_UA_Client.addAction(self.actionUnsubscribeEvents)
        self.menuBar.addAction(self.menuOPC_UA_Client.menuAction())

    def setupUi(self, mw, view):
        mw.setObjectName("MainWindow")
        mw.resize(922, 879)

        self.centralWidget = QWidget(mw)

        self.positionViewer = PositionViewer()
        view.setPositionViewer(self.positionViewer)

        self.gridLayout_2 = QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)

        self.splitter = QSplitter(self.centralWidget)

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())

        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)

        self.treeView = QWidget(self.splitter)
        vl = QVBoxLayout()
        vl.addWidget(view)
        self.treeView.setLayout(vl)

        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)

        mw.setCentralWidget(self.centralWidget)

        self.menuBar = QMenuBar(mw)
        self.menuBar.setGeometry(QRect(0, 0, 922, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuOPC_UA_Client = QMenu(self.menuBar)
        self.menuOPC_UA_Client.setObjectName("menuOPC_UA_Client")
        mw.setMenuBar(self.menuBar)

        self.statusBar = QStatusBar(mw)
        self.statusBar.setObjectName("statusBar")
        mw.setStatusBar(self.statusBar)

        self.dockSetup(mw)
        self.actionSetup(mw)

        self.retranslateUi(mw)
        QMetaObject.connectSlotsByName(mw)

    def retranslateUi(self, mw):
        _translate = QCoreApplication.translate
        mw.setWindowTitle(_translate("MainWindow", "Covalyzer Client"))
        self.menuOPC_UA_Client.setTitle(_translate("MainWindow", "Act&ions"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect"))
        self.connectOptionButton.setText(_translate("MainWindow", "Connect options"))
        self.subDockWidget.setWindowTitle(_translate("MainWindow", "O&verview"))
        self.refDockWidget.setWindowTitle(_translate("MainWindow", "&Account Details"))
        self.posDockWidget.setWindowTitle(_translate("MainWindow", "&My Positions"))
        self.chainDockWidget.setWindowTitle(_translate("MainWindow", "&Option Chain"))
        self.graphDockWidget.setWindowTitle(_translate("MainWindow", "&Charts"))
        self.labelNumberOfPoints.setText(_translate("MainWindow", "Number of Points"))
        self.labelIntervall.setText(_translate("MainWindow", "Intervall [s]"))
        self.buttonApply.setText(_translate("MainWindow", "Apply"))
        self.actionConnect.setText(_translate("MainWindow", "&Connect"))
        self.actionDisconnect.setText(_translate("MainWindow", "&Disconnect"))
        self.actionDisconnect.setToolTip(_translate("MainWindow", "Disconnect from server"))
        self.actionSubscribeDataChange.setText(_translate("MainWindow", "&Subscribe to data change"))
        self.actionSubscribeDataChange.setToolTip(_translate("MainWindow", "Subscribe to data change from selected node"))
        self.actionUnsubscribeDataChange.setText(_translate("MainWindow", "&Unsubscribe to DataChange"))
        self.actionUnsubscribeDataChange.setToolTip(_translate("MainWindow", "Unsubscribe to DataChange for current node"))
        self.actionSubscribeEvent.setText(_translate("MainWindow", "Subscribe to &events"))
        self.actionSubscribeEvent.setToolTip(_translate("MainWindow", "Subscribe to events from selected node"))
        self.actionUnsubscribeEvents.setText(_translate("MainWindow", "U&nsubscribe to Events"))
        self.actionUnsubscribeEvents.setToolTip(_translate("MainWindow", "Unsubscribe to Events from current node"))
        self.actionCopyPath.setText(_translate("MainWindow", "Copy &Path"))
        self.actionCopyPath.setToolTip(_translate("MainWindow", "Copy path to node to clipboard"))
        self.actionCopyNodeId.setText(_translate("MainWindow", "C&opy NodeId"))
        self.actionCopyNodeId.setToolTip(_translate("MainWindow", "Copy NodeId to clipboard"))
        self.actionAddToGraph.setText(_translate("MainWindow", "Add to &Graph"))
        self.actionAddToGraph.setToolTip(_translate("MainWindow", "Add this node to the graph"))
        self.actionAddToGraph.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionRemoveFromGraph.setText(_translate("MainWindow", "Remove from Graph"))
        self.actionRemoveFromGraph.setToolTip(_translate("MainWindow", "Remove this node from the graph"))
        self.actionRemoveFromGraph.setShortcut(_translate("MainWindow", "Ctrl+Shift+G"))
        self.actionCall.setText(_translate("MainWindow", "Call"))
        self.actionCall.setToolTip(_translate("MainWindow", "Call Ua Method"))

