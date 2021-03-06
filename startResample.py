import sys
import logging
import argparse

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

if __name__ == "__main__":
    globvars.init_globvars()

    argp = argparse.ArgumentParser()
    argp.add_argument(
        "--symbol", type=str, default="", help="strike for options"
    )
    args = argp.parse_args()

    logfilename = "Resample.log"
    formatter = logging.Formatter(fmt='%(asctime)s.%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    mainLogger = logging.getLogger(__name__)
    mainLogger.setLevel(logging.DEBUG)
    file_Handler = logging.FileHandler(logfilename, mode='a')
    file_Handler.setLevel(logging.DEBUG)
    file_Handler.setFormatter(formatter)
    mainLogger.addHandler(file_Handler)

    globvars.logger = mainLogger

    if args.symbol:
        resample(False, args.symbol)

