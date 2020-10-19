import sys
from ctypes import cdll,c_char_p
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QAction,QApplication,QStyleFactory,QFileDialog
from mainwindow import *

class Testdll(Ui_MainWindow,QMainWindow):
    def __init__(self, parent=None):
        super(Testdll, self).__init__(parent)
        self.screen = QDesktopWidget().screenGeometry()
        self.width = self.screen.width()
        self.height = self.screen.height()
        self.setupUi(self)
        self.grabbutton.clicked.connect(self.camgrab)
        self.loadButton.clicked.connect(self.load)
        self.horizontalSlider.sliderMoved.connect(self.threhold)
        self.horizontalSlider_2.sliderMoved.connect(self.threhold)
        self.horizontalSlider_3.sliderMoved.connect(self.selectshapearea)
        self.horizontalSlider_4.sliderMoved.connect(self.selectshapearea)
        self.horizontalSlider_5.sliderMoved.connect(self.selectshaperoundness)
        self.horizontalSlider_6.sliderMoved.connect(self.selectshaperoundness)
        self.horizontalSlider_7.sliderMoved.connect(self.erosion)
        self.horizontalSlider_8.sliderMoved.connect(self.dilation)
        self.horizontalSlider_9.sliderMoved.connect(self.open)
        self.horizontalSlider_10.sliderMoved.connect(self.closing)
        self.EnterButton.clicked.connect(self.threhold_enter)
        self.EnterButton_2.clicked.connect(self.selectshapearea_enter)
        self.EnterButton_3.clicked.connect(self.selectshaperoundness_enter)
        self.EnterButton_4.clicked.connect(self.erosion_enter)
        self.EnterButton_5.clicked.connect(self.dilation_enter)
        self.EnterButton_6.clicked.connect(self.open_enter)
        self.EnterButton_7.clicked.connect(self.closing_enter)
        self.ConnectionButton.clicked.connect(self.connection)
        self.UnionButton.clicked.connect(self.union)
        self.enlargeButton.clicked.connect(self.enlarge)
        self.reduceButton.clicked.connect(self.reduce)

        self.mydll = cdll.LoadLibrary('dlltest.dll')
        id = int(self.winId())
        self.mydll.openwindow(id)


    def camgrab(self):
        self.mydll.grab()

    def threhold(self):
        self.mingray.setText("Min:"+str(self.horizontalSlider.value()))
        self.maxgray.setText("Max:"+str(self.horizontalSlider_2.value()))
        self.mydll.threhold(self.horizontalSlider.value(),self.horizontalSlider_2.value())
        if self.horizontalSlider.value()>self.horizontalSlider_2.value():
            self.horizontalSlider.setValue(self.horizontalSlider_2.value())

    def threhold_enter(self):
        self.mydll.threhold_enter(self.horizontalSlider.value(),self.horizontalSlider_2.value())

    def selectshapearea(self):
        self.minarea.setText("Min:"+str(self.horizontalSlider_3.value()))
        self.maxarea.setText("Max:"+str(self.horizontalSlider_4.value()))
        self.mydll.selectshapearea(self.horizontalSlider_3.value(),self.horizontalSlider_4.value())
        if self.horizontalSlider_3.value()>self.horizontalSlider_4.value():
            self.horizontalSlider_3.setValue(self.horizontalSlider_4.value())

    def selectshapearea_enter(self):
        self.mydll.selectshapearea_enter(self.horizontalSlider_3.value(),self.horizontalSlider_4.value())

    def selectshaperoundness(self):
        self.minroundness.setText("Min:"+str(self.horizontalSlider_5.value()/100))
        self.maxroundness.setText("Max:"+str(self.horizontalSlider_6.value()/100))
        self.mydll.selectshaperoundness(self.horizontalSlider_5.value(),self.horizontalSlider_6.value())
        if self.horizontalSlider_5.value()>self.horizontalSlider_6.value():
            self.horizontalSlider_5.setValue(self.horizontalSlider_6.value())

    def selectshaperoundness_enter(self):
        self.mydll.selectshaperoundness_enter(self.horizontalSlider_5.value(),self.horizontalSlider_6.value())

    def erosion(self):
        self.mydll.erosion(self.horizontalSlider_7.value())

    def erosion_enter(self):
        self.mydll.erosion_enter(self.horizontalSlider_7.value())

    def dilation(self):
        self.mydll.dilation(self.horizontalSlider_8.value())

    def dilation_enter(self):
        self.mydll.dilation_enter(self.horizontalSlider_8.value())

    def open(self):
        self.mydll.open(self.horizontalSlider_9.value())

    def open_enter(self):
        self.mydll.open_enter(self.horizontalSlider_9.value())

    def closing(self):
        self.mydll.close(self.horizontalSlider_10.value())

    def closing_enter(self):
        self.mydll.close_enter(self.horizontalSlider_10.value())

    def connection(self):
        self.mydll.connection_enter()

    def union(self):
        self.mydll.union_enter()

    def load(self):
        filename = QFileDialog.getOpenFileName(self,"open file dialog",r"C:\Users\Administrator\Desktop",r"all files(*.*)")
        filepath = filename[0]
        p = c_char_p(filepath.encode())
        self.mydll.load(p)

    def enlarge(self):
        self.mydll.enlarge()

    def reduce(self):
        self.mydll.reduce()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create("Fusion"))
    test = Testdll()
    test.show()
    sys.exit(app.exec_())