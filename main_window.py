
import os
from deutsch_calculator import calculate_rate, resource_path

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QStringListModel)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QListView, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget, QFileDialog)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 602)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_p1 = QGroupBox(self.centralwidget)
        self.groupBox_p1.setObjectName(u"groupBox_p1")
        self.groupBox_p1.setMaximumSize(QSize(260, 16777215))
        self.groupBox_p1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox_p1)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_p1 = QLabel(self.groupBox_p1)
        self.label_p1.setObjectName(u"label_p1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_p1.sizePolicy().hasHeightForWidth())
        self.label_p1.setSizePolicy(sizePolicy)
        self.label_p1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_p1.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_p1)

        self.pushButton_p1 = QPushButton(self.groupBox_p1)
        self.pushButton_p1.setObjectName(u"pushButton_p1")
        self.pushButton_p1.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_p1.sizePolicy().hasHeightForWidth())
        self.pushButton_p1.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.pushButton_p1, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.groupBox_p1, 0, 0, 1, 1)

        self.groupBox_p2 = QGroupBox(self.centralwidget)
        self.groupBox_p2.setObjectName(u"groupBox_p2")
        self.groupBox_p2.setMaximumSize(QSize(260, 16777215))
        self.groupBox_p2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_p2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox_p2 = QComboBox(self.groupBox_p2)
        self.comboBox_p2.addItem("")
        self.comboBox_p2.addItem("")
        self.comboBox_p2.setObjectName(u"comboBox_p2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox_p2.sizePolicy().hasHeightForWidth())
        self.comboBox_p2.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.comboBox_p2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.groupBox_p2, 1, 0, 1, 1)

        self.groupBox_p7 = QGroupBox(self.centralwidget)
        self.groupBox_p7.setObjectName(u"groupBox_p7")
        self.groupBox_p7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_p7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit = QTextEdit(self.groupBox_p7)
        self.textEdit.setReadOnly(True)  # 设置为只读模式
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_2.addWidget(self.textEdit)


        self.gridLayout_2.addWidget(self.groupBox_p7, 0, 2, 5, 1)

        self.groupBox_p6 = QGroupBox(self.centralwidget)
        self.groupBox_p6.setObjectName(u"groupBox_p6")
        self.groupBox_p6.setMaximumSize(QSize(260, 16777215))
        self.groupBox_p6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_p6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listView_p6 = QListView(self.groupBox_p6)
        self.listView_p6.setObjectName(u"listView_p6")
        self.listView_p6.setMaximumSize(QSize(242, 16777215))

        self.verticalLayout_3.addWidget(self.listView_p6, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addWidget(self.groupBox_p6, 2, 1, 3, 1)

        self.groupBox_p4 = QGroupBox(self.centralwidget)
        self.groupBox_p4.setObjectName(u"groupBox_p4")
        self.groupBox_p4.setMaximumSize(QSize(260, 16777215))
        self.groupBox_p4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_p4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_p4 = QPushButton(self.groupBox_p4)
        self.pushButton_p4.setObjectName(u"pushButton_p4")
        self.pushButton_p4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton_p4.sizePolicy().hasHeightForWidth())
        self.pushButton_p4.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.pushButton_p4, 0, Qt.AlignmentFlag.AlignHCenter)

        self.gridLayout_2.addWidget(self.groupBox_p4, 4, 0, 1, 1)

        self.groupBox_p5 = QGroupBox(self.centralwidget)
        self.groupBox_p5.setObjectName(u"groupBox_p5")
        self.groupBox_p5.setMaximumSize(QSize(260, 16777215))
        self.groupBox_p5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_4 = QGridLayout(self.groupBox_p5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(40, -1, 40, -1)
        self.label_p5_1 = QLabel(self.groupBox_p5)
        self.label_p5_1.setObjectName(u"label_p5_1")

        self.gridLayout_4.addWidget(self.label_p5_1, 0, 0, 1, 1)

        self.label_p5_5 = QLabel(self.groupBox_p5)
        self.label_p5_5.setObjectName(u"label_p5_5")
        self.label_p5_5.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_p5_5, 0, 1, 1, 1)

        self.label_p5_2 = QLabel(self.groupBox_p5)
        self.label_p5_2.setObjectName(u"label_p5_2")

        self.gridLayout_4.addWidget(self.label_p5_2, 1, 0, 1, 1)

        self.label_p5_6 = QLabel(self.groupBox_p5)
        self.label_p5_6.setObjectName(u"label_p5_6")
        self.label_p5_6.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_p5_6, 1, 1, 1, 1)

        self.label_p5_3 = QLabel(self.groupBox_p5)
        self.label_p5_3.setObjectName(u"label_p5_3")

        self.gridLayout_4.addWidget(self.label_p5_3, 2, 0, 1, 1)

        self.label_p5_7 = QLabel(self.groupBox_p5)
        self.label_p5_7.setObjectName(u"label_p5_7")
        self.label_p5_7.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_p5_7, 2, 1, 1, 1)

        self.label_p5_4 = QLabel(self.groupBox_p5)
        self.label_p5_4.setObjectName(u"label_p5_4")

        self.gridLayout_4.addWidget(self.label_p5_4, 3, 0, 1, 1)

        self.label_p5_8 = QLabel(self.groupBox_p5)
        self.label_p5_8.setObjectName(u"label_p5_8")
        self.label_p5_8.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_p5_8, 3, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_p5, 0, 1, 2, 1)

        self.groupBox_p3 = QGroupBox(self.centralwidget)
        self.groupBox_p3.setObjectName(u"groupBox_p3")
        self.groupBox_p3.setMaximumSize(QSize(260, 16777215))
        self.groupBox_p3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_3 = QGridLayout(self.groupBox_p3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(30, -1, 30, -1)
        self.label_2_p3_2 = QLabel(self.groupBox_p3)
        self.label_2_p3_2.setObjectName(u"label_2_p3_2")
        sizePolicy.setHeightForWidth(self.label_2_p3_2.sizePolicy().hasHeightForWidth())
        self.label_2_p3_2.setSizePolicy(sizePolicy)
        self.label_2_p3_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2_p3_2, 1, 1, 1, 1)

        self.comboBox_p3_1 = QComboBox(self.groupBox_p3)
        self.comboBox_p3_1.addItem("")
        self.comboBox_p3_1.addItem("")
        self.comboBox_p3_1.addItem("")
        self.comboBox_p3_1.setObjectName(u"comboBox_p3_1")
        sizePolicy2.setHeightForWidth(self.comboBox_p3_1.sizePolicy().hasHeightForWidth())
        self.comboBox_p3_1.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.comboBox_p3_1, 2, 0, 1, 1)

        self.comboBox_2_p3_2 = QComboBox(self.groupBox_p3)
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.addItem("")
        self.comboBox_2_p3_2.setObjectName(u"comboBox_2_p3_2")
        sizePolicy2.setHeightForWidth(self.comboBox_2_p3_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2_p3_2.setSizePolicy(sizePolicy2)

        self.gridLayout_3.addWidget(self.comboBox_2_p3_2, 2, 2, 1, 1)

        self.label_p3_3 = QLabel(self.groupBox_p3)
        self.label_p3_3.setObjectName(u"label_p3_3")
        sizePolicy.setHeightForWidth(self.label_p3_3.sizePolicy().hasHeightForWidth())
        self.label_p3_3.setSizePolicy(sizePolicy)
        self.label_p3_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_p3_3, 0, 2, 1, 1)

        self.label_p3_1 = QLabel(self.groupBox_p3)
        self.label_p3_1.setObjectName(u"label_p3_1")
        sizePolicy.setHeightForWidth(self.label_p3_1.sizePolicy().hasHeightForWidth())
        self.label_p3_1.setSizePolicy(sizePolicy)
        self.label_p3_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_p3_1, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_p3, 2, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.comboBox_p2.setCurrentIndex(0)
        self.comboBox_p3_1.setCurrentIndex(0)
        self.comboBox_2_p3_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u751f\u8bcd\u7387\u67e5\u8be2", None))
        self.groupBox_p1.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u6b65\uff1a\u9009\u62e9\u5f85\u68c0\u6d4b\u6587\u672c\uff08.txt)", None))
        self.label_p1.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None))
        self.pushButton_p1.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6587\u4ef6", None))
        self.groupBox_p2.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u6b65\uff1a\u9009\u62e9\u6559\u6750", None))
        self.comboBox_p2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6559\u6750", None))
        self.comboBox_p2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5f53\u4ee3\u5927\u5b66\u5fb7\u8bed", None))

        self.comboBox_p2.setCurrentText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6559\u6750", None))
        self.groupBox_p7.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u672c\u663e\u793a\u533a", None))
        self.groupBox_p6.setTitle(QCoreApplication.translate("MainWindow", u"\u751f\u8bcd\u5217\u8868", None))
        self.groupBox_p4.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u56db\u6b65\uff1a\u70b9\u51fb\u6309\u94ae\uff0c\u5f00\u59cb\u68c0\u6d4b", None))
        self.pushButton_p4.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.groupBox_p5.setTitle(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u663e\u793a\u533a", None))
        self.label_p5_1.setText(QCoreApplication.translate("MainWindow", u"\u5355\u8bcd\u6570\uff1a", None))
        self.label_p5_5.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_p5_2.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u638c\u63e1\uff1a", None))
        self.label_p5_6.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_p5_3.setText(QCoreApplication.translate("MainWindow", u"\u751f\u8bcd\u6570\uff1a", None))
        self.label_p5_7.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_p5_4.setText(QCoreApplication.translate("MainWindow", u"\u751f\u8bcd\u7387\uff1a", None))
        self.label_p5_8.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.groupBox_p3.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e09\u6b65\uff1a\u9009\u62e9\u8bcd\u5e93\u8303\u56f4", None))
        self.label_2_p3_2.setText(QCoreApplication.translate("MainWindow", u"\u5230", None))
        self.comboBox_p3_1.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9", None))
        self.comboBox_p3_1.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u518c", None))
        self.comboBox_p3_1.setItemText(2, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u518c", None))

        self.comboBox_p3_1.setCurrentText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9", None))
        self.comboBox_2_p3_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9", None))
        self.comboBox_2_p3_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u8bfe", None))
        self.comboBox_2_p3_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u8bfe", None))
        self.comboBox_2_p3_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e09\u8bfe", None))
        self.comboBox_2_p3_2.setItemText(4, QCoreApplication.translate("MainWindow", u"\u7b2c\u56db\u8bfe", None))
        self.comboBox_2_p3_2.setItemText(5, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e94\u8bfe", None))
        self.comboBox_2_p3_2.setItemText(6, QCoreApplication.translate("MainWindow", u"\u7b2c\u516d\u8bfe", None))
        self.comboBox_2_p3_2.setItemText(7, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e03\u8bfe", None))
        self.comboBox_2_p3_2.setItemText(8, QCoreApplication.translate("MainWindow", u"\u7b2c\u516b\u8bfe", None))
        self.comboBox_2_p3_2.setItemText(9, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e5d\u8bfe", None))
        self.comboBox_2_p3_2.setItemText(10, QCoreApplication.translate("MainWindow", u"\u7b2c\u5341\u8bfe", None))
        self.comboBox_2_p3_2.setItemText(11, QCoreApplication.translate("MainWindow", u"\u7b2c\u5341\u4e00\u8bfe", None))
        self.comboBox_2_p3_2.setItemText(12, QCoreApplication.translate("MainWindow", u"\u7b2c\u5341\u4e8c\u8bfe", None))

        self.comboBox_2_p3_2.setCurrentText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9", None))
        self.label_p3_3.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u8bfe", None))
        self.label_p3_1.setText(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u518c", None))
    # retranslateUi


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = QStringListModel()
        self.lines = [] #词表

        #选择待检测文本
        self.pushButton_p1.clicked.connect(self.select_text_and_read_file)
        #计算册+单元
        self.comboBox_2_p3_2.activated.connect(self.select_textbook_book_lesson)
        #开始
        self.pushButton_p4.clicked.connect(self.start_calculating)
        
    #读入待检测文本
    def select_text_and_read_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "\u9009\u62e9\u8981\u5206\u6790\u7684\u6587\u672c", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            self.label_p1.setText(file_path)
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            self.textEdit.setText(text)

    
    def calculate_lesson_index(self):
        book = self.comboBox_p3_1.currentText()
        lesson = self.comboBox_2_p3_2.currentText()
        base_index = {"第一册": 0, "第二册": 12}.get(book, 0)
        lesson_index = {
            "第一课": 1, "第二课": 2, "第三课": 3, "第四课": 4,
            "第五课": 5, "第六课": 6, "第七课": 7, "第八课": 8,
            "第九课": 9, "第十课": 10, "第十一课": 11, "第十二课": 12
        }.get(lesson, 0)
        return base_index + lesson_index
    
    #读入词表（调用calculate_lesson_index）
    def select_textbook_book_lesson(self):
        textbook_folder_name = self.comboBox_p2.currentText()
        book_path = resource_path(textbook_folder_name)
        # current_directory = os.path.dirname(os.path.abspath(__file__))
        # for entry in os.listdir(current_directory):
        #     entry_path = os.path.join(current_directory, entry)
        #     if os.path.isdir(entry_path) and os.path.basename(entry_path) == textbook_folder_name:
        index = self.calculate_lesson_index()
        for i in range (1,index+1):
            with open(os.path.join(book_path, f"{i}.txt"), 'r', encoding='utf-8') as file:
                text = file.read()
            self.lines += text.split()
    

    #开始计算
    def start_calculating(self):
        vocabulary = self.lines

        text = self.textEdit.toPlainText()

        wordcount, new_word_count, known_word_count, new_word_proportion, new_words, processed_text = calculate_rate(text, vocabulary)

        self.label_p5_5.setText(str(wordcount))
        self.label_p5_6.setText(str(known_word_count))
        self.label_p5_7.setText(str(new_word_count))
        self.label_p5_8.setText(str(round(new_word_proportion*100, 2))+'%')
        self.model = QStringListModel()
        self.model.setStringList(new_words)
        self.listView_p6.setModel(self.model) 

        
        html_text = ""
        for word, flag in processed_text:
            if flag:
                html_text += f'<span style="color:red;">{word}</span> '
            else:
                html_text += f'<span style="color:black;">{word}</span> '
        self.textEdit.setHtml(html_text)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec())