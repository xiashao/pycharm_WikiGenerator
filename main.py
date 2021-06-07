# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import mainWindows
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit, QLabel, QPushButton, QMainWindow,QDialog



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # desk = app.desktop()
    # mc = Wiki()
    # app.exec()
    mainWindow = QMainWindow()
    ui = mainWindows.Ui_WikiGenerator()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
