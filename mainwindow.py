# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Wed Jul 17 20:09:38 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(614, 331)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabwidget = QtGui.QTabWidget(self.centralwidget)
        self.tabwidget.setEnabled(True)
        self.tabwidget.setGeometry(QtCore.QRect(10, 10, 271, 231))
        self.tabwidget.setAutoFillBackground(True)
        self.tabwidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabwidget.setObjectName(_fromUtf8("tabwidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.combobox_regparams = QtGui.QComboBox(self.tab)
        self.combobox_regparams.setGeometry(QtCore.QRect(110, 10, 141, 22))
        self.combobox_regparams.setObjectName(_fromUtf8("combobox_regparams"))
        self.combobox_regparams.addItem(_fromUtf8(""))
        self.combobox_regparams.addItem(_fromUtf8(""))
        self.spinbox_wave_height = QtGui.QDoubleSpinBox(self.tab)
        self.spinbox_wave_height.setGeometry(QtCore.QRect(110, 50, 61, 22))
        self.spinbox_wave_height.setAccelerated(True)
        self.spinbox_wave_height.setDecimals(3)
        self.spinbox_wave_height.setMaximum(0.4)
        self.spinbox_wave_height.setSingleStep(0.001)
        self.spinbox_wave_height.setProperty("value", 0.1)
        self.spinbox_wave_height.setObjectName(_fromUtf8("spinbox_wave_height"))
        self.spinbox_wave_period = QtGui.QDoubleSpinBox(self.tab)
        self.spinbox_wave_period.setGeometry(QtCore.QRect(110, 80, 61, 22))
        self.spinbox_wave_period.setAccelerated(True)
        self.spinbox_wave_period.setDecimals(3)
        self.spinbox_wave_period.setMinimum(0.5)
        self.spinbox_wave_period.setMaximum(5.0)
        self.spinbox_wave_period.setSingleStep(0.001)
        self.spinbox_wave_period.setProperty("value", 1.0)
        self.spinbox_wave_period.setObjectName(_fromUtf8("spinbox_wave_period"))
        self.spinbox_wavelength = QtGui.QDoubleSpinBox(self.tab)
        self.spinbox_wavelength.setEnabled(False)
        self.spinbox_wavelength.setGeometry(QtCore.QRect(110, 110, 62, 22))
        self.spinbox_wavelength.setAccelerated(True)
        self.spinbox_wavelength.setDecimals(3)
        self.spinbox_wavelength.setSingleStep(0.001)
        self.spinbox_wavelength.setObjectName(_fromUtf8("spinbox_wavelength"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 91, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.slider_horiz = Qwt5.QwtSlider(self.tab)
        self.slider_horiz.setGeometry(QtCore.QRect(10, 150, 171, 41))
        self.slider_horiz.setReadOnly(False)
        self.slider_horiz.setValid(True)
        self.slider_horiz.setOrientation(QtCore.Qt.Horizontal)
        self.slider_horiz.setScalePosition(Qwt5.QwtSlider.BottomScale)
        self.slider_horiz.setBgStyle(Qwt5.QwtSlider.BgSlot)
        self.slider_horiz.setThumbLength(16)
        self.slider_horiz.setThumbWidth(12)
        self.slider_horiz.setBorderWidth(2)
        self.slider_horiz.setObjectName(_fromUtf8("slider_horiz"))
        self.slider_height = Qwt5.QwtSlider(self.tab)
        self.slider_height.setGeometry(QtCore.QRect(190, 40, 61, 141))
        self.slider_height.setOrientation(QtCore.Qt.Vertical)
        self.slider_height.setScalePosition(Qwt5.QwtSlider.RightScale)
        self.slider_height.setBgStyle(Qwt5.QwtSlider.BgSlot)
        self.slider_height.setThumbLength(16)
        self.slider_height.setThumbWidth(12)
        self.slider_height.setBorderWidth(2)
        self.slider_height.setObjectName(_fromUtf8("slider_height"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(0, 10, 101, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabwidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.combobox_randwavetype = QtGui.QComboBox(self.tab_2)
        self.combobox_randwavetype.setGeometry(QtCore.QRect(110, 10, 111, 22))
        self.combobox_randwavetype.setObjectName(_fromUtf8("combobox_randwavetype"))
        self.combobox_randwavetype.addItem(_fromUtf8(""))
        self.combobox_randwavetype.addItem(_fromUtf8(""))
        self.combobox_randwavetype.addItem(_fromUtf8(""))
        self.combobox_randwavetype.addItem(_fromUtf8(""))
        self.combobox_randwavetype.addItem(_fromUtf8(""))
        self.table_rwaves = QtGui.QTableWidget(self.tab_2)
        self.table_rwaves.setEnabled(True)
        self.table_rwaves.setGeometry(QtCore.QRect(10, 40, 241, 161))
        self.table_rwaves.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_rwaves.setProperty("showDropIndicator", False)
        self.table_rwaves.setDragDropOverwriteMode(False)
        self.table_rwaves.setAlternatingRowColors(False)
        self.table_rwaves.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.table_rwaves.setShowGrid(True)
        self.table_rwaves.setCornerButtonEnabled(False)
        self.table_rwaves.setObjectName(_fromUtf8("table_rwaves"))
        self.table_rwaves.setColumnCount(2)
        self.table_rwaves.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.table_rwaves.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_rwaves.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_rwaves.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table_rwaves.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table_rwaves.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table_rwaves.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table_rwaves.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_rwaves.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.table_rwaves.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table_rwaves.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table_rwaves.setItem(2, 1, item)
        self.table_rwaves.horizontalHeader().setVisible(False)
        self.table_rwaves.horizontalHeader().setDefaultSectionSize(175)
        self.table_rwaves.horizontalHeader().setHighlightSections(False)
        self.table_rwaves.horizontalHeader().setMinimumSectionSize(30)
        self.table_rwaves.horizontalHeader().setSortIndicatorShown(False)
        self.table_rwaves.horizontalHeader().setStretchLastSection(True)
        self.table_rwaves.verticalHeader().setVisible(False)
        self.table_rwaves.verticalHeader().setCascadingSectionResizes(True)
        self.table_rwaves.verticalHeader().setDefaultSectionSize(20)
        self.table_rwaves.verticalHeader().setHighlightSections(False)
        self.table_rwaves.verticalHeader().setMinimumSectionSize(15)
        self.table_rwaves.verticalHeader().setStretchLastSection(False)
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tabwidget.addTab(self.tab_2, _fromUtf8(""))
        self.dock_time_series = QtGui.QDockWidget(self.centralwidget)
        self.dock_time_series.setGeometry(QtCore.QRect(10, 580, 325, 256))
        self.dock_time_series.setMinimumSize(QtCore.QSize(325, 256))
        self.dock_time_series.setMaximumSize(QtCore.QSize(325, 256))
        self.dock_time_series.setObjectName(_fromUtf8("dock_time_series"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.plot_ts = Qwt5.QwtPlot(self.dockWidgetContents_2)
        self.plot_ts.setGeometry(QtCore.QRect(10, 10, 291, 201))
        self.plot_ts.setStyleSheet(_fromUtf8("font: 8pt \"MS Shell Dlg 2\";"))
        self.plot_ts.setObjectName(_fromUtf8("plot_ts"))
        self.dock_time_series.setWidget(self.dockWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolbar_main = QtGui.QToolBar(MainWindow)
        self.toolbar_main.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.toolbar_main.setMovable(False)
        self.toolbar_main.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolbar_main.setObjectName(_fromUtf8("toolbar_main"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar_main)
        self.dock_spectrum = QtGui.QDockWidget(MainWindow)
        self.dock_spectrum.setMinimumSize(QtCore.QSize(325, 256))
        self.dock_spectrum.setMaximumSize(QtCore.QSize(325, 256))
        self.dock_spectrum.setFloating(False)
        self.dock_spectrum.setObjectName(_fromUtf8("dock_spectrum"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.plot_spec = Qwt5.QwtPlot(self.dockWidgetContents)
        self.plot_spec.setGeometry(QtCore.QRect(10, 10, 291, 201))
        self.plot_spec.setStyleSheet(_fromUtf8("font: 8pt \"MS Shell Dlg 2\";"))
        self.plot_spec.setObjectName(_fromUtf8("plot_spec"))
        self.dock_spectrum.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dock_spectrum)
        self.actionRegular = QtGui.QAction(MainWindow)
        self.actionRegular.setObjectName(_fromUtf8("actionRegular"))
        self.actionRandom = QtGui.QAction(MainWindow)
        self.actionRandom.setObjectName(_fromUtf8("actionRandom"))
        self.action_view_ts = QtGui.QAction(MainWindow)
        self.action_view_ts.setCheckable(True)
        self.action_view_ts.setChecked(True)
        self.action_view_ts.setObjectName(_fromUtf8("action_view_ts"))
        self.action_view_spec = QtGui.QAction(MainWindow)
        self.action_view_spec.setCheckable(True)
        self.action_view_spec.setChecked(True)
        self.action_view_spec.setObjectName(_fromUtf8("action_view_spec"))
        self.action_wiki = QtGui.QAction(MainWindow)
        self.action_wiki.setObjectName(_fromUtf8("action_wiki"))
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.action_editsettings = QtGui.QAction(MainWindow)
        self.action_editsettings.setEnabled(False)
        self.action_editsettings.setObjectName(_fromUtf8("action_editsettings"))
        self.action_start = QtGui.QAction(MainWindow)
        self.action_start.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_start.setIcon(icon)
        self.action_start.setObjectName(_fromUtf8("action_start"))
        self.actionRecording = QtGui.QAction(MainWindow)
        self.actionRecording.setObjectName(_fromUtf8("actionRecording"))
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.action_view_ts)
        self.menuView.addAction(self.action_view_spec)
        self.menuHelp.addAction(self.action_wiki)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action_about)
        self.menuOptions.addAction(self.action_editsettings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolbar_main.addAction(self.action_start)

        self.retranslateUi(MainWindow)
        self.tabwidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.action_view_ts, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.dock_time_series.setVisible)
        QtCore.QObject.connect(self.dock_time_series, QtCore.SIGNAL(_fromUtf8("visibilityChanged(bool)")), self.action_view_ts.setChecked)
        QtCore.QObject.connect(self.action_view_spec, QtCore.SIGNAL(_fromUtf8("triggered(bool)")), self.dock_spectrum.setVisible)
        QtCore.QObject.connect(self.dock_spectrum, QtCore.SIGNAL(_fromUtf8("visibilityChanged(bool)")), self.action_view_spec.setChecked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MakeWaves", None))
        self.combobox_regparams.setItemText(0, _translate("MainWindow", "Height and Period", None))
        self.combobox_regparams.setItemText(1, _translate("MainWindow", "Height and Wavelength", None))
        self.label.setText(_translate("MainWindow", "Wave Height (m):", None))
        self.label_2.setText(_translate("MainWindow", "Wave Period (s):", None))
        self.label_3.setText(_translate("MainWindow", "Wavelength (m):", None))
        self.label_4.setText(_translate("MainWindow", "Set Parameters:", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab), _translate("MainWindow", "Regular", None))
        self.combobox_randwavetype.setItemText(0, _translate("MainWindow", "Bretschneider", None))
        self.combobox_randwavetype.setItemText(1, _translate("MainWindow", "JONSWAP", None))
        self.combobox_randwavetype.setItemText(2, _translate("MainWindow", "NH Extreme", None))
        self.combobox_randwavetype.setItemText(3, _translate("MainWindow", "NH Typical", None))
        self.combobox_randwavetype.setItemText(4, _translate("MainWindow", "Pierson Moscowitz", None))
        item = self.table_rwaves.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "0", None))
        item = self.table_rwaves.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "1", None))
        item = self.table_rwaves.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "2", None))
        item = self.table_rwaves.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Parameter", None))
        item = self.table_rwaves.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value", None))
        __sortingEnabled = self.table_rwaves.isSortingEnabled()
        self.table_rwaves.setSortingEnabled(False)
        item = self.table_rwaves.item(0, 0)
        item.setText(_translate("MainWindow", "Significant Wave Height (m)", None))
        item = self.table_rwaves.item(0, 1)
        item.setText(_translate("MainWindow", "0.1", None))
        item = self.table_rwaves.item(1, 0)
        item.setText(_translate("MainWindow", "Significant Wave Period (s)", None))
        item = self.table_rwaves.item(1, 1)
        item.setText(_translate("MainWindow", "1", None))
        item = self.table_rwaves.item(2, 0)
        item.setText(_translate("MainWindow", "Scale Ratio", None))
        item = self.table_rwaves.item(2, 1)
        item.setText(_translate("MainWindow", "1", None))
        self.table_rwaves.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("MainWindow", "Spectrum Type:", None))
        self.tabwidget.setTabText(self.tabwidget.indexOf(self.tab_2), _translate("MainWindow", "Random", None))
        self.dock_time_series.setWindowTitle(_translate("MainWindow", "Output Time Series", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Settings", None))
        self.toolbar_main.setWindowTitle(_translate("MainWindow", "Main Toolbar", None))
        self.dock_spectrum.setWindowTitle(_translate("MainWindow", "Output Spectrum", None))
        self.actionRegular.setText(_translate("MainWindow", "Regular", None))
        self.actionRandom.setText(_translate("MainWindow", "Random", None))
        self.action_view_ts.setText(_translate("MainWindow", "Output Time Series", None))
        self.action_view_spec.setText(_translate("MainWindow", "Output Spectrum", None))
        self.action_wiki.setText(_translate("MainWindow", "Wiki", None))
        self.action_about.setText(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.action_editsettings.setText(_translate("MainWindow", "Recalculate Limits", None))
        self.action_start.setText(_translate("MainWindow", "Start", None))
        self.action_start.setToolTip(_translate("MainWindow", "Start Generating Waves", None))
        self.actionRecording.setText(_translate("MainWindow", "Recording...", None))

from PyQt4 import Qwt5
import resources_rc
