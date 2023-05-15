from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *







# -*- coding: utf-8 -*-



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 618)
        MainWindow.setMinimumSize(QSize(1200, 600))
        MainWindow.setMaximumSize(QSize(1200, 618))
        MainWindow.setBaseSize(QSize(10, 10))
        MainWindow.setStyleSheet(u"background-color: rgb(219, 219, 219);")
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1201, 91))
        self.frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: #FFFFFF;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.start_button = QPushButton(self.frame)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(20, 20, 161, 51))
        self.start_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;")
        self.en_button = QPushButton(self.frame)
        self.en_button.setObjectName(u"en_button")
        self.en_button.setGeometry(QRect(1040, 20, 61, 51))
        self.en_button.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";")
        self.stat_button = QPushButton(self.frame)
        self.stat_button.setObjectName(u"stat_button")
        self.stat_button.setGeometry(QRect(300, 20, 201, 51))
        self.stat_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;")
        self.ru_button = QPushButton(self.frame)
        self.ru_button.setObjectName(u"ru_button")
        self.ru_button.setGeometry(QRect(1120, 20, 61, 51))
        self.ru_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;")
        self.info_button = QPushButton(self.frame)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(510, 20, 211, 51))
        self.info_button.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;")
        self.difficulty_button = QPushButton(self.frame)
        self.difficulty_button.setObjectName(u"difficulty_button")
        self.difficulty_button.setGeometry(QRect(730, 20, 201, 51))
        self.difficulty_button.setStyleSheet(u"background-color: rgb(121, 216, 88);\n"
"border-radius: 20px; \n"
"font: 24pt \"MS Shell Dlg 2\";\n"
"color: #000000;")
        self.text = QLabel(self.centralwidget)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(40, 210, 1121, 381))
        self.text.setStyleSheet(u"background-color: rgb(219, 219, 219);\n"
"border: 0;\n"
"font: 50pt \"MS Shell Dlg 2\";\n"
"overflow-wrap: break-word; \n"
"color: #000000;\n"
"overflow-wrap: break-word;\n"
"\n"
"")
        self.text.setTextFormat(Qt.PlainText)
        self.text.setScaledContents(False)
        self.text.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.text.setWordWrap(True)
        self.text.setOpenExternalLinks(False)
        self.text_for_input = QLabel(self.centralwidget)
        self.text_for_input.setObjectName(u"text_for_input")
        self.text_for_input.setGeometry(QRect(40, 100, 1121, 101))
        self.text_for_input.setStyleSheet(u"background-color: rgb(219, 219, 219);\n"
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
        self.text_for_input_2 = QLabel(self.centralwidget)
        self.text_for_input_2.setObjectName(u"text_for_input_2")
        self.text_for_input_2.setGeometry(QRect(40, 100, 1121, 101))
        self.text_for_input_2.setStyleSheet(u"background-color: rgb(219, 219, 219,0);\n"
"border: 0;\n"
"font: 50pt \"MS Shell Dlg 2\"; \n"
"color: #000000;\n"
"\n"
"\n"
"")
        self.text_for_input_2.setTextFormat(Qt.PlainText)
        self.text_for_input_2.setScaledContents(False)
        self.text_for_input_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.text_for_input_2.setWordWrap(False)
        self.text_for_input_2.setOpenExternalLinks(False)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 100, 1181, 491))
        self.textBrowser.setStyleSheet(u"background-color: rgb(219, 219, 219);\n"
"border: 0;\n"
"font: 50pt \"MS Shell Dlg 2\";\n"
"overflow-wrap: break-word; \n"
"color: #000000;\n"
"overflow-wrap: break-word;\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

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
        self.text.setText(QCoreApplication.translate("MainWindow", u"\u044b\u043e\u043f \u0434\u043b\u044b\u0432\u043e \u0434\u043b\u043e\u0430\u0434\u043b \u043f\u043e\u043b\u043e \u044b\u0434\u043f\u043b\u0432\u0440\u0434\u043e\u044b \u0443\u043a\u0440\u0434\u043b\u043f\u043e\u044b\u0434\u043b\u0430 \u043f\u043e\u044b\u043b\u0436\u043f \u0440\u0434\u043b\u0443\u043a \u043f\u0442\u0434\u043b\u044b\u043a\u0432\u043e\u043f \u0436\u0432\u0430\u043b\u043e \u043f\u0434\u043b\u043e\u044f\u0430\u0432 \u043b\u043f\u043e\u0432\u043b\u0434\u0447\u0430\u043e \u043e\u043a\u0432 \u0449\u0436\u0434\u0443\u044b\u043e\u043a \u043f\u043b\u044b\u0443\u043a\u043e\u0435 ", None))
        self.text_for_input.setText(QCoreApplication.translate("MainWindow", u"\u044b\u043e\u043f \u0434\u043b\u044b\u0432\u043e \u0434\u043b\u043e\u0430\u0434\u043b \u043f\u043e\u043b\u043e \u044b\u0434\u043f\u043b\u0432\u0440\u0434\u043e\u044b \u0443\u043a\u0440\u0434\u043b\u043f\u043e\u044b\u0434\u043b\u0430 \u043f\u043e\u044b\u043b\u0436\u043f \u0440\u0434\u043b\u0443\u043a \u043f\u0442\u0434\u043b\u044b\u043a\u0432\u043e\u043f \u0436\u0432\u0430\u043b\u043e \u043f\u0434\u043b\u043e\u044f\u0430\u0432 \u043b\u043f\u043e\u0432\u043b\u0434\u0447\u0430\u043e \u043e\u043a\u0432 \u0449\u0436\u0434\u0443\u044b\u043e\u043a \u043f\u043b\u044b\u0443\u043a\u043e\u0435 ", None))
        self.text_for_input_2.setText(QCoreApplication.translate("MainWindow", u"\u044b\u043e\u043f \u0434\u043b\u044b\u0432\u043e \u0434\u043b\u043e\u0430\u0434\u043b \u043f\u043e\u043b\u043e \u044b\u0434\u043f\u043b\u0432\u0440\u0434\u043e\u044b \u0443\u043a\u0440\u0434\u043b\u043f\u043e\u044b\u0434\u043b\u0430 \u043f\u043e\u044b\u043b\u0436\u043f \u0440\u0434\u043b\u0443\u043a \u043f\u0442\u0434\u043b\u044b\u043a\u0432\u043e\u043f \u0436\u0432\u0430\u043b\u043e \u043f\u0434\u043b\u043e\u044f\u0430\u0432 \u043b\u043f\u043e\u0432\u043b\u0434\u0447\u0430\u043e \u043e\u043a\u0432 \u0449\u0436\u0434\u0443\u044b\u043e\u043a \u043f\u043b\u044b\u0443\u043a\u043e\u0435 ", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">5) \u0427\u0442\u043e\u0431\u044b \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043d\u0430\u0431\u043e\u0440 \u0441\u043b\u043e\u0432 - \u043f\u043e\u0432\u0442\u043e\u0440\u0438\u0442\u0435 \u0448\u0430\u0433\u0438 1-3 \u0434\u0430\u043d\u043d\u043e\u0433\u043e \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u0430.</span></p>\n"
"<p style=\"-qt-"
                        "paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:28pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:28pt;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:28pt;\"><br /></p></body></html>", None))
    # retranslateUi

