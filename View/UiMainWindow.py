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
        self.addrDockWidget = self.getAddrDockWidget(mw)
        self.subDockWidget = self.getSubDockWidget(mw)
        self.refDockWidget = self.getRefDockWidget(mw)
        self.posDockWidget = self.getPositionsWidget(mw)
        self.chainDockWidget = self.getChainDockWidget(mw)
        self.evDockWidget = self.getEvDockWidget(mw)
        self.logDockWidget_2 = self.getLogDockWidget_2(mw)
        self.graphDockWidget = self.getGraphDockWidget(mw)

        mw.addDockWidget(Qt.DockWidgetArea(4), self.addrDockWidget)
        mw.addDockWidget(Qt.DockWidgetArea(2), self.subDockWidget)
        mw.addDockWidget(Qt.DockWidgetArea(2), self.refDockWidget)
        mw.addDockWidget(Qt.DockWidgetArea(2), self.posDockWidget)
        mw.addDockWidget(Qt.DockWidgetArea(2), self.chainDockWidget)
        mw.addDockWidget(Qt.DockWidgetArea(2), self.evDockWidget)
        mw.addDockWidget(Qt.DockWidgetArea(8), self.logDockWidget_2)
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

    def getOptionChainDockWidget(self,mw):
        pass

    def getAccountDetailsDockWidget(self,mw):
        pass

    def getGraphDockWidget(self,mw):
        ret = QDockWidget(mw)
        ret.setObjectName("graphDockWidget")
        self.dockWidgetContents_6 = QWidget()
        self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
        self.gridLayout_7 = QGridLayout(self.dockWidgetContents_6)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.graphLayout = QVBoxLayout()
        self.graphLayout.setSpacing(6)
        self.graphLayout.setObjectName("graphLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.labelCandleWidth = QLabel("Candle Width")
        self.labelCandleWidth.setObjectName("labelNumberOfPoints")
        self.horizontalLayout.addWidget(self.labelCandleWidth)
        self.candleWidthSelectorCombo = self.getCandleWidthSelectCbx()
        self.candleWidthSelectorCombo.currentIndexChanged.connect(self.changeCandleWidth)
        self.horizontalLayout.addWidget(self.candleWidthSelectorCombo)

        self.labelNumberOfPoints = QLabel(self.dockWidgetContents_6)
        self.labelNumberOfPoints.setObjectName("labelNumberOfPoints")
        self.horizontalLayout.addWidget(self.labelNumberOfPoints)
        self.spinBoxNumberOfPoints = QSpinBox(self.dockWidgetContents_6)
        self.spinBoxNumberOfPoints.setMinimum(10)
        self.spinBoxNumberOfPoints.setMaximum(100)
        self.spinBoxNumberOfPoints.setProperty("value", 30)
        self.spinBoxNumberOfPoints.setObjectName("spinBoxNumberOfPoints")
        self.horizontalLayout.addWidget(self.spinBoxNumberOfPoints)
        self.labelIntervall = QLabel(self.dockWidgetContents_6)
        self.labelIntervall.setObjectName("labelIntervall")
        self.horizontalLayout.addWidget(self.labelIntervall)
        self.spinBoxIntervall = QSpinBox(self.dockWidgetContents_6)
        self.spinBoxIntervall.setMinimum(1)
        self.spinBoxIntervall.setMaximum(3600)
        self.spinBoxIntervall.setProperty("value", 5)
        self.spinBoxIntervall.setObjectName("spinBoxIntervall")
        self.horizontalLayout.addWidget(self.spinBoxIntervall)
        self.buttonApply = QPushButton(self.dockWidgetContents_6)
        self.buttonApply.setObjectName("buttonApply")
        self.horizontalLayout.addWidget(self.buttonApply)
        self.graphLayout.addLayout(self.horizontalLayout)
        self.gridLayout_7.addLayout(self.graphLayout, 0, 0, 1, 1)
        self.graphLayout.addWidget(self.positionViewer)

        ret.setWidget(self.dockWidgetContents_6)

        return ret

    def getLogDockWidget_2(self,mw):
        ret = QDockWidget(mw)
        ret.setObjectName("logDockWidget_2")
        self.dockWidgetContents_7 = QWidget()
        self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")
        self.gridLayout_6 = QGridLayout(self.dockWidgetContents_7)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        #self.gridLayout_6.setSpacing(20)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.logTextEdit = QTextEdit(self.dockWidgetContents_7)
        self.logTextEdit.setObjectName("logTextEdit")
        self.gridLayout_6.addWidget(self.logTextEdit, 0, 0, 1, 1)
        ret.setWidget(self.dockWidgetContents_7)
        return ret
        # MainWindow.addDockWidget(Qt.DockWidgetArea(8), ret)

    def getEvDockWidget(self,mw):
        ret = QDockWidget(mw)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ret.sizePolicy().hasHeightForWidth())
        ret.setSizePolicy(sizePolicy)
        ret.setObjectName("evDockWidget")
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.gridLayout_5 = QGridLayout(self.dockWidgetContents_5)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        # self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.evView = QListView(self.dockWidgetContents_5)
        self.evView.setAcceptDrops(True)
        self.evView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.evView.setDragDropMode(QAbstractItemView.DropOnly)
        self.evView.setObjectName("evView")
        self.gridLayout_5.addWidget(self.evView, 0, 0, 1, 1)
        ret.setWidget(self.dockWidgetContents_5)
        return ret

    def getAddrDockWidget(self,mw):
        ret = QDockWidget(mw)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ret.sizePolicy().hasHeightForWidth())
        ret.setSizePolicy(sizePolicy)
        ret.setFeatures(QDockWidget.NoDockWidgetFeatures)
        ret.setAllowedAreas(Qt.TopDockWidgetArea)
        ret.setObjectName("addrDockWidget")
        self.dockWidgetContents_2 = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_2.setSizePolicy(sizePolicy)
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.gridLayout = QGridLayout(self.dockWidgetContents_2)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.connectButton = QPushButton(self.dockWidgetContents_2)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 1, 4, 1, 1)
        self.disconnectButton = QPushButton(self.dockWidgetContents_2)
        self.disconnectButton.setObjectName("disconnectButton")
        self.gridLayout.addWidget(self.disconnectButton, 1, 5, 1, 1)
        self.addrComboBox = QComboBox(self.dockWidgetContents_2)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addrComboBox.sizePolicy().hasHeightForWidth())
        self.addrComboBox.setSizePolicy(sizePolicy)
        self.addrComboBox.setEditable(True)
        self.addrComboBox.setInsertPolicy(QComboBox.InsertAtTop)
        self.addrComboBox.setObjectName("addrComboBox")
        self.gridLayout.addWidget(self.addrComboBox, 1, 2, 1, 1)
        self.connectOptionButton = QPushButton(self.dockWidgetContents_2)
        self.connectOptionButton.setObjectName("connectOptionButton")
        self.gridLayout.addWidget(self.connectOptionButton, 1, 3, 1, 1)
        ret.setWidget(self.dockWidgetContents_2)
        return ret

    def getSubDockWidget(self, mw):
        ret = QDockWidget(mw)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ret.sizePolicy().hasHeightForWidth())
        ret.setSizePolicy(sizePolicy)
        ret.setObjectName("subDockWidget")
        self.dockWidgetContents_3 = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_3.setSizePolicy(sizePolicy)
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_3 = QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.subView = QTableView(self.dockWidgetContents_3)
        self.subView.setAcceptDrops(True)
        self.subView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.subView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.subView.setDragDropOverwriteMode(False)
        self.subView.setDragDropMode(QAbstractItemView.DropOnly)
        self.subView.setObjectName("subView")
        self.gridLayout_3.addWidget(self.subView, 0, 0, 1, 1)
        ret.setWidget(self.dockWidgetContents_3)
        return ret

    def getRefDockWidget(self, mw):
        ret = QDockWidget(mw)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ret.sizePolicy().hasHeightForWidth())
        ret.setSizePolicy(sizePolicy)
        ret.setObjectName("refDockWidget")
        self.dockWidgetContents_4 = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_4.setSizePolicy(sizePolicy)
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.refView = QTableView(self.dockWidgetContents_4)
        self.refView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.refView.setObjectName("refView")
        self.verticalLayout_2.addWidget(self.refView)
        ret.setWidget(self.dockWidgetContents_4)
        return ret

    def getPositionsWidget(self, mw):
        ret = QDockWidget(mw)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ret.sizePolicy().hasHeightForWidth())
        ret.setSizePolicy(sizePolicy)
        ret.setObjectName("posDockWidget")
        self.dockWidgetContents_4 = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_4.setSizePolicy(sizePolicy)
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.refView = QTableView(self.dockWidgetContents_4)
        self.refView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.refView.setObjectName("refView")
        self.verticalLayout_2.addWidget(self.refView)
        ret.setWidget(self.dockWidgetContents_4)
        return ret


    def getChainDockWidget(self, mw):
        ret = QDockWidget(mw)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ret.sizePolicy().hasHeightForWidth())
        ret.setSizePolicy(sizePolicy)
        ret.setObjectName("chainDockWidget")
        self.dockWidgetContents_4 = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_4.setSizePolicy(sizePolicy)
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.refView = QTableView(self.dockWidgetContents_4)
        self.refView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.refView.setObjectName("chainView")
        self.verticalLayout_2.addWidget(self.refView)
        ret.setWidget(self.dockWidgetContents_4)
        return ret

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
        mw.setWindowTitle(_translate("MainWindow", "FreeOpcUa Client"))
        self.menuOPC_UA_Client.setTitle(_translate("MainWindow", "Act&ions"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect"))
        self.connectOptionButton.setText(_translate("MainWindow", "Connect options"))
        self.subDockWidget.setWindowTitle(_translate("MainWindow", "O&verview"))
        self.refDockWidget.setWindowTitle(_translate("MainWindow", "&Account Details"))
        self.posDockWidget.setWindowTitle(_translate("MainWindow", "&My Positions"))
        self.chainDockWidget.setWindowTitle(_translate("MainWindow", "&Option Chain"))
        self.evDockWidget.setWindowTitle(_translate("MainWindow", "&Obsolete"))
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

