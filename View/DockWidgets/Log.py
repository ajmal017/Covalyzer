from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def getLogDockWidget(self, mw):
    ret = QDockWidget(mw)
    ret.setObjectName("logDockWidget_2")
    self.dockWidgetContents_7 = QWidget()
    self.dockWidgetContents_7.setObjectName("dockWidgetContents_7")
    self.gridLayout_6 = QGridLayout(self.dockWidgetContents_7)
    self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
    # self.gridLayout_6.setSpacing(20)
    self.gridLayout_6.setObjectName("gridLayout_6")
    self.logTextEdit = QTextEdit(self.dockWidgetContents_7)
    self.logTextEdit.setObjectName("logTextEdit")
    self.gridLayout_6.addWidget(self.logTextEdit, 0, 0, 1, 1)
    ret.setWidget(self.dockWidgetContents_7)
    return ret
