from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

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

