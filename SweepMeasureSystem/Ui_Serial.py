# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\luspock\Documents\Projects\PyDrivers\SweepMeasureSystem\tools\..\serial.ui',
# licensing of 'C:\Users\luspock\Documents\Projects\PyDrivers\SweepMeasureSystem\tools\..\serial.ui' applies.
#
# Created: Thu Jan 17 11:51:36 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_SerialWindow(object):
    def setupUi(self, SerialWindow):
        SerialWindow.setObjectName("SerialWindow")
        SerialWindow.resize(856, 527)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(SerialWindow)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(SerialWindow)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnCheckSerialPort = QtWidgets.QPushButton(self.groupBox)
        self.btnCheckSerialPort.setObjectName("btnCheckSerialPort")
        self.verticalLayout_4.addWidget(self.btnCheckSerialPort)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.cbbSerialPorts = QtWidgets.QComboBox(self.groupBox)
        self.cbbSerialPorts.setObjectName("cbbSerialPorts")
        self.horizontalLayout_3.addWidget(self.cbbSerialPorts)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.cbbSerialPortBaudrate = QtWidgets.QComboBox(self.groupBox)
        self.cbbSerialPortBaudrate.setObjectName("cbbSerialPortBaudrate")
        self.cbbSerialPortBaudrate.addItem("")
        self.cbbSerialPortBaudrate.addItem("")
        self.cbbSerialPortBaudrate.addItem("")
        self.cbbSerialPortBaudrate.addItem("")
        self.cbbSerialPortBaudrate.addItem("")
        self.cbbSerialPortBaudrate.addItem("")
        self.cbbSerialPortBaudrate.addItem("")
        self.cbbSerialPortBaudrate.addItem("")
        self.cbbSerialPortBaudrate.addItem("")
        self.horizontalLayout_4.addWidget(self.cbbSerialPortBaudrate)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.cbbSerialPortDatabit = QtWidgets.QComboBox(self.groupBox)
        self.cbbSerialPortDatabit.setObjectName("cbbSerialPortDatabit")
        self.cbbSerialPortDatabit.addItem("")
        self.cbbSerialPortDatabit.addItem("")
        self.cbbSerialPortDatabit.addItem("")
        self.cbbSerialPortDatabit.addItem("")
        self.horizontalLayout_5.addWidget(self.cbbSerialPortDatabit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.cbbSerialPortParity = QtWidgets.QComboBox(self.groupBox)
        self.cbbSerialPortParity.setObjectName("cbbSerialPortParity")
        self.cbbSerialPortParity.addItem("")
        self.cbbSerialPortParity.addItem("")
        self.cbbSerialPortParity.addItem("")
        self.horizontalLayout_6.addWidget(self.cbbSerialPortParity)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.cbbSerialPortStopbit = QtWidgets.QComboBox(self.groupBox)
        self.cbbSerialPortStopbit.setObjectName("cbbSerialPortStopbit")
        self.cbbSerialPortStopbit.addItem("")
        self.cbbSerialPortStopbit.addItem("")
        self.cbbSerialPortStopbit.addItem("")
        self.horizontalLayout_7.addWidget(self.cbbSerialPortStopbit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.btnSerialStatus = QtWidgets.QPushButton(self.groupBox)
        self.btnSerialStatus.setStyleSheet("")
        self.btnSerialStatus.setText("")
        self.btnSerialStatus.setObjectName("btnSerialStatus")
        self.horizontalLayout_8.addWidget(self.btnSerialStatus)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btnSerialOpen = QtWidgets.QPushButton(self.groupBox)
        self.btnSerialOpen.setObjectName("btnSerialOpen")
        self.horizontalLayout_9.addWidget(self.btnSerialOpen)
        self.btnSerialCLose = QtWidgets.QPushButton(self.groupBox)
        self.btnSerialCLose.setObjectName("btnSerialCLose")
        self.horizontalLayout_9.addWidget(self.btnSerialCLose)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(SerialWindow)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.leSerialPortDataBytesSent = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leSerialPortDataBytesSent.sizePolicy().hasHeightForWidth())
        self.leSerialPortDataBytesSent.setSizePolicy(sizePolicy)
        self.leSerialPortDataBytesSent.setObjectName("leSerialPortDataBytesSent")
        self.horizontalLayout_10.addWidget(self.leSerialPortDataBytesSent)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.leSerialPortDataBytesReceived = QtWidgets.QLineEdit(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leSerialPortDataBytesReceived.sizePolicy().hasHeightForWidth())
        self.leSerialPortDataBytesReceived.setSizePolicy(sizePolicy)
        self.leSerialPortDataBytesReceived.setObjectName("leSerialPortDataBytesReceived")
        self.horizontalLayout_11.addWidget(self.leSerialPortDataBytesReceived)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.horizontalLayout_12.addLayout(self.verticalLayout_6)
        self.groupBox_4 = QtWidgets.QGroupBox(SerialWindow)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pteSerialPortInput = QtWidgets.QPlainTextEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pteSerialPortInput.sizePolicy().hasHeightForWidth())
        self.pteSerialPortInput.setSizePolicy(sizePolicy)
        self.pteSerialPortInput.setObjectName("pteSerialPortInput")
        self.horizontalLayout.addWidget(self.pteSerialPortInput)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbSerialPortSendHex = QtWidgets.QCheckBox(self.groupBox_3)
        self.cbSerialPortSendHex.setObjectName("cbSerialPortSendHex")
        self.verticalLayout.addWidget(self.cbSerialPortSendHex)
        self.btnSerialPortSend = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSerialPortSend.setObjectName("btnSerialPortSend")
        self.verticalLayout.addWidget(self.btnSerialPortSend)
        self.btnSerialPortSendClear = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSerialPortSendClear.setObjectName("btnSerialPortSendClear")
        self.verticalLayout.addWidget(self.btnSerialPortSendClear)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pteSerialPortReceive = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.pteSerialPortReceive.setObjectName("pteSerialPortReceive")
        self.horizontalLayout_2.addWidget(self.pteSerialPortReceive)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbSerialPortReceiveHex = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbSerialPortReceiveHex.setObjectName("cbSerialPortReceiveHex")
        self.verticalLayout_2.addWidget(self.cbSerialPortReceiveHex)
        self.btnSerialPortReceiveClear = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSerialPortReceiveClear.setObjectName("btnSerialPortReceiveClear")
        self.verticalLayout_2.addWidget(self.btnSerialPortReceiveClear)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.horizontalLayout_12.addWidget(self.groupBox_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.retranslateUi(SerialWindow)
        QtCore.QMetaObject.connectSlotsByName(SerialWindow)

    def retranslateUi(self, SerialWindow):
        SerialWindow.setWindowTitle(QtWidgets.QApplication.translate("SerialWindow", "Form", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("SerialWindow", "Serial Settings", None, -1))
        self.btnCheckSerialPort.setText(QtWidgets.QApplication.translate("SerialWindow", "Check Serial Port", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("SerialWindow", "Serial Ports", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("SerialWindow", "Baud Rate", None, -1))
        self.cbbSerialPortBaudrate.setItemText(0, QtWidgets.QApplication.translate("SerialWindow", "300", None, -1))
        self.cbbSerialPortBaudrate.setItemText(1, QtWidgets.QApplication.translate("SerialWindow", "600", None, -1))
        self.cbbSerialPortBaudrate.setItemText(2, QtWidgets.QApplication.translate("SerialWindow", "1200", None, -1))
        self.cbbSerialPortBaudrate.setItemText(3, QtWidgets.QApplication.translate("SerialWindow", "2400", None, -1))
        self.cbbSerialPortBaudrate.setItemText(4, QtWidgets.QApplication.translate("SerialWindow", "4800", None, -1))
        self.cbbSerialPortBaudrate.setItemText(5, QtWidgets.QApplication.translate("SerialWindow", "9600", None, -1))
        self.cbbSerialPortBaudrate.setItemText(6, QtWidgets.QApplication.translate("SerialWindow", "19200", None, -1))
        self.cbbSerialPortBaudrate.setItemText(7, QtWidgets.QApplication.translate("SerialWindow", "38400", None, -1))
        self.cbbSerialPortBaudrate.setItemText(8, QtWidgets.QApplication.translate("SerialWindow", "115200", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("SerialWindow", "Databit", None, -1))
        self.cbbSerialPortDatabit.setItemText(0, QtWidgets.QApplication.translate("SerialWindow", "5", None, -1))
        self.cbbSerialPortDatabit.setItemText(1, QtWidgets.QApplication.translate("SerialWindow", "6", None, -1))
        self.cbbSerialPortDatabit.setItemText(2, QtWidgets.QApplication.translate("SerialWindow", "7", None, -1))
        self.cbbSerialPortDatabit.setItemText(3, QtWidgets.QApplication.translate("SerialWindow", "8", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("SerialWindow", "Parity", None, -1))
        self.cbbSerialPortParity.setItemText(0, QtWidgets.QApplication.translate("SerialWindow", "N", None, -1))
        self.cbbSerialPortParity.setItemText(1, QtWidgets.QApplication.translate("SerialWindow", "Odd", None, -1))
        self.cbbSerialPortParity.setItemText(2, QtWidgets.QApplication.translate("SerialWindow", "Even", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("SerialWindow", "Stopbit", None, -1))
        self.cbbSerialPortStopbit.setItemText(0, QtWidgets.QApplication.translate("SerialWindow", "1", None, -1))
        self.cbbSerialPortStopbit.setItemText(1, QtWidgets.QApplication.translate("SerialWindow", "1.5", None, -1))
        self.cbbSerialPortStopbit.setItemText(2, QtWidgets.QApplication.translate("SerialWindow", "2", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("SerialWindow", "Status", None, -1))
        self.btnSerialOpen.setText(QtWidgets.QApplication.translate("SerialWindow", "Open", None, -1))
        self.btnSerialCLose.setText(QtWidgets.QApplication.translate("SerialWindow", "Close", None, -1))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("SerialWindow", "Status", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("SerialWindow", "Sent", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate("SerialWindow", "Received", None, -1))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("SerialWindow", "Message", None, -1))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("SerialWindow", "Input", None, -1))
        self.cbSerialPortSendHex.setText(QtWidgets.QApplication.translate("SerialWindow", "Send Hex", None, -1))
        self.btnSerialPortSend.setText(QtWidgets.QApplication.translate("SerialWindow", "Send", None, -1))
        self.btnSerialPortSendClear.setText(QtWidgets.QApplication.translate("SerialWindow", "Clear", None, -1))
        self.groupBox_2.setTitle(QtWidgets.QApplication.translate("SerialWindow", "Receive", None, -1))
        self.cbSerialPortReceiveHex.setText(QtWidgets.QApplication.translate("SerialWindow", "Receive Hex", None, -1))
        self.btnSerialPortReceiveClear.setText(QtWidgets.QApplication.translate("SerialWindow", "Clear", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SerialWindow = QtWidgets.QWidget()
    ui = Ui_SerialWindow()
    ui.setupUi(SerialWindow)
    SerialWindow.show()
    sys.exit(app.exec_())

