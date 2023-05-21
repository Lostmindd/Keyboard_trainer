
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 618)
        MainWindow.setMinimumSize(QSize(1200, 600))
        MainWindow.setMaximumSize(QSize(1200, 618))
        MainWindow.setBaseSize(QSize(10, 10))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 245, 245);")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.menu_frame = QFrame(self.centralwidget)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setGeometry(QRect(0, 0, 1201, 91))
        self.menu_frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: #FFFFFF;")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.start_button = QPushButton(self.menu_frame)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setEnabled(True)
        self.start_button.setGeometry(QRect(20, 20, 161, 51))
        self.start_button.setStyleSheet(u"QPushButton { \n"
"background-color:rgb(89, 175, 255) ;\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"}\n"
"QPushButton:hover { \n"
"background-color:rgb(69, 155, 235) ;\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"}\n"
"QPushButton:pressed { \n"
"background-color:rgb(39, 125, 205) ;\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"}")
        self.en_button = QPushButton(self.menu_frame)
        self.en_button.setObjectName(u"en_button")
        self.en_button.setGeometry(QRect(1040, 20, 61, 51))
        self.en_button.setStyleSheet(u"QPushButton { \n"
"background-color:rgb(0, 0, 0) ;\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #FFFFF;\n"
"}\n"
"QPushButton:hover { \n"
"background-color:rgb(80, 80, 80) ;\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #FFFFF;\n"
"}\n"
"")
        self.stat_button = QPushButton(self.menu_frame)
        self.stat_button.setObjectName(u"stat_button")
        self.stat_button.setGeometry(QRect(300, 20, 201, 51))
        self.stat_button.setStyleSheet(u"QPushButton { \n"
"background-color:rgb(255, 255, 255) ;\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"}\n"
"QPushButton:hover { \n"
"background-color:rgb(230, 230, 230) ;\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"}\n"
"QPushButton:pressed { \n"
"background-color:rgb(200, 200, 200) ;\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"}")
        self.ru_button = QPushButton(self.menu_frame)
        self.ru_button.setObjectName(u"ru_button")
        self.ru_button.setGeometry(QRect(1120, 20, 61, 51))
        self.ru_button.setStyleSheet(u"QPushButton { \n"
"background-color:rgb(255, 255, 255) ;\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"}\n"
"")
        self.info_button = QPushButton(self.menu_frame)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(510, 20, 211, 51))
        self.info_button.setStyleSheet(u"QPushButton { \n"
"background-color:rgb(255, 255, 255) ;\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"}\n"
"QPushButton:hover { \n"
"background-color:rgb(230, 230, 230) ;\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"}\n"
"QPushButton:pressed { \n"
"background-color:rgb(200, 200, 200) ;\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;\n"
"}")
        self.difficulty_button = QPushButton(self.menu_frame)
        self.difficulty_button.setObjectName(u"difficulty_button")
        self.difficulty_button.setGeometry(QRect(730, 20, 201, 51))
        self.difficulty_button.setStyleSheet(u"\nQPushButton { \n"
"background-color:rgb(121, 216, 88) ;\n"
"border-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: #000000;\n}\nQPushButton:hover { \n"
"background-color:rgb(101, 196, 68);\n"
"border-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: #000000;\n}\nQPushButton:pressed { \n"
"background-color:rgb(71, 166, 38) ;\n"
"border-radius: 20px; \nfont: 24pt \"MS Shell Dlg 2\";\ncolor: #000000;\n}")
        self.info_frame = QFrame(self.centralwidget)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setGeometry(QRect(0, 89, 1201, 531))
        self.info_frame.setStyleSheet(u"border: 0;")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.info_tab = QTextBrowser(self.info_frame)
        self.info_tab.setObjectName(u"info_tab")
        self.info_tab.setGeometry(QRect(10, 0, 1191, 531))
        self.info_tab.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border: 0;\n"
"font: 50pt \"MS Shell Dlg 2\";\n"
"overflow-wrap: break-word; \n"
"color: #000000;\n"
"overflow-wrap: break-word;\n"
"\n"
"")
        self.info_tab.setUndoRedoEnabled(True)
        self.info_tab.setTextInteractionFlags(Qt.NoTextInteraction)
        self.stat_frame = QFrame(self.centralwidget)
        self.stat_frame.setObjectName(u"stat_frame")
        self.stat_frame.setEnabled(True)
        self.stat_frame.setGeometry(QRect(0, 89, 1211, 541))
        self.stat_frame.setStyleSheet(u"border: 0;")
        self.stat_frame.setFrameShape(QFrame.StyledPanel)
        self.stat_frame.setFrameShadow(QFrame.Raised)
        self.stat_table = QTableWidget(self.stat_frame)
        if (self.stat_table.columnCount() < 3):
            self.stat_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.stat_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.stat_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.stat_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.stat_table.rowCount() < 6):
            self.stat_table.setRowCount(6)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.stat_table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.stat_table.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.stat_table.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.stat_table.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.stat_table.setVerticalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.stat_table.setVerticalHeaderItem(5, __qtablewidgetitem8)
        font = QFont()
        font.setPointSize(20)
        font.setBold(False)

        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font);
        self.stat_table.setItem(0, 0, __qtablewidgetitem9)
        font1 = QFont()
        font1.setPointSize(20)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font1);
        self.stat_table.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font1);
        self.stat_table.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font1);
        self.stat_table.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font1);
        self.stat_table.setItem(1, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font1);
        self.stat_table.setItem(1, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem15.setFont(font1);
        self.stat_table.setItem(2, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem16.setFont(font1);
        self.stat_table.setItem(2, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem17.setFont(font1);
        self.stat_table.setItem(2, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem18.setFont(font1);
        self.stat_table.setItem(3, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem19.setFont(font1);
        self.stat_table.setItem(3, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem20.setFont(font1);
        self.stat_table.setItem(3, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem21.setFont(font1);
        self.stat_table.setItem(4, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem22.setFont(font1);
        self.stat_table.setItem(4, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem23.setFont(font1);
        self.stat_table.setItem(4, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setFont(font1);
        self.stat_table.setItem(5, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem25.setFont(font1);
        self.stat_table.setItem(5, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem26.setFont(font1);
        self.stat_table.setItem(5, 2, __qtablewidgetitem26)
        self.stat_table.setObjectName(u"stat_table")
        self.stat_table.setGeometry(QRect(20, 60, 1161, 471))
        self.stat_table.setStyleSheet(u"font: 15pt \"MS Shell Dlg 2\";")
        self.stat_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.stat_table.setShowGrid(True)
        self.stat_table.horizontalHeader().setMinimumSectionSize(150)
        self.stat_table.horizontalHeader().setDefaultSectionSize(224)
        self.stat_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.stat_table.verticalHeader().setDefaultSectionSize(55)
  #=================
        self.result_frame = QFrame(self.centralwidget)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setEnabled(True)
        self.result_frame.setGeometry(QRect(0, 89, 1211, 541))
        self.result_frame.setStyleSheet(u"border: 0;")
        self.result_frame.setFrameShape(QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QFrame.Raised)
        self.result_stat_tab2 = QLabel(self.result_frame)
        self.result_stat_tab2.setObjectName(u"stat_tab2")
        self.result_stat_tab2.setGeometry(QRect(10, 80, 1201, 121))
        self.result_stat_tab2.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
                                     "border: 0;\n"
                                     "font: 32pt \"MS Shell Dlg 2\";\n"
                                     "overflow-wrap: break-word; \n"
                                     "color: #000000;\n"
                                     "overflow-wrap: break-word;\n"
                                     "\n"
                                     "")
        self.result_stat_tab2.setTextFormat(Qt.PlainText)
        self.result_stat_tab2.setScaledContents(False)
        self.result_stat_tab2.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.result_stat_tab2.setWordWrap(True)
        self.result_stat_tab2.setOpenExternalLinks(False)
        self.result_stat_tab1 = QLabel(self.result_frame)
        self.result_stat_tab1.setObjectName(u"stat_tab1")
        self.result_stat_tab1.setGeometry(QRect(10, 0, 1201, 91))
        self.result_stat_tab1.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
                                     "border: 0;\n"
                                     "font: 40pt \"MS Shell Dlg 2\";\n"
                                     "overflow-wrap: break-word; \n"
                                     "color: #000000;\n"
                                     "overflow-wrap: break-word;\n"
                                     "\n"
                                     "")
        self.result_stat_tab1.setTextFormat(Qt.PlainText)
        self.result_stat_tab1.setScaledContents(False)
        self.result_stat_tab1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.result_stat_tab1.setWordWrap(True)
        self.result_stat_tab1.setOpenExternalLinks(False)
        self.result_stat_tab_day_1 = QLabel(self.result_frame)
        self.result_stat_tab_day_1.setObjectName(u"stat_tab_day_1")
        self.result_stat_tab_day_1.setGeometry(QRect(10, 140, 1201, 81))
        self.result_stat_tab_day_1.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
                                          "border: 0;\n"
                                          "font: 32pt \"MS Shell Dlg 2\";\n"
                                          "overflow-wrap: break-word; \n"
                                          "text-decoration: underline; \n"
                                          "color: #000000;\n"
                                          "overflow-wrap: break-word;\n"
                                          "\n"
                                          "")
        self.result_stat_tab_day_1.setTextFormat(Qt.PlainText)
        self.result_stat_tab_day_1.setScaledContents(False)
        self.result_stat_tab_day_1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.result_stat_tab_day_1.setWordWrap(True)
        self.result_stat_tab_day_1.setOpenExternalLinks(False)
        self.result_stat_tab_day_3 = QLabel(self.result_frame)
        self.result_stat_tab_day_3.setObjectName(u"stat_tab_day_3")
        self.result_stat_tab_day_3.setGeometry(QRect(10, 200, 1201, 81))
        self.result_stat_tab_day_3.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
                                          "border: 0;\n"
                                          "font: 32pt \"MS Shell Dlg 2\";\n"
                                          "overflow-wrap: break-word; \n"
                                          "text-decoration: underline; \n"
                                          "color: #000000;\n"
                                          "overflow-wrap: break-word;\n"
                                          "\n"
                                          "")
        self.result_stat_tab_day_3.setTextFormat(Qt.PlainText)
        self.result_stat_tab_day_3.setScaledContents(False)
        self.result_stat_tab_day_3.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.result_stat_tab_day_3.setWordWrap(True)
        self.result_stat_tab_day_3.setOpenExternalLinks(False)
        self.result_stat_tab_day_10 = QLabel(self.result_frame)
        self.result_stat_tab_day_10.setObjectName(u"stat_tab_day_10")
        self.result_stat_tab_day_10.setGeometry(QRect(10, 260, 1211, 81))
        self.result_stat_tab_day_10.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
                                           "border: 0;\n"
                                           "font: 32pt \"MS Shell Dlg 2\";\n"
                                           "overflow-wrap: break-word; \n"
                                           "text-decoration: underline; \n"
                                           "color: #000000;\n"
                                           "overflow-wrap: break-word;\n"
                                           "\n"
                                           "")
        self.result_stat_tab_day_10.setTextFormat(Qt.PlainText)
        self.result_stat_tab_day_10.setScaledContents(False)
        self.result_stat_tab_day_10.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.result_stat_tab_day_10.setWordWrap(True)
        self.result_stat_tab_day_10.setOpenExternalLinks(False)
        self.result_stat_tab_day_30 = QLabel(self.result_frame)
        self.result_stat_tab_day_30.setObjectName(u"stat_tab_day_30")
        self.result_stat_tab_day_30.setGeometry(QRect(110, 320, 1001, 111))
        self.result_stat_tab_day_30.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
                                           "border: 0;\n"
                                           "font: 32pt \"MS Shell Dlg 2\";\n"
                                           "overflow-wrap: break-word; \n"
                                           "text-decoration: underline; \n"
                                           "color: #000000;\n"
                                           "overflow-wrap: break-word;\n"
                                           "\n"
                                           "")
        self.result_stat_tab_day_30.setTextFormat(Qt.PlainText)
        self.result_stat_tab_day_30.setScaledContents(False)
        self.result_stat_tab_day_30.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.result_stat_tab_day_30.setWordWrap(True)
        self.result_stat_tab_day_30.setOpenExternalLinks(False)

        self.result_stat_tab_day_4 = QLabel(self.result_frame)
        self.result_stat_tab_day_4.setObjectName(u"stat_tab_day_30")
        self.result_stat_tab_day_4.setGeometry(QRect(110, 380, 1001, 111))
        self.result_stat_tab_day_4.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
                                                  "border: 0;\n"
                                                  "font: 32pt \"MS Shell Dlg 2\";\n"
                                                  "overflow-wrap: break-word; \n"
                                                  "text-decoration: underline; \n"
                                                  "color: #000000;\n"
                                                  "overflow-wrap: break-word;\n"
                                                  "\n"
                                                  "")
        self.result_stat_tab_day_4.setTextFormat(Qt.PlainText)
        self.result_stat_tab_day_4.setScaledContents(False)
        self.result_stat_tab_day_4.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.result_stat_tab_day_4.setWordWrap(True)
        self.result_stat_tab_day_4.setOpenExternalLinks(False)

        self.result_stat_tab_day_5 = QLabel(self.result_frame)
        self.result_stat_tab_day_5.setObjectName(u"stat_tab_day_30")
        self.result_stat_tab_day_5.setGeometry(QRect(110, 440, 1001, 111))
        self.result_stat_tab_day_5.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
                                                 "border: 0;\n"
                                                 "font: 32pt \"MS Shell Dlg 2\";\n"
                                                 "overflow-wrap: break-word; \n"
                                                 "text-decoration: underline; \n"
                                                 "color: #000000;\n"
                                                 "overflow-wrap: break-word;\n"
                                                 "\n"
                                                 "")
        self.result_stat_tab_day_5.setTextFormat(Qt.PlainText)
        self.result_stat_tab_day_5.setScaledContents(False)
        self.result_stat_tab_day_5.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.result_stat_tab_day_5.setWordWrap(True)
        self.result_stat_tab_day_5.setOpenExternalLinks(False)
  #=================
        self.training_window = QFrame(self.centralwidget)
        self.training_window.setObjectName(u"training_window")
        self.training_window.setGeometry(QRect(0, 89, 1201, 531))
        self.training_window.setStyleSheet(u"border: 0;")
        self.training_window.setFrameShape(QFrame.StyledPanel)
        self.training_window.setFrameShadow(QFrame.Raised)
        self.text_for_input = QLabel(self.training_window)
        self.text_for_input.setObjectName(u"text_for_input")
        self.text_for_input.setGeometry(QRect(40, 20, 1121, 101))
        self.text_for_input.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border: 0;\n"
"font: 50pt \"MS Shell Dlg 2\";\n"
"overflow-wrap: break-word; \n"
"color: #000000;\n"
"overflow-wrap: break-word;\n"
"\n"
"")
        self.text_for_input.setTextFormat(Qt.PlainText)
        self.text_for_input.setScaledContents(False)
        self.text_for_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.text_for_input.setWordWrap(False)
        self.text_for_input.setOpenExternalLinks(False)
        self.text_for_input_printed = QLabel(self.training_window)
        self.text_for_input_printed.setObjectName(u"text_for_input_printed")
        self.text_for_input_printed.setGeometry(QRect(40, 20, 1121, 101))
        self.text_for_input_printed.setStyleSheet(u"background-color: rgb(219, 219, 219,0);\n"
"border: 0;\n"
"font: 50pt \"MS Shell Dlg 2\"; \n"                                              

"color: #555999;\n"
"\n"
"\n"
"")
        self.text_for_input_printed.setTextFormat(Qt.PlainText)
        self.text_for_input_printed.setScaledContents(False)
        self.text_for_input_printed.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.text_for_input_printed.setWordWrap(False)
        self.text_for_input_printed.setOpenExternalLinks(False)
        self.text = QLabel(self.training_window)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(40, 110, 1121, 391))
        self.text.setStyleSheet(u"background-color: rgb(245, 245, 245);\n"
"border: 0;\n"
"font: 50pt \"MS Shell Dlg 2\";\n"
"overflow-wrap: break-word; \n"
"color: #000000;\n"
"word-wrap: break-word;")
        self.start_button.setFocusPolicy(Qt.NoFocus)
        self.stat_button.setFocusPolicy(Qt.NoFocus)
        self.info_button.setFocusPolicy(Qt.NoFocus)
        self.difficulty_button.setFocusPolicy(Qt.NoFocus)
        self.en_button.setFocusPolicy(Qt.NoFocus)
        self.ru_button.setFocusPolicy(Qt.NoFocus)
        self.info_tab.setFocusPolicy(Qt.NoFocus)
        self.text.setTextFormat(Qt.PlainText)
        self.text.setScaledContents(False)
        self.text.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.text.setWordWrap(True)
        self.text.setOpenExternalLinks(False)

        self.gradient = QLabel(self.training_window)
        self.gradient.setObjectName(u"gradient")
        self.gradient.setGeometry(QRect(40, 110, 1121, 391))
        self.gradient.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(245, 245, 245, 150), stop:1 rgba(245, 245, 245, 255));\n"
            "")
        self.gradient.setTextFormat(Qt.PlainText)
        self.gradient.setScaledContents(False)
        self.gradient.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.gradient.setWordWrap(True)
        self.gradient.setOpenExternalLinks(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Keyboard trainer", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.en_button.setText(QCoreApplication.translate("MainWindow", u"EN", None))
        self.stat_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.ru_button.setText(QCoreApplication.translate("MainWindow", u"RU", None))
        self.info_button.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.difficulty_button.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.info_tab.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:50pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">1) \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c, \u043d\u0430\u0436\u0430\u0442\u0438\u0435\u043c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443"
                        " &quot;\u0421\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c&quot;. \u0412\u044b\u0431\u0440\u0430\u043d\u043d\u0430\u044f \u043d\u0430 \u0434\u0430\u043d\u043d\u044b\u0439 \u043c\u043e\u043c\u0435\u043d\u0442 \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442\u0441\u044f \u043f\u043e \u0446\u0432\u0435\u0442\u0443 \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0432\u0443\u044e\u0449\u0435\u0439 \u043a\u043d\u043e\u043f\u043a\u0438:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">---&quot;\u0417\u0435\u043b\u0435\u043d\u044b\u0439&quot; - \u043d\u0438\u0437\u043a\u0438\u0439 \u0440\u0435\u0436\u0438\u043c \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0438;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;"
                        "\">---&quot;\u0416\u0451\u043b\u0442\u044b\u0439&quot; - \u0441\u0440\u0435\u0434\u043d\u0438\u0439 \u0440\u0435\u0436\u0438\u043c \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0438;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">---&quot;\u041a\u0440\u0430\u0441\u043d\u044b\u0439&quot; - \u0432\u044b\u0441\u043e\u043a\u0438\u0439 \u0440\u0435\u0436\u0438\u043c \u0441\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u0438.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">2) \u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u044f\u0437\u044b\u043a \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0445 \u0441\u043b\u043e\u0432 \u043d\u0430\u0436\u0430\u0442\u0438\u0435\u043c \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 en/ru:</span></p>\n"
""
                        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">---&quot;en&quot; - \u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">---&quot;ru&quot; - \u0420\u0443\u0441\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">3) \u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;\u0441\u0442\u0430\u0440\u0442&quot;, \u0447\u0442\u043e\u0431\u044b \u043d\u0430\u0447\u0430\u0442\u044c \u0442\u0440\u0435\u043d\u0438\u0440\u043e\u0432\u043a\u0443.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; mar"
                        "gin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">4) \u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043a\u043d\u043e\u043f\u043a\u0443 &quot;\u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430&quot;, \u0447\u0442\u043e\u0431\u044b \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0441\u0432\u043e\u044e \u0441\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0443.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">5) \u0427\u0442\u043e\u0431\u044b \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043d\u0430\u0431\u043e\u0440 \u0441\u043b\u043e\u0432 - \u043f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u0448\u0430\u0433\u0438 1-3 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u0430.</span></p></body></html>", None))

        ___qtablewidgetitem = self.stat_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"\u0417\u0430 \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None));
        ___qtablewidgetitem1 = self.stat_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0417\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 3 \u0434\u043d\u044f",
                                                                None));
        ___qtablewidgetitem2 = self.stat_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0417\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 10 \u0434\u043d\u0435\u0439",
                                                                None));
        ___qtablewidgetitem3 = self.stat_table.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0421\u0440\u0435\u0434\u043d\u0435\u0435 \u0432\u0440\u0435\u043c\u044f (\u0441\u0435\u043a\u0443\u043d\u0434)",
                                                                None));
        ___qtablewidgetitem4 = self.stat_table.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u041d\u0430\u043f\u0435\u0447\u0430\u0442\u0430\u043d\u043e \u0441\u043b\u043e\u0432 \u0432 \u0441\u0440\u0435\u0434\u043d\u0435\u043c",
                                                                None));
        ___qtablewidgetitem5 = self.stat_table.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u041d\u0430\u043f\u0435\u0447\u0430\u0442\u0430\u043d\u043e \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432 \u0432 \u0441\u0440\u0435\u0434\u043d\u0435\u043c",
                                                                None));
        ___qtablewidgetitem6 = self.stat_table.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0421\u043e\u0432\u0435\u0440\u0448\u0435\u043d\u043d\u043e \u043e\u0448\u0438\u0431\u043e\u043a \u0432 \u0441\u0440\u0435\u0434\u043d\u0435\u043c",
                                                                None));
        ___qtablewidgetitem7 = self.stat_table.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043d\u0430\u0431\u043e\u0440\u0430 (\u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432 \u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0443)",
                                                                None));
        ___qtablewidgetitem8 = self.stat_table.verticalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f \u0442\u043e\u0447\u043d\u043e\u0441\u0442\u044c",
                                                                None));

        __sortingEnabled = self.stat_table.isSortingEnabled()
        self.stat_table.setSortingEnabled(False)
        self.stat_table.setSortingEnabled(__sortingEnabled)
        # self.text_for_input.setText(QCoreApplication.translate("MainWindow", u"\u044b\u043e\u043f \u0434\u043b\u044b\u0432\u043e \u0434\u043b\u043e\u0430\u0434\u043b \u043f\u043e\u043b\u043e \u044b\u0434\u043f\u043b\u0432\u0440\u0434\u043e\u044b \u0443\u043a\u0440\u0434\u043b\u043f\u043e\u044b\u0434\u043b\u0430 \u043f\u043e\u044b\u043b\u0436\u043f \u0440\u0434\u043b\u0443\u043a \u043f\u0442\u0434\u043b\u044b\u043a\u0432\u043e\u043f \u0436\u0432\u0430\u043b\u043e \u043f\u0434\u043b\u043e\u044f\u0430\u0432 \u043b\u043f\u043e\u0432\u043b\u0434\u0447\u0430\u043e \u043e\u043a\u0432 \u0449\u0436\u0434\u0443\u044b\u043e\u043a \u043f\u043b\u044b\u0443\u043a\u043e\u0435 ", None))
        # self.text_for_input_printed.setText(QCoreApplication.translate("MainWindow", u"\u044b\u043e\u043f \u0434\u043b\u044b\u0432\u043e \u0434\u043b\u043e\u0430\u0434\u043b \u043f\u043e\u043b\u043e \u044b\u0434\u043f\u043b\u0432\u0440\u0434\u043e\u044b \u0443\u043a\u0440\u0434\u043b\u043f\u043e\u044b\u0434\u043b\u0430 \u043f\u043e\u044b\u043b\u0436\u043f \u0440\u0434\u043b\u0443\u043a \u043f\u0442\u0434\u043b\u044b\u043a\u0432\u043e\u043f \u0436\u0432\u0430\u043b\u043e \u043f\u0434\u043b\u043e\u044f\u0430\u0432 \u043b\u043f\u043e\u0432\u043b\u0434\u0447\u0430\u043e \u043e\u043a\u0432 \u0449\u0436\u0434\u0443\u044b\u043e\u043a \u043f\u043b\u044b\u0443\u043a\u043e\u0435 ", None))
        # self.text.setText(QCoreApplication.translate("MainWindow", u"\u044b\u043e\u043f \u0434\u043b\u044b\u0432\u043e \u0434\u043b\u043e\u0430\u0434\u043b \u043f\u043e\u043b\u043e \u044b\u0434\u043f\u043b\u0432\u0440\u0434\u043e\u044b \u0443\u043a\u0440\u0434\u043b\u043f\u043e\u044b\u0434\u043b\u0430 \u043f\u043e\u044b\u043b\u0436\u043f \u0440\u0434\u043b\u0443\u043a \u043f\u0442\u0434\u043b\u044b\u043a\u0432\u043e\u043f \u0436\u0432\u0430\u043b\u043e \u043f\u0434\u043b\u043e\u044f\u0430\u0432 \u043b\u043f\u043e\u0432\u043b\u0434\u0447\u0430\u043e \u043e\u043a\u0432 \u0449\u0436\u0434\u0443\u044b\u043e\u043a \u043f\u043b\u044b\u0443\u043a\u043e\u0435 ", None))
    # retranslateUi

