import sys
import logging

from PyQt5.QtCore import pyqtSignal, QTimer, Qt, QObject, QSettings, QItemSelection, QMimeData, QCoreApplication
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QAbstractItemView, QMenu, QAction
from uawidgets.logger import QtHandler
from Model.CMTModel import CMTModel
from Controller.CMTController import Controller
from View.CMTWidget import CMTWidget
from View.MainWindow import MainWindow
from Misc.globals import globvars
from Model.resamplecsv import resample

def main():
    globvars.init_globvars()
    globvars.initMainLogger()

    globvars.logger = globvars.mainLogger

    model = CMTModel()
    globvars.controller = Controller(model)
    model.initData(globvars.controller)

    app = QApplication(sys.argv)
    view = CMTWidget(model, globvars.controller)
    client = MainWindow(view)

    qt_handler = QtHandler(client.ui.logTextEdit)
    qt_handler.setLevel(logging.INFO)
    qt_handler.setFormatter(globvars.loggingdata.formatter)
    globvars.mainLogger.addHandler(qt_handler)


    globvars.mainLogger.info("Covalyzer Startup")
    globvars.mainLogger.info("Settings at %s", client.settings.fileName())

    client.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
