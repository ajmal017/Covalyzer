#! /usr/bin/env python3

from PyQt5.QtCore import pyqtSignal, QTimer, Qt, QObject, QSettings, QItemSelection, QMimeData, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QAbstractItemView, QMenu, QAction

from View.UiMainWindow import UiMainWindow
from View.ConnectionDialog import ConnectionDialog
from View.ToolBar import ToolBar
from Misc.globals import globvars

from uawidgets.utils import trycatchslot
from uawidgets.call_method_dialog import CallMethodDialog

class MainWindow(QMainWindow):

    def __init__(self, v):
        QMainWindow.__init__(self)
        self.ui = UiMainWindow()
        self.ui.setupUi(self,v)

        self.addToolBar(ToolBar(v, globvars.controller, self.ui.positionViewer))

        w = QWidget()
        self.ui.addrDockWidget.setTitleBarWidget(w)
        # tabify some docks
        self.tabifyDockWidget(self.ui.subDockWidget, self.ui.refDockWidget)
        self.tabifyDockWidget(self.ui.refDockWidget, self.ui.graphDockWidget)

        # setup QSettings for application and get a settings object
        QCoreApplication.setOrganizationName("Mitec")
        QCoreApplication.setApplicationName("Covalyzer")
        self.settings = QSettings("./Covalyzer.ini", QSettings.IniFormat)

        self._address_list = self.settings.value("address_list", ["localhost:7", "opc.tcp://localhost:53530/OPCUA/SimulationServer/"])
        print("ADR", self._address_list)
        self._address_list_max_count = int(self.settings.value("address_list_max_count", 10))

        # init widgets
        for addr in self._address_list:
            self.ui.addrComboBox.insertItem(100, addr)

        self.resize(int(self.settings.value("main_window_width", 800)), int(self.settings.value("main_window_height", 600)))
        data = self.settings.value("main_window_state", None)
        if data:
            self.restoreState(data)

        self.ui.connectButton.clicked.connect(self.connect)
        self.ui.disconnectButton.clicked.connect(self.disconnect)
        self.ui.actionConnect.triggered.connect(self.connect)
        self.ui.actionDisconnect.triggered.connect(self.disconnect)
        self.ui.connectOptionButton.clicked.connect(self.show_connection_dialog)

    def show_connection_dialog(self):
        dia = ConnectionDialog(self, self.ui.addrComboBox.currentText())
        dia.exec_()

    @trycatchslot
    def show_refs(self, selection):
        if isinstance(selection, QItemSelection):
            if not selection.indexes(): # no selection
                return

        node = self.get_current_node()
        if node:
            self.refs_ui.show_refs(node)
    
    @trycatchslot
    def show_attrs(self, selection):
        if isinstance(selection, QItemSelection):
            if not selection.indexes(): # no selection
                return

        node = self.get_current_node()
        if node:
            self.attrs_ui.show_attrs(node)

    @trycatchslot
    def connect(self):
        uri = self.ui.addrComboBox.currentText()
        try:
            globvars.controller.connect(host = "localhost", port = 7497, cltid=20)
            # self.uaclient.connect(uri)
        except Exception as ex:
            self.show_error(ex)
            raise

        self._update_address_list(uri)

    def show_error(self, msg):
        globvars.logger.warning("showing error: %s")
        self.ui.statusBar.show()
        self.ui.statusBar.setStyleSheet("QStatusBar { background-color : red; color : black; }")
        self.ui.statusBar.showMessage(str(msg))
        # QTimer.singleShot(1500, self.ui.statusBar.hide)

    def _update_address_list(self, uri):
        if uri == self._address_list[0]:
            return
        if uri in self._address_list:
            self._address_list.remove(uri)
        self._address_list.insert(0, uri)
        if len(self._address_list) > self._address_list_max_count:
            self._address_list.pop(-1)

    def disconnect(self):
        globvars.controller.disconnect()

    def closeEvent(self, event):
        # self.tree_ui.save_state()
        # self.refs_ui.save_state()
        self.settings.setValue("main_window_width", self.size().width())
        self.settings.setValue("main_window_height", self.size().height())
        self.settings.setValue("main_window_state", self.saveState())
        self.settings.setValue("address_list", self._address_list)
        self.disconnect()
        event.accept()

    def addAction(self, action):
        self._contextMenu.addAction(action)

    def call_method(self):
        node = self.get_current_node()
        dia = CallMethodDialog(self, self.uaclient.client, node)
        dia.show()
