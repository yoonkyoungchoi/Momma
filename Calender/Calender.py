import sys
from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton, \
    QApplication, QCalendarWidget, QLineEdit, QPlainTextEdit
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 윈도우 설정
        self.setGeometry(300, 100, 1200, 800)  # x, y, w, h
        self.setWindowTitle('Canlendar Widget')

        # CalendarWidget 위젯 화면에 표시
        self.cal = QCalendarWidget(self)
        self.cal.setGeometry(120, 50, 970, 300)
        self.cal.setGridVisible(True)
        self.cal.selectionChanged.connect(self.calendar_change)

        # min max 기간 설정
        #self.cal.setMinimumDate(QDate(2020, 8, 25))
        #self.cal.setMaximumDate(QDate(2020, 8, 27))

        # Calendar 에서 선택한 값 표시할 QLabel
        self.calendar_label = QLabel(self)
        self.calendar_label.setGeometry(120, 370, 970, 30)
        self.calendar_label.setStyleSheet('background-color:#D3D3D3')

        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("일기를 작성해요주세용.\n")
        self.b.setGeometry(120, 420, 970, 200)

        self.setupUI()

    def setupUI(self):
        btn1 = QPushButton("저장", self)
        btn2 = QPushButton("닫기", self)
        btn1.setGeometry(450, 650, 80, 30)
        btn1.clicked.connect(QCoreApplication.instance().quit)
        btn2.setGeometry(650, 650, 80, 30)
        btn2.clicked.connect(QCoreApplication.instance().quit)

    # Calendar Open 함수
    @pyqtSlot()
    def calendar_change(self):
        cal_date = self.cal.selectedDate()
        strDate = cal_date.toString('\t\t\t\t\t\t\t\t' + 'yyyy년 ' + 'MM월 ' +'dd일')  # QDate 를 str
        self.calendar_label.setText(strDate)

    # 달력에서 현재를 선택
    @pyqtSlot()
    def select_today(self):
        # self.cal.showToday()
        # self.cal.showNextMonth()
        #self.cal.setSelectedDate(QDate())
        self.cal.currentPageChanged(self, 2022, 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())