from PyQt5.QtWidgets import *

def createWidgets(self):
    self.gridLayout_7 = QGridLayout(self.dockWidgetContents_6)
    self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
    self.gridLayout_7.setSpacing(6)
    self.gridLayout_7.setObjectName("gridLayout_7")

    self.labelCandleWidth = QLabel("Candle Width")
    self.labelCandleWidth.setObjectName("labelNumberOfPoints")

    self.candleWidthSelectorCombo = self.getCandleWidthSelectCbx()
    self.candleWidthSelectorCombo.currentIndexChanged.connect(self.changeCandleWidth)

    self.labelNumberOfPoints = QLabel(self.dockWidgetContents_6)
    self.labelNumberOfPoints.setObjectName("labelNumberOfPoints")

    self.spinBoxNumberOfPoints = QSpinBox(self.dockWidgetContents_6)
    self.spinBoxNumberOfPoints.setMinimum(10)
    self.spinBoxNumberOfPoints.setMaximum(100)
    self.spinBoxNumberOfPoints.setProperty("value", 30)
    self.spinBoxNumberOfPoints.setObjectName("spinBoxNumberOfPoints")

    self.spinBoxIntervall = QSpinBox(self.dockWidgetContents_6)
    self.spinBoxIntervall.setMinimum(1)
    self.spinBoxIntervall.setMaximum(3600)
    self.spinBoxIntervall.setProperty("value", 5)
    self.spinBoxIntervall.setObjectName("spinBoxIntervall")

    self.labelIntervall = QLabel(self.dockWidgetContents_6)
    self.labelIntervall.setObjectName("labelIntervall")

    self.buttonApply = QPushButton(self.dockWidgetContents_6)
    self.buttonApply.setObjectName("buttonApply")

#this is a pseudo partial class from UiMainWindow
def getGraphDockWidget(self, mw):
    ret = QDockWidget(mw)
    ret.setObjectName("graphDockWidget")
    self.dockWidgetContents_6 = QWidget()
    self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")

    createWidgets(self)

    self.graphLayout = QVBoxLayout()
    self.graphLayout.setSpacing(6)
    self.graphLayout.setObjectName("graphLayout")

    self.horizontalLayout = QHBoxLayout()
    self.horizontalLayout.setSpacing(6)
    self.horizontalLayout.setObjectName("horizontalLayout")

    self.horizontalLayout.addWidget(self.labelCandleWidth)
    self.horizontalLayout.addWidget(self.candleWidthSelectorCombo)
    self.horizontalLayout.addWidget(self.labelNumberOfPoints)
    self.horizontalLayout.addWidget(self.spinBoxNumberOfPoints)
    self.horizontalLayout.addWidget(self.labelIntervall)
    self.horizontalLayout.addWidget(self.spinBoxIntervall)
    self.horizontalLayout.addWidget(self.buttonApply)

    self.graphLayout.addLayout(self.horizontalLayout)
    self.gridLayout_7.addLayout(self.graphLayout, 0, 0, 1, 1)
    self.graphLayout.addWidget(self.positionViewer)

    ret.setWidget(self.dockWidgetContents_6)

    return ret

