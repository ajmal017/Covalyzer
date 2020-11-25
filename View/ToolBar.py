from datetime import datetime


from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction, QMenu, QLabel, QColorDialog, QFontDialog, QComboBox, QToolButton
from PyQt5.QtGui import QIcon

from Misc.globals import globvars
import Misc.const
from Color import PALETTES_NAMED

class ToolBar(QToolBar):
    def __init__(self, w, c, p, parent = None):
        super(ToolBar, self).__init__(parent)
        self.setObjectName("toolbar")
        self.cwidget        = w
        self.controller     = c
        self.positionViewer = p

        self.actionSelectFont               = self.myAddAction('View/icons/Digital - Zero.png', "Select Font"                 , self.openFontDialog)
        self.actionShowPositionViewer       = self.myAddAction('View/icons/Torch.png', "Show Position"                        , self.showPositionViewer)
        self.actionResizeColumnWidth        = self.myAddAction("View/icons/I don't know.png", "resize columnwidth in table"   , self.doActionResizeColumns)
        self.actionConnectToBrkApi          = self.myAddAction('View/icons/Link - 01.png', "Connect toIBKR"                   , self.cmw_actionConnectToBrkApi)
        self.actionDisconnectFromBrkApi     = self.myAddAction('View/icons/Link - 02.png', "Disconnect from IBKR"             , self.cmw_actionDisconnectFromBrkApi)

        # toolbutton which stays in presses-state
        self.toolButton = QToolButton(self)
        self.toolButton.setIcon(QIcon('View/icons/Signal.png'))
        self.toolButton.setCheckable(True)
        self.toolButton.toggled.connect(self.updateHistory)

        self.colorSelectorCombo                     = self.getColorCbx()
        self.watchlistSelectorCombo                 = self.getWatchlistCbx()
        self.downloadSelectorCombo                  = self.getDwnLoadSelctCbx()
        self.portSelectorCombo                      = self.getPortSelectlistCbx()
        self.chartSelectorCombo                     = self.getChartSelectlistCbx()
        self.filterSelectorCombo                    = self.getFilterSelectCbx()
        self.candleWidthSelectorCombo               = self.getCandleWidthSelectCbx()

        self.downloadSelectorCombo.currentIndexChanged.connect          (self.changeDownloadMode)
        self.portSelectorCombo.currentIndexChanged.connect          (self.changeBrokerPort)
        self.filterSelectorCombo.currentIndexChanged.connect        (self.changeFilter)
        self.chartSelectorCombo.currentIndexChanged.connect        (self.changeChart)
        self.candleWidthSelectorCombo.currentIndexChanged.connect   (self.changeCandleWidth)

        self.downloadSelectorCombo.setCurrentIndex(2)
        self.filterSelectorCombo.setCurrentIndex(1)
        self.candleWidthSelectorCombo.setCurrentIndex(2)

        self.addWidget(self.toolButton)
        self.addSeparator()
        self.addWidget(self.colorSelectorCombo)
        self.addSeparator()
        self.addWidget(self.watchlistSelectorCombo)
        self.addSeparator()
        self.addWidget(self.downloadSelectorCombo)
        self.addWidget(self.portSelectorCombo)
        self.addWidget(self.chartSelectorCombo)
        self.addWidget(self.filterSelectorCombo)
        self.addWidget(self.candleWidthSelectorCombo)

    def myAddAction(self, icon, tttext, callback):
        action = QAction(QIcon(icon), 'Flee the Scene', self)
        action.setToolTip(tttext)
        action.triggered.connect(callback)
        self.addAction(action)
        return action

    def getColorCbx(self):
        ret = QComboBox()
        for k in PALETTES_NAMED:
            ret.addItem(k)
        ret.setCurrentIndex(1)
        ret.currentIndexChanged.connect(self.changeColorPalette)
        return ret

    def getWatchlistCbx(self):
        ret = QComboBox()
        ret.addItem("Current Portfolio")
        ret.addItem("BCI Candidates")
        ret.addItem("Closed Positions")
        return ret

    def getCandleWidthSelectCbx(self):
        ret = QComboBox()
        ret.addItem("1 min")
        ret.addItem("5 min")
        ret.addItem("60 min")
        return ret

    def getFilterSelectCbx(self):
        ret = QComboBox()
        ret.addItem("include closed positions")
        ret.addItem("excluse closed positions")
        return ret

    def getChartSelectlistCbx(self):
        ret = QComboBox()
        ret.addItem("TimeValue")
        ret.addItem("OptionPrice")
        return ret

    def getDwnLoadSelctCbx(self):
        ret = QComboBox()
        ret.addItem("only stocks")
        ret.addItem("only options")
        ret.addItem("both")
        return ret

    def getPortSelectlistCbx(self):
        ret = QComboBox()
        ret.addItem("TWS REAL  7495")
        ret.addItem("TWS PAPER 7497")
        ret.addItem("GTW REAL  4001")
        ret.addItem("GTW PAPER 4002")
        if (Misc.const.IBPORT == 7495):
            ret.setCurrentIndex(0)
        elif (Misc.const.IBPORT == 7497):
            ret.setCurrentIndex(1)
        elif (Misc.const.IBPORT == 4001):
            ret.setCurrentIndex(2)
        elif (Misc.const.IBPORT == 4002):
            ret.setCurrentIndex(3)
        return ret

    def doActionResizeColumns(self):
        self.cwidget.table_view.resizeColumnsToContents();

    def showPositionViewer(self):
        cc = self.cwidget.getSelectedRow()
        if cc != None:
            a = self.controller.getStockData(cc)
            t = self.chartSelectorCombo.currentText()
            self.positionViewer.updateMplChart(cc, a, t)

    def changeColorPalette(self):
        globvars.colors = PALETTES_NAMED[self.colorSelectorCombo.currentText()]

    def changeCandleWidth(self):
        curCandleWidthText = self.candleWidthSelectorCombo.currentText()
        if curCandleWidthText == "1 min":
            self.controller.model.candleWidth = Misc.const.CANDLEWIDTH1
        elif curCandleWidthText == "5 min":
            self.controller.model.candleWidth = Misc.const.CANDLEWIDTH5
        elif curCandleWidthText == "60 min":
            self.controller.model.candleWidth = Misc.const.CANDLEWIDTH60

    def changeChart(self):
        self.cwidget.setChartType(self.chartSelectorCombo.currentText())

        cc = self.cwidget.proxy_model.sourceModel().bwl[str(((self.cwidget.r * 2) + Misc.const.INITIALTTICKERID))]
        a = self.cwidget.controller.getStockData(cc)
        self.cwidget.positionViewer.updateMplChart(cc, a, self.cwidget.charttype)

    def changeFilter(self):
        curtext = self.filterSelectorCombo.currentText()
        if curtext == "include closed positions":
            self.controller.model.includeZeroPositions = True
        else:
            self.controller.model.includeZeroPositions = False

    def changeCandleWidth(self):
        curtext = self.candleWidthSelectorCombo.currentText()
        if curtext == "1 min":
            self.controller.model.candleWidth = Misc.const.CANDLEWIDTH1
        elif curtext == "5 min":
            self.controller.model.candleWidth = Misc.const.CANDLEWIDTH5
        elif curtext == "60 min":
            self.controller.model.candleWidth = Misc.const.CANDLEWIDTH60
        else:
            self.controller.model.candleWidth = Misc.const.CANDLEWIDTH5

        cc = self.cwidget.proxy_model.sourceModel().bwl[str(((self.cwidget.r * 2) + Misc.const.INITIALTTICKERID))]
        a = self.cwidget.controller.getStockData(cc)
        self.cwidget.positionViewer.updateMplChart(cc, a, self.cwidget.charttype)

    def changeDownloadMode(self):
        curtext = self.downloadSelectorCombo.currentText()
        if curtext == "only stocks":
            self.controller.downloadSelector = Misc.const.STOCKSONLY
        elif curtext == "only options":
            self.controller.downloadSelector = Misc.const.OPTIONSONLY
        else:
            self.controller.downloadSelector = Misc.const.BOTH


    def changeBrokerPort(self):
        port = 4002
        if self.portSelectorCombo.currentText() == "TWS REAL  7495":
            port= 7495
        if self.portSelectorCombo.currentText() == "TWS PAPER 7497":
            port= 7497
        if self.portSelectorCombo.currentText() == "GTW REAL  4001":
            port= 4001
        if self.portSelectorCombo.currentText() == "GTW PAPER 4002":
            port= 4002
        self.controller.changeBrokerPort(port)

    def openFontDialog(self):
        font, ok = QFontDialog.getFont(self.cwidget.current_font)
        print(str(font))
        if ok:
            self.cwidget.changeFont(font)
        return font

    def updateHistory(self):
        self.controller.switchDownloadState()

    def cmw_actionConnectToBrkApi(self):
        self.actionConnectToBrkApi.setEnabled(False)
        self.actionDisconnectFromBrkApi.setEnabled(True)
        self.controller.connect()

    def cmw_actionDisconnectFromBrkApi(self):
        self.actionConnectToBrkApi.setEnabled(True)
        self.actionDisconnectFromBrkApi.setEnabled(False)
        self.controller.disconnect()
