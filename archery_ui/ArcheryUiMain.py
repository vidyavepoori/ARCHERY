###### _____________ARCHARY PROJECT________________######
# Author List:		[ vidya vepoori, niklesh]
# Filename:			ArcheryUiMain.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from MainUi import Ui_MainWindow
from archeryMain import *


class MainWindow:

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.TitlePg)
        self.ui.LoginBtn_1.clicked.connect(self.go_to_loginPg)
        self.ui.quit_1.clicked.connect(self.Quit)

    def go_to_TitlePg(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.TitlePg)

    def go_to_loginPg(self):
        self.ui.stackedWidget.showFullScreen()
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPg)
        self.ui.passwordBox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.back_2.clicked.connect(self.go_to_TitlePg)
        self.ui.quit_2.clicked.connect(self.Quit)
        self.ui.LoginBtn2.clicked.connect(self.go_to_LevelPg)

    def go_to_LevelPg(self):

        login_id = self.ui.loginBox.text()
        password = self.ui.passwordBox.text()
        
        print(password)

        if len(password) != 5 or len(password) == 0:
            self.ui.l_error_1.setText("*Please input all Fields")

        if password == "12345":

            self.ui.stackedWidget.setCurrentWidget(self.ui.LevelPg)
            self.ui.quit_3.clicked.connect(self.Quit)
            self.ui.b_national.clicked.connect(self.go_to_MatchPg)
            self.ui.b_state.clicked.connect(self.go_to_MatchPg)
            self.ui.b_district.clicked.connect(self.go_to_MatchPg)
            self.ui.b_training.clicked.connect(self.go_to_TraningPg)

    def go_to_MatchPg(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.MatchPg)
        self.ui.back_4.clicked.connect(self.go_to_LevelPg)
        self.ui.quit_4.clicked.connect(self.Quit)
        self.ui.b_next_1.clicked.connect(self.go_to_nextPg)

    def go_to_nextPg(self):

        distance = self.ui.distanceBox.text()
        shorts = self.ui.shortBox.text()
        rb_dual = self.ui.rb_dual.isChecked()
        rb_single = self.ui.rb_single.isChecked()

        if distance.isdigit() == True and shorts.isdigit() == True:
            if (rb_dual == True and rb_single == False):
                self.go_to_dualPg()
            if (rb_dual == False and rb_single == True):
                self.go_to_singlepg()

        else:
            self.ui.l_error_2.setText("*Please enter a intger value")

    def go_to_dualPg(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.DualPg)
        self.ui.back_5.clicked.connect(self.go_to_MatchPg)
        self.ui.quit_5.clicked.connect(self.Quit)
        self.ui.StartBtn_1.clicked.connect(self.go_to_D_StartPg)

    def go_to_D_StartPg(self):

        player1 = self.ui.player1Box_1.text()
        player2 = self.ui.player2Box_1.text()
        country = self.ui.countryBox_1.text()

        if len(player1) != 0 and len(player2) != 0 and len(country) != 0:
            self.go_to_StartPg()

        else:
            self.ui.l_error.setText("*Please enter value")

    def go_to_singlepg(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.SinglePg)
        self.ui.back_6.clicked.connect(self.go_to_MatchPg)
        self.ui.quit_6.clicked.connect(self.Quit)
        self.ui.StartBtn_2.clicked.connect(self.go_to_S_StartPg)

    def go_to_S_StartPg(self):

        player1 = self.ui.player1Box_2.text()
        country = self.ui.countryBox_2.text()

        if len(player1) != 0 and len(country) != 0:

            self.go_to_StartPg()

        else:
            self.ui.l_error_4.setText("*Please enter value")

    def go_to_TraningPg(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.TrainingPg)
        self.ui.back_7.clicked.connect(self.go_to_LevelPg)
        self.ui.quit_7.clicked.connect(self.Quit)
        self.ui.b_next_2.clicked.connect(self.go_to_T_StartPg)

    def go_to_T_StartPg(self):

        distance = self.ui.distance_field_2.text()
        shorts = self.ui.short_field_2.text()
        if distance.isdigit() == True and shorts.isdigit() == True:
            self.go_to_StartPg()
        else:
            self.ui.l_error_5.setText("*Please enter intger value")

    def go_to_StartPg(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.StartPg)
        self.ui.back_8.clicked.connect(self.go_to_LevelPg)
        self.ui.quit_8.clicked.connect(self.Quit)
        self.ui.StartBtn2.clicked.connect(self.ArcheryMain)
        self.ui.Score_btn.clicked.connect(self.go_to_ScorePg)

    def go_to_ScorePg(self):

        self.ui.stackedWidget.setCurrentWidget(self.ui.ScorePg)
        self.ui.back_9.clicked.connect(self.go_to_LevelPg)
        self.ui.quit_9.clicked.connect(self.Quit)

    def ArcheryMain(self):

        self.archerymain = ArcheryPage()
        self.mainwindow = MainWindow(self.archerymain)
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.mainwindow)
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)

    def show(self):
        self.main_win.show()

    def Quit(self):
        sys.exit(app.exec())


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
