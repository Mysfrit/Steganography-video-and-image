import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMessageBox, QApplication, QLineEdit, QMainWindow

import SteganoImage

import SteganoVideo

inputPath = ""
outputPath = ""


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 734)
        MainWindow.setMinimumSize(QtCore.QSize(1108, 734))
        MainWindow.setMaximumSize(QtCore.QSize(1108, 734))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("SA.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgb(222, 1, 84), stop:0 rgb(165, 1, 50));\n"
            "color: rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(".QLabel{\n"
                                         "background-color: transparent;\n"
                                         "font-size: 11px;\n"
                                         "font-weight: bold;\n"
                                         "}\n"
                                         "\n"
                                         ".QTextEdit{\n"
                                         "background-color: transparent;\n"
                                         "border: 3px solid white;\n"
                                         "border-radius: 10px;\n"
                                         "padding: 3px;\n"
                                         "}\n"
                                         "\n"
                                         ".QPushButton{\n"
                                         " background-color: transparent;\n"
                                         "  color: rgb(255, 255, 255);\n"
                                         "  border: 2px solid white;\n"
                                         "  text-align: center;\n"
                                         "  font-size: 11px;\n"
                                         "  border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         ".QPushButton:hover{\n"
                                         "  background-color: transparent; \n"
                                         "  color: rgb(255, 255, 255);\n"
                                         "  border-top: 1px solid rgb(151, 151, 151); \n"
                                         "  border-left: 1px solid rgb(151, 151, 151);\n"
                                         "  border-bottom: 1px solid rgb(151, 151, 151);\n"
                                         "  border-right: 1px solid rgb(151, 151, 151);\n"
                                         "  text-align: center;\n"
                                         "  font-size: 11px;\n"
                                         "  border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         ".QPushButton:pressed{\n"
                                         "  background-color: transparent;\n"
                                         "  color: rgb(255, 255, 255);\n"
                                         "  border-top: 1px solid rgb(109, 109, 109);\n"
                                         "  border-left: 1px solid rgb(109, 109, 109);\n"
                                         "  border-bottom: 1px solid rgb(109, 109, 109);\n"
                                         "  border-right: 1px solid rgb(109, 109, 109);\n"
                                         "  text-align: center;\n"
                                         "  font-size: 11px;\n"
                                         "  border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         ".QComboBox{\n"
                                         "  color: rgb(255, 255, 255);\n"
                                         "  background-color: transparent;\n"
                                         "  border: 2px solid white;\n"
                                         "  border-radius: 10px;\n"
                                         "  padding: 0px 0px 0px 4px;\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         ".QComboBox::drop-down{\n"
                                         "  \n"
                                         "  background-color: transparent;\n"
                                         "  border: 0px;\n"
                                         "  border-radius: 6px;\n"
                                         "}\n"
                                         "\n"
                                         ".QComboBox::down-arrow{ \n"
                                         "  image: url(white-down-arrow-png-2.png);\n"
                                         "  height: 13px;\n"
                                         "  width: 13px;\n"
                                         "  padding: 0px 5px 0px 0px;\n"
                                         "}\n"
                                         "\n"
                                         ".QLineEdit{\n"
                                         "  background-color: transparent;\n"
                                         "  border: 2px solid white;\n"
                                         "  border-radius: 10px;\n"
                                         "}\n"
                                         "\n"
                                         ".QFrame{\n"
                                         " background-color: transparent;\n"
                                         "  border: 2px solid white;\n"
                                         "  border-radius: 10px;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")
        self.inputFile_Button = QtWidgets.QPushButton(self.centralwidget)
        self.inputFile_Button.setGeometry(QtCore.QRect(50, 200, 341, 41))
        self.inputFile_Button.setObjectName("inputFile_Button")
        self.inputFile_Button.clicked.connect(self.inputFileLoad)
        self.outputFile_Button = QtWidgets.QPushButton(self.centralwidget)
        self.outputFile_Button.setGeometry(QtCore.QRect(50, 290, 341, 41))
        self.outputFile_Button.setObjectName("outputFile_Button")
        self.outputFile_Button.clicked.connect(self.outputFileLoad)
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(40, 250, 101, 31))
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.messageLabel = QtWidgets.QLabel(self.centralwidget)
        self.messageLabel.setGeometry(QtCore.QRect(20, 380, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.messageLabel.setFont(font)
        self.messageLabel.setObjectName("messageLabel")
        self.messageText_TextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.messageText_TextEdit.setGeometry(QtCore.QRect(10, 410, 421, 231))
        # self.messageText_TextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.messageText_TextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messageText_TextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.messageText_TextEdit.setObjectName("messageText_TextEdit")
        self.messageText_TextEdit.textChanged.connect(self.changedText)
        self.inputType_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.inputType_comboBox.setGeometry(QtCore.QRect(200, 90, 131, 21))
        self.inputType_comboBox.setObjectName("inputType_comboBox")
        self.inputType_comboBox.addItem("")
        self.inputType_comboBox.setItemText(0, "")
        self.inputType_comboBox.addItem("")
        self.inputType_comboBox.currentTextChanged.connect(self.changeType)
        self.operation_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.operation_comboBox.setGeometry(QtCore.QRect(200, 120, 131, 21))
        self.operation_comboBox.setObjectName("operation_comboBox")
        self.operation_comboBox.addItem("")
        self.operation_comboBox.setItemText(0, "")
        self.operation_comboBox.addItem("")
        self.operation_comboBox.currentTextChanged.connect(self.changeOperation)
        self.chooseTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseTypeLabel.setGeometry(QtCore.QRect(50, 90, 151, 16))
        self.chooseTypeLabel.setAutoFillBackground(False)
        self.chooseTypeLabel.setObjectName("chooseTypeLabel")
        self.chooseOperationLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseOperationLabel.setGeometry(QtCore.QRect(50, 120, 131, 16))
        self.chooseOperationLabel.setObjectName("chooseOperationLabel")
        self.passwordInput_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput_lineEdit.setGeometry(QtCore.QRect(140, 250, 251, 31))
        self.passwordInput_lineEdit.setStyleSheet("padding: 0px 0px 0px 4px;")
        self.passwordInput_lineEdit.setObjectName("passwordInput_lineEdit")
        self.passwordInput_lineEdit.setEchoMode(QLineEdit.Password)
        self.underLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.underLabel2.setGeometry(QtCore.QRect(10, 70, 421, 91))
        self.underLabel2.setStyleSheet("border: 3px solid white;\n"
                                       "border-radius: 10px;\n"
                                       "background-color: rgb(165, 1, 50);\n"
                                       "")
        self.underLabel2.setText("")
        self.underLabel2.setObjectName("underLabel2")
        self.underLabel3 = QtWidgets.QLabel(self.centralwidget)
        self.underLabel3.setGeometry(QtCore.QRect(10, 180, 421, 171))
        self.underLabel3.setStyleSheet("border: 3px solid white;\n"
                                       "border-radius: 10px;\n"
                                       "background-color: rgb(165, 1, 50);\n"
                                       "")
        self.underLabel3.setText("")
        self.underLabel3.setObjectName("underLabel3")
        self.underLabel5 = QtWidgets.QLabel(self.centralwidget)
        self.underLabel5.setGeometry(QtCore.QRect(10, 370, 421, 271))
        self.underLabel5.setStyleSheet("border: 3px solid white;\n"
                                       "border-radius: 10px;\n"
                                       "background-color: rgb(165, 1, 50);\n"
                                       "")
        self.underLabel5.setText("")
        self.underLabel5.setObjectName("underLabel5")
        self.logoTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoTextLabel.setGeometry(QtCore.QRect(10, 10, 421, 41))
        self.logoTextLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logoTextLabel.setAutoFillBackground(False)
        self.logoTextLabel.setStyleSheet("font-size: 17px;\n"
                                         "border: 3px solid white;\n"
                                         "border-radius: 10px;\n"
                                         "background-color: rgb(165, 1, 50);\n"
                                         "")
        self.logoTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logoTextLabel.setObjectName("logoTextLabel")
        self.encodeDecode_Button = QtWidgets.QPushButton(self.centralwidget)
        self.encodeDecode_Button.setGeometry(QtCore.QRect(10, 660, 421, 61))
        self.encodeDecode_Button.setObjectName("encodeDecode_Button")
        self.encodeDecode_Button.setStyleSheet("background-color:rgb(165, 1, 50);")
        self.encodeDecode_Button.clicked.connect(self.encodePushButtonClick)
        self.remainingCharacters_Label = QtWidgets.QLabel(self.centralwidget)
        self.remainingCharacters_Label.setGeometry(QtCore.QRect(110, 380, 500, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.remainingCharacters_Label.setFont(font)
        self.remainingCharacters_Label.setStyleSheet("color: rgb(194, 194, 194);")
        self.remainingCharacters_Label.setObjectName("remainingCharacters_Label")
        self.origArrowLabel = QtWidgets.QLabel(self.centralwidget)
        self.origArrowLabel.setGeometry(QtCore.QRect(360, 90, 231, 131))
        self.origArrowLabel.setStyleSheet("image: url(arrow2.png);")
        self.origArrowLabel.setText("")
        self.origArrowLabel.setObjectName("origArrowLabel")
        self.modArrowLabel = QtWidgets.QLabel(self.centralwidget)
        self.modArrowLabel.setGeometry(QtCore.QRect(370, 310, 261, 151))
        self.modArrowLabel.setStyleSheet("image: url(arrow3.png);")
        self.modArrowLabel.setText("")
        self.modArrowLabel.setObjectName("modArrowLabel")
        self.origFileLabel = QtWidgets.QLabel(self.centralwidget)
        self.origFileLabel.setGeometry(QtCore.QRect(570, 20, 500, 31))
        self.origFileLabel.setObjectName("origFileLabel")
        self.modFileLabel = QtWidgets.QLabel(self.centralwidget)
        self.modFileLabel.setGeometry(QtCore.QRect(620, 370, 500, 31))
        self.modFileLabel.setObjectName("modFileLabel")
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setGeometry(QtCore.QRect(930, 40, 151, 301))
        self.logoLabel.setStyleSheet("border: 0px;\n"
                                     "border-radius: 10px;\n"
                                     "background-color: transparent;\n"
                                     "image: url(SA.png);")
        self.logoLabel.setText("")
        self.logoLabel.setObjectName("logoLabel")
        self.origImageShow_Label = QtWidgets.QLabel(self.centralwidget)
        self.origImageShow_Label.setGeometry(QtCore.QRect(570, 50, 341, 301))
        self.origImageShow_Label.setStyleSheet("border: 3px solid white;\n"
                                               "border-radius: 10px;\n"
                                               "backgroudn-color: transparent;")
        self.origImageShow_Label.setText("")
        self.origImageShow_Label.setObjectName("origImageShow_Label")
        self.modImageShow_Label = QtWidgets.QLabel(self.centralwidget)
        self.modImageShow_Label.setGeometry(QtCore.QRect(620, 400, 341, 301))
        self.modImageShow_Label.setStyleSheet("border: 3px solid white;\n"
                                              "border-radius: 10px;\n"
                                              "backgroudn-color: transparent;")
        self.modImageShow_Label.setText("")
        self.modImageShow_Label.setObjectName("modImageShow_Label")
        self.logoTextLabel.raise_()
        self.underLabel5.raise_()
        self.underLabel3.raise_()
        self.underLabel2.raise_()
        self.inputFile_Button.raise_()
        self.outputFile_Button.raise_()
        self.password_label.raise_()
        self.messageLabel.raise_()
        self.messageText_TextEdit.raise_()
        self.inputType_comboBox.raise_()
        self.operation_comboBox.raise_()
        self.chooseTypeLabel.raise_()
        self.chooseOperationLabel.raise_()
        self.passwordInput_lineEdit.raise_()
        self.encodeDecode_Button.raise_()
        self.remainingCharacters_Label.raise_()
        self.origArrowLabel.raise_()
        self.modArrowLabel.raise_()
        self.origFileLabel.raise_()
        self.modFileLabel.raise_()
        self.logoLabel.raise_()
        self.origImageShow_Label.raise_()
        self.modImageShow_Label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.constructionLabel = QtWidgets.QLabel(self.centralwidget)
        self.constructionLabel.setGeometry(QtCore.QRect(0, 173, 1108, 561))
        self.constructionLabel.setObjectName("constructionLabel")
        self.constructionLabel.raise_()
        self.constructionLabel.setVisible(False)
        pixmap = QPixmap("WIP.png")
        self.constructionLabel.setPixmap(pixmap)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SteganApp v2.0"))
        self.inputFile_Button.setText(_translate("MainWindow", "INPUT FILE"))
        self.outputFile_Button.setText(_translate("MainWindow", "OUTPUT FILE"))
        self.password_label.setText(_translate("MainWindow", "PASSWORD"))
        self.messageLabel.setText(_translate("MainWindow", "MESSAGE:"))
        self.messageText_TextEdit.setHtml(_translate("MainWindow",
                                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"))

        self.inputType_comboBox.setItemText(0, _translate("MainWindow", "Image (.png/.jpg)"))
        self.inputType_comboBox.setItemText(1, _translate("MainWindow", "Video (.mp4)"))
        self.operation_comboBox.setItemText(0, _translate("MainWindow", "Encode"))
        self.operation_comboBox.setItemText(1, _translate("MainWindow", "Decode"))
        self.chooseTypeLabel.setText(_translate("MainWindow", "Choose a type of a input"))
        self.chooseOperationLabel.setText(_translate("MainWindow", "Choose an operation"))
        self.logoTextLabel.setText(_translate("MainWindow", "SteganApp - Beta v2.0"))
        self.encodeDecode_Button.setText(_translate("MainWindow", "ENCODE"))
        self.remainingCharacters_Label.setText(
            _translate("MainWindow", "(Remaining amount of possible characters: ___)"))
        self.origFileLabel.setText(_translate("MainWindow", "INPUT FILE:"))
        self.modFileLabel.setText(_translate("MainWindow", "MODIFIED FILE:"))
        self.constructionLabel.setText(_translate("MainWindow", ""))

    def changeOperation(self):
        if self.operation_comboBox.currentText().__contains__("Decode"):
            self.outputFile_Button.setEnabled(False)
            self.outputFile_Button.setVisible(False)
            self.modImageShow_Label.setVisible(False)
            self.modFileLabel.setVisible(False)
            self.modArrowLabel.setVisible(False)
            self.outputFile_Button.setEnabled(False)
            self.outputFile_Button.setVisible(False)
            self.modImageShow_Label.setVisible(False)
            self.encodeDecode_Button.setText("DECODE")
            self.messageText_TextEdit.setText("")
            self.passwordInput_lineEdit.setText("")
            self.messageText_TextEdit.setTextInteractionFlags(Qt.NoTextInteraction)
        else:
            self.outputFile_Button.setEnabled(True)
            self.outputFile_Button.setVisible(True)
            self.modImageShow_Label.setVisible(True)
            self.modArrowLabel.setVisible(True)

            self.outputFile_Button.setEnabled(True)
            self.outputFile_Button.setVisible(True)
            self.modImageShow_Label.setVisible(True)
            self.modFileLabel.setVisible(True)
            self.encodeDecode_Button.setText("ENCODE")
            self.messageText_TextEdit.setText("")
            self.passwordInput_lineEdit.setText("")
            self.messageText_TextEdit.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)
            if self.operation_comboBox.currentText().__contains__("Encode") and self.inputType_comboBox.currentText().__contains__("mp4"):
                self.modImageShow_Label.setVisible(False)

    def changeType(self):
        if self.inputType_comboBox.currentText().__contains__("mp4"):
            self.modFileLabel.setGeometry(620, 440, 341, 31)
            self.origFileLabel.setGeometry(570, 80, 341, 31)

            self.origImageShow_Label.setVisible(False)
            self.modImageShow_Label.setVisible(False)
            self.remainingCharacters_Label.setVisible(False)
        else:
            self.origFileLabel.setGeometry(570, 20, 341, 31)
            self.modFileLabel.setGeometry(620, 370, 341, 31)

            self.origImageShow_Label.setVisible(True)
            self.modImageShow_Label.setVisible(True)
            self.remainingCharacters_Label.setVisible(True)

    def changedText(self):
        try:
            global inputPath
            if inputPath != "" and not self.inputType_comboBox.currentText().__contains__("mp4"):
                xxx = int(SteganoImage.imageMaxCharInfo(inputPath)) - len(self.messageText_TextEdit.toPlainText())

                self.remainingCharacters_Label.setText(
                    f"(Remaining amount of possible characters: {xxx})")
        except Exception as e:
            print(e)

    def inputFileLoad(self):
        if self.inputType_comboBox.currentText().__contains__("Image"):

            if self.operation_comboBox.currentText() == "Decode":
                fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(),
                                                                    'PNG (*.png)')

            else:
                fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(),
                                                                    'JPG (*.jpg);;PNG (*.png)')
        elif self.operation_comboBox.currentText().__contains__("Encode"):
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(),
                                                                'MP4 *.mp4')
            self.origFileLabel.setText(f"INPUT FILE: {fileName}")
        else:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(),
                                                                'MOV *.mov')
            self.origFileLabel.setText(f"INPUT FILE: {fileName}")


        global inputPath
        print(fileName)
        inputPath = fileName

        try:
            if fileName != "" and not self.inputType_comboBox.currentText().__contains__("mp4"):
                pixmap = QPixmap(fileName)

                self.remainingCharacters_Label.setText(
                    f"(Remaining amount of possible characters: {SteganoImage.imageMaxCharInfo(fileName)})")
                pixmap = pixmap.scaled(341, 301, Qt.KeepAspectRatio)
                self.origImageShow_Label.setPixmap(pixmap)
                self.origImageShow_Label.adjustSize()
                self.origFileLabel.setText(f"INPUT FILE: {fileName}")
        except Exception as e:
            print(e)

    def outputFileLoad(self):
        if self.inputType_comboBox.currentText().__contains__("Image"):
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Single File', QtCore.QDir.rootPath(),
                                                                'PNG (*.png)')
            self.modFileLabel.setText(f"MODIFIED FILE: {fileName}")
        else:
            fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Single File', QtCore.QDir.rootPath(),
                                                                'MOV (*.mov)')
            self.modFileLabel.setText(f"MODIFIED FILE: {fileName}")

        global outputPath
        outputPath = fileName
        self.modFileLabel.setText(f"MODIFIED FILE: {fileName}")
        print(outputPath)

    # Zasifruje spravu do obrazku
    def encodePushButtonClick(self):
        global inputPath
        global outputPath
        try:
            if self.operation_comboBox.currentText().__contains__("Decode"):
                self.decodePushButtonClick()
                return
            error_dialog = QMessageBox()
            error_dialog.setWindowIcon(QIcon("SA.png"))
            error_dialog.setWindowTitle("Error of the file")
            error_dialog.setIcon(QMessageBox.Critical)

            if self.inputType_comboBox.currentText().__contains__("mp4"):
                try:
                    SteganoVideo.videoEncode(inputPath,
                                             outputPath,
                                             self.messageText_TextEdit.toPlainText(),
                                             self.passwordInput_lineEdit.text())
                except OverflowError:
                    error_dialog.setWindowTitle("Message overflow")
                    error_dialog.setText("Your message is too big step-bro.")
                    error_dialog.exec()
                    return

            elif inputPath != "" and outputPath != "" and \
                    (len(self.passwordInput_lineEdit.text()) >= 5) and len(self.messageText_TextEdit.toPlainText()) > 0:
                if SteganoImage.maxMessageLen(inputPath, self.messageText_TextEdit.toPlainText()):
                    try:
                        SteganoImage.encode(inputPath,
                                            outputPath,
                                            self.messageText_TextEdit.toPlainText(),
                                            self.passwordInput_lineEdit.text())


                        pixmap = QPixmap(outputPath)
                        pixmap = pixmap.scaled(341, 301, Qt.KeepAspectRatio)
                        self.modImageShow_Label.setPixmap(pixmap)
                        self.modImageShow_Label.adjustSize()

                    except PermissionError:
                        error_dialog.setWindowTitle("Permission")
                        error_dialog.setText("You don't have permission to save file")
                        error_dialog.exec()

                    except Exception as e:
                        print(e)
                    error_dialog.setText("Encode successful")
                    error_dialog.setWindowTitle("Done")
                    error_dialog.setIcon(QMessageBox.Information)
                    error_dialog.exec()
                    return
                else:
                    error_dialog.setText("Overextension of maximal number of characters in the message")
                    error_dialog.setWindowTitle("Message too long")
                    error_dialog.exec()
            elif inputPath == "" or outputPath == "":
                error_dialog.setText("You haven't chosen path to files")
                error_dialog.exec()
                return
            elif len(self.passwordInput_lineEdit.text()) < 5:
                error_dialog.setText("Forgotten password or failure due to short password")
                error_dialog.setWindowTitle("Wrong password")
                error_dialog.exec()
                return
            elif len(self.messageText_TextEdit.toPlainText()) == 0:
                error_dialog.setText("Enter text for Encode")
                error_dialog.setWindowTitle("Missing text")
                error_dialog.exec()
                return
        except Exception as e:
            print(e)

    # Desifruje spravu z obrazku
    def decodePushButtonClick(self):
        global inputPath
        print(self.passwordInput_lineEdit.text())
        error_dialog = QMessageBox()
        error_dialog.setWindowIcon(QIcon("SA.png"))
        error_dialog.setIcon(QMessageBox.Critical)
        if inputPath != "":
            try:
                if self.inputType_comboBox.currentText().__contains__("mp4"):
                    self.messageText_TextEdit.setPlainText(SteganoVideo.videoDecode(inputPath,
                                                                                    self.passwordInput_lineEdit.text()))

                else:
                    self.messageText_TextEdit.setPlainText(SteganoImage.decodeFromImage(inputPath,
                                                                                        self.passwordInput_lineEdit.text()))
            except Exception as e:
                print(e)
                error_dialog.setText("Wrong password")
                error_dialog.setWindowTitle("Wrong password")
                error_dialog.exec()
        else:
            error_dialog.setText("File missing")
            error_dialog.setWindowTitle("Failure of the file")
            error_dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Gui()
    sys.exit(app.exec_())
