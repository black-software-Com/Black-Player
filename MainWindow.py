#!/use/bin/python3
# Black-MediaPlayer v1.0

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(774, 622)
        self.open_file_action = QAction(MainWindow)
        self.open_file_action.setObjectName(u"open_file_action")
        self.exit_m = QAction(MainWindow)
        self.exit_m.setObjectName(u"exit_m")
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        self.black_m = QAction(MainWindow)
        self.black_m.setObjectName(u"black_m")
        self.dev_m = QAction(MainWindow)
        self.dev_m.setObjectName(u"dev_m")
        self.help_m = QAction(MainWindow)
        self.help_m.setObjectName(u"help_m")
        self.feedback_m = QAction(MainWindow)
        self.feedback_m.setObjectName(u"feedback_m")
        self.about_m = QAction(MainWindow)
        self.about_m.setObjectName(u"about_m")
        self.volup_m = QAction(MainWindow)
        self.volup_m.setObjectName(u"volup_m")
        self.voldown_m = QAction(MainWindow)
        self.voldown_m.setObjectName(u"voldown_m")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.playlistView = QListView(self.centralWidget)
        self.playlistView.setObjectName(u"playlistView")
        self.playlistView.setAcceptDrops(True)
        self.playlistView.setProperty("showDropIndicator", True)
        self.playlistView.setDragDropMode(QAbstractItemView.DropOnly)
        self.playlistView.setDefaultDropAction(Qt.CopyAction)
        self.playlistView.setAlternatingRowColors(True)
        self.playlistView.setUniformItemSizes(True)

        self.verticalLayout.addWidget(self.playlistView)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.currentTimeLabel = QLabel(self.centralWidget)
        self.currentTimeLabel.setObjectName(u"currentTimeLabel")
        self.currentTimeLabel.setMinimumSize(QSize(80, 0))
        self.currentTimeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.currentTimeLabel)

        self.timeSlider = QSlider(self.centralWidget)
        self.timeSlider.setObjectName(u"timeSlider")
        self.timeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.timeSlider)

        self.totalTimeLabel = QLabel(self.centralWidget)
        self.totalTimeLabel.setObjectName(u"totalTimeLabel")
        self.totalTimeLabel.setMinimumSize(QSize(80, 0))
        self.totalTimeLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.totalTimeLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.previousButton = QPushButton(self.centralWidget)
        self.previousButton.setObjectName(u"previousButton")
        icon = QIcon()
        icon.addFile(u"images/control-skip-180.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previousButton.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.previousButton)

        self.playButton = QPushButton(self.centralWidget)
        self.playButton.setObjectName(u"playButton")
        icon1 = QIcon()
        icon1.addFile(u"images/control.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.playButton)

        self.pauseButton = QPushButton(self.centralWidget)
        self.pauseButton.setObjectName(u"pauseButton")
        icon2 = QIcon()
        icon2.addFile(u"images/control-pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pauseButton.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.pauseButton)

        self.stopButton = QPushButton(self.centralWidget)
        self.stopButton.setObjectName(u"stopButton")
        icon3 = QIcon()
        icon3.addFile(u"images/control-stop-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.stopButton)

        self.nextButton = QPushButton(self.centralWidget)
        self.nextButton.setObjectName(u"nextButton")
        icon4 = QIcon()
        icon4.addFile(u"images/control-skip.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextButton.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.nextButton)

        self.viewButton = QPushButton(self.centralWidget)
        self.viewButton.setObjectName(u"viewButton")
        icon5 = QIcon()
        icon5.addFile(u"images/application-image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.viewButton.setIcon(icon5)
        self.viewButton.setCheckable(True)
      
        self.horizontalLayout_5.addWidget(self.viewButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.label = QLabel(self.centralWidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"images/speaker-volume.png"))

        self.horizontalLayout_5.addWidget(self.label)

        self.volumeSlider = QSlider(self.centralWidget)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(100)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_5.addWidget(self.volumeSlider)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.label_2 = QLabel(self.centralWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 774, 26))
        self.menuFIle = QMenu(self.menuBar)
        self.menuFIle.setObjectName(u"menuFIle")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuVolume = QMenu(self.menuBar)
        self.menuVolume.setObjectName(u"menuVolume")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menuBar.addAction(self.menuFIle.menuAction())
        self.menuBar.addAction(self.menuVolume.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFIle.addAction(self.open_file_action)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.exit_m)
        self.menuHelp.addActions([self.black_m,self.dev_m])
        self.help_mm = self.menuHelp.addMenu("Help")
        self.help_mm.addActions([self.help_m,self.feedback_m])
        
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.about_m)
        self.menuVolume.addAction(self.volup_m)
        self.menuVolume.addAction(self.voldown_m)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Black-Player", None))
        MainWindow.setWindowIcon(QIcon('./Scr/black-videoplayer-icon.png'))
        self.open_file_action.setText(QCoreApplication.translate("MainWindow", u"Open file...", None))
        self.open_file_action.setShortcut('Ctrl+o')
        self.open_file_action.setStatusTip("Open File")
        self.exit_m.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.exit_m.setShortcut('Alt+F4')
        self.exit_m.setStatusTip("Exit Program")
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.black_m.setText("Black")
        self.black_m.setShortcut('F1')
        self.black_m.setStatusTip("Black-Software Website")
        self.dev_m.setText("Dev")
        self.dev_m.setShortcut('F2')
        self.dev_m.setStatusTip("Black Developer")
        self.help_m.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.help_m.setShortcut('Ctrl+H')
        self.help_m.setStatusTip("Black-Player helper")
        self.feedback_m.setText(QCoreApplication.translate("MainWindow", u"Send FeedBack", None))
        self.feedback_m.setShortcut('Ctrl+f')
        self.feedback_m.setStatusTip('Send FeedBack')
        self.about_m.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.about_m.setShortcut('F3')
        self.about_m.setStatusTip("About Black-Player")
        self.volup_m.setText(QCoreApplication.translate("MainWindow", u"Volume Up", None))
        self.volup_m.setStatusTip("Volume Up")
        self.voldown_m.setText(QCoreApplication.translate("MainWindow", u"Volume Down", None))
        self.voldown_m.setStatusTip("Volume Down")
        self.currentTimeLabel.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.totalTimeLabel.setText(QCoreApplication.translate("MainWindow", u"0:00", None))
        self.previousButton.setText("")
        self.playButton.setText("")
        self.pauseButton.setText("")
        self.stopButton.setText("")
        self.nextButton.setText("")
        self.viewButton.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Black-Player v1.0", None))
        self.menuFIle.setTitle(QCoreApplication.translate("MainWindow", u"FIle", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuVolume.setTitle(QCoreApplication.translate("MainWindow", u"Sound", None))
