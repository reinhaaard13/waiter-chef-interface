from wtc.queue import OrderQueue
from wtc.order import Order
from PyQt5 import QtCore, QtGui, QtWidgets

order_queue = OrderQueue()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 477)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

        # premade menu
        self.menus = ['Nasi Goreng', 'Ayam Goreng', 'Ayam Bakar', 'Udang Mayonaise', 'Cumi Goreng Tepung']
        self.menuTemplate = []
        for i, menu in enumerate(self.menus):
            self.menuTemplate.append(QtWidgets.QPushButton(menu, self.centralwidget))
            self.menuTemplate[i].setObjectName("menuTemplate")
            self.menuTemplate[i].clicked.connect(lambda checked, a=i: self.submitOrder(a))
            self.verticalLayout_2.addWidget(self.menuTemplate[i])
        
        self.orderInputLayout = QtWidgets.QHBoxLayout()
        self.orderInputLayout.setObjectName("orderInputLayout")

        self.orderLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.orderLineEdit.setObjectName("orderLineEdit")
        self.orderInputLayout.addWidget(self.orderLineEdit)

        self.orderQty = QtWidgets.QSpinBox(self.centralwidget)
        self.orderQty.setObjectName("orderQty")
        self.orderQty.setValue(1)
        self.orderInputLayout.addWidget(self.orderQty)

        self.verticalLayout_2.addLayout(self.orderInputLayout)

        self.orderSubmit = QtWidgets.QPushButton(self.centralwidget)
        self.orderSubmit.setObjectName("orderSubmit")
        self.orderSubmit.clicked.connect(lambda: self.submitOrder(-1))
        self.verticalLayout_2.addWidget(self.orderSubmit)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.orderQueueGroup = QtWidgets.QGroupBox(self.centralwidget)
        self.orderQueueGroup.setObjectName("orderQueueGroup")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.orderQueueGroup)
        self.verticalLayout.setObjectName("verticalLayout")

        self.orderQueueScrollArea = QtWidgets.QScrollArea(self.orderQueueGroup)
        self.orderQueueScrollArea.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding))
        self.orderQueueScrollArea.setWidgetResizable(True)
        self.orderQueueScrollArea.setObjectName("orderQueueScrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 209, 383))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.getAllOrder()

        self.orderQueueScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.orderQueueScrollArea)

        self.horizontalLayout_2.addWidget(self.orderQueueGroup)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)

        self.youAreMaking = QtWidgets.QLabel(self.centralwidget)
        self.youAreMaking.setObjectName("youAreMaking")
        self.verticalLayout_3.addWidget(self.youAreMaking)

        self.menuInProgressLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.menuInProgressLabel.setFont(font)
        self.menuInProgressLabel.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred))
        self.menuInProgressLabel.setWordWrap(True)
        self.menuInProgressLabel.setObjectName("menuInProgressLabel")
        self.verticalLayout_3.addWidget(self.menuInProgressLabel)

        self.menuDone = QtWidgets.QPushButton(self.centralwidget)
        self.menuDone.clicked.connect(self.doneCooking)
        self.menuDone.setObjectName("menuDone")
        self.verticalLayout_3.addWidget(self.menuDone)

        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Waiter-to-Chef Interface"))
        self.orderSubmit.setText(_translate("MainWindow", "Submit Order"))
        self.orderQueueGroup.setTitle(_translate("MainWindow", "Order Queue"))
        self.youAreMaking.setText(_translate("MainWindow", "Order In Progress"))
        self.menuInProgressLabel.setText(_translate("MainWindow", "Nothing"))
        self.menuDone.setText(_translate("MainWindow", "Mark as Done"))

    def getAllOrder(self):
        list_order = order_queue.getQueueToList()

        for order in list_order:
            if order:
                self.orderQueueItem = QtWidgets.QWidget(self.scrollAreaWidgetContents)
                self.orderQueueItem.setStyleSheet("QWidget {\n"
        "    background-color: rgb(198, 194, 200);\n"
        "    padding: 3px;\n"
        "    border-radius: 10px;\n"
        "}")
                self.orderQueueItem.setObjectName("orderQueueItem")

                self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.orderQueueItem)
                self.verticalLayout_4.setObjectName("verticalLayout_4")

                self.menuName = QtWidgets.QLabel(order.nama, self.orderQueueItem)
                font = QtGui.QFont()
                font.setPointSize(12)
                self.menuName.setFont(font)
                self.menuName.setObjectName("menuName")
                self.verticalLayout_4.addWidget(self.menuName)

                self.menuQty = QtWidgets.QLabel(order.qty, self.orderQueueItem)
                self.menuQty.setObjectName("menuQty")

                self.verticalLayout_4.addWidget(self.menuQty)

                self.verticalLayout_5.addWidget(self.orderQueueItem)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)

    def submitOrder(self,i=-1):
        if i >= 0:
            name, qty = self.menus[i], '1'
        else:
            name = self.orderLineEdit.text()
            qty = self.orderQty.text()
            self.orderLineEdit.setText('')
            self.orderQty.setValue(1)

        order_queue.enqueue(Order(name, qty))

        self.refreshOrderQueue()

    def refreshOrderQueue(self):
        for i in reversed(range(self.verticalLayout_5.count())): 
            try:
                self.verticalLayout_5.itemAt(i).widget().setParent(None)
            except AttributeError:
                self.verticalLayout_5.removeItem(self.verticalLayout_5.itemAt(i))
        
        self.getAllOrder()
        self.refreshOrderToCook()

    def refreshOrderToCook(self):
        try:
            self.menuInProgressLabel.setText(order_queue.first().nama + '\nx' + order_queue.first().qty)
        except AttributeError:
            pass
        except IndexError:
            self.menuInProgressLabel.setText("Nothing")

    def doneCooking(self):
        order_queue.dequeue()
        self.refreshOrderQueue()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    