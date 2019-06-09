from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel, QGridLayout, QSlider
import matplotlib.pylab as plt
from matplotlib.figure import Figure
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from numpy import *
import pylab as p
from PyQt5 import QtCore, QtWidgets, uic

import matplotlib
matplotlib.use('QT5Agg')

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar


def barnsley_fern(iteration_number):
    X = [0]
    Y = [0]
    for n in range(iteration_number):
        r = random.uniform(0, 100)
        if r < 1.0:
            x = 0
            y = 0.16*Y[n-1]
        elif r < 86.0:
            x = 0.85*X[n-1] + 0.04*Y[n-1]
            y = -0.04*X[n-1] + 0.85*Y[n-1]+1.6
        elif r < 93.0:
            x = 0.2*X[n-1] - 0.26*Y[n-1]
            y = 0.23*X[n-1] + 0.22*Y[n-1] + 1.6
        else:
            x = -0.15*X[n-1] + 0.28*Y[n-1]
            y = 0.26*X[n-1] + 0.24*Y[n-1] + 0.44
        X.append(x)
        Y.append(y)
    return X,Y

def sierpinski_triangle(iteration_number):
    X = [0]
    Y = [0]
    for n in range(iteration_number):
        r = random.uniform(0, 100)
        if r < 33.333:
            x = 0.5*X[n-1] - 0.5
            y = 0.5*Y[n-1] + 0.5
        elif r < 66.666:
            x = 0.5*X[n-1] - 0.5
            y = 0.5*Y[n-1] - 0.5
        else:
            x = 0.5*X[n-1] + 0.5
            y = 0.5*Y[n-1] - 0.5
        X.append(x)
        Y.append(y)
    return X,Y

def spiral(iteration_number):
    X = [0]
    Y = [0]
    for n in range(iteration_number):
        r = random.uniform(0, 100)
        if r < 89.5652:
            x = 0.787879*X[n-1] - 0.424242*Y[n-1] + 1.758647
            y = 0.242424*X[n-1] + 0.859848*Y[n-1] + 1.408065
        elif r < 94.7826:
            x = -0.121212*X[n-1] + 0.257576*Y[n-1] - 6.721654
            y = 0.151515*X[n-1] + 0.053030*Y[n-1] + 1.377236
        else:
            x = 0.181818*X[n-1] - 0.136364*Y[n-1] + 6.086107
            y = 0.090909*X[n-1] + 0.181818*Y[n-1] + 1.568035
        X.append(x)
        Y.append(y)
    return X,Y

def dragon(iteration_number):
    X = [0]
    Y = [0]
    for n in range(iteration_number):
        r = random.uniform(0, 100)
        if r < 78.7473:
            x = 0.824074*X[n-1] + 0.281428*Y[n-1] - 1.882290
            y = -0.212346*X[n-1] + 0.864198*Y[n-1] - 0.110607
        else:
            x = 0.088272*X[n-1] + 0.520988*Y[n-1] + 0.785360
            y = -0.463889*X[n-1] - 0.377778*Y[n-1] + 8.095795
        X.append(x)
        Y.append(y)
    return X,Y


def maple_leaf(iteration_number):
    X = [0]
    Y = [0]
    for n in range(iteration_number):
        r = random.uniform(0, 100)
        if r < 10:
            x = 0.14*X[n-1] + 0.01*Y[n-1] - 1.31
            y = 0.51*Y[n-1] + 0.1
        elif r < 45:
            x = 0.43*X[n-1] + 0.52*Y[n-1] + 1.49
            y = -0.45*X[n-1] + 0.5*Y[n-1] - 0.75
        elif r < 80:
            x = 0.45*X[n-1] - 0.49*Y[n-1] - 1.62
            y = 0.47*X[n-1] + 0.47*Y[n-1] - 0.74
        else:
            x = 0.49*X[n-1] + 0.02
            y = 0.51*Y[n-1] + 1.62
        X.append(x)
        Y.append(y)
    return X,Y

def tree(iteration_number):
    X = [0]
    Y = [0]
    for n in range(iteration_number):
        r = random.uniform(0, 100)
        if r < 14.2:
            x = 0.05*X[n-1] - 0.06
            y = 0.4*Y[n-1] - 0.47
        elif r < 28.4:
            x = -0.05*X[n-1] - 0.06
            y = 0.4*Y[n-1] - 0.47
        elif r < 42.6:
            x = 0.03*X[n-1] - 0.14*Y[n-1] - 0.16
            y = 0.26*Y[n-1] -0.01
        elif r < 56.8:
            x = -0.03*X[n-1] + 0.14*Y[n-1] - 0.16
            y = 0.26*Y[n-1] -0.01
        elif r < 71:
            x = 0.56*X[n-1] + 0.44*Y[n-1] + 0.3
            y = -0.37*X[n-1] + 0.51*Y[n-1] + 0.15
        elif r < 85.4:
            x = 0.19*X[n-1] + 0.07*Y[n-1] - 0.2
            y = -0.1*X[n-1] + 0.15*Y[n-1] + 0.28
        else:
            x = -0.33*X[n-1] - 0.34*Y[n-1] - 0.54
            y = -0.33*X[n-1] + 0.34*Y[n-1] + 0.39
        X.append(x)
        Y.append(y)
    return X,Y

def param_ifs_1(a, b, c, d, e, f, probability, iteration_number):
    X = [0]
    Y = [0]
    for n in range(iteration_number):
        r = random.uniform(0,100)
        if r < probability:
            x = a*X[n-1] + b*Y[n-1] + c
            y = d*X[n-1] + e*Y[n-1] + f
        else:
            x = -a*X[n-1] - b*Y[n-1] - c
            y = -d*X[n-1] - e*Y[n-1] - f
        X.append(x)
        Y.append(y)
    return X,Y


class GUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.a = 0.84
        self.b = 0.0
        self.c = 0.64
        self.d = 0.0
        self.e = 0.94
        self.f = 1.2
        self.probability = 75
        self.iterations = 100000
        self.fun = barnsley_fern
        self.interface()

    def interface(self):
        layout = QGridLayout()
        bt_layout_upper = QHBoxLayout()
        bt_layout_lower = QHBoxLayout()
        
        self.b1 = QPushButton("Barnsley Fern")
        self.b1.clicked.connect(self.handle_b1)

        self.b2 = QPushButton("Sierpinski Triangle")
        self.b2.clicked.connect(self.handle_b2)

        self.b3 = QPushButton("Tree")
        self.b3.clicked.connect(self.handle_b3)

        self.b4 = QPushButton("Maple Leaf")
        self.b4.clicked.connect(self.handle_b4)

        self.b5 = QPushButton("Spiral")
        self.b5.clicked.connect(self.handle_b5)

        self.b6 = QPushButton("Dragon")
        self.b6.clicked.connect(self.handle_b6)

        bt_layout_upper.addWidget(self.b1)
        bt_layout_upper.addWidget(self.b2)
        bt_layout_upper.addWidget(self.b3)

        bt_layout_lower.addWidget(self.b4)
        bt_layout_lower.addWidget(self.b5)
        bt_layout_lower.addWidget(self.b6)

        self.label_iter = QLabel("Number of iterations:", self)
        self.s_iter = QSlider(Qt.Horizontal)
        self.s_iter.setMinimum(1)
        self.s_iter.setMaximum(100000)
        self.s_iter.setValue(100000)
        self.s_iter.setTickInterval(1)
        self.s_iter.sliderReleased.connect(self.handle_s_iter)

        self.label1 = QLabel("a:", self)
        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(-200)
        self.s1.setMaximum(200)
        self.s1.setValue(64)
        self.s1.setTickInterval(1)
        #self.s1.sliderReleased.connect(self.handle_s1)

        self.label2 = QLabel("b:", self)
        self.s2 = QSlider(Qt.Horizontal)
        self.s2.setMinimum(-200)
        self.s2.setMaximum(200)
        self.s2.setValue(64)
        self.s2.setTickInterval(1)
        #self.s2.sliderReleased.connect(self.handle_s2)

        self.label3 = QLabel("c:", self)
        self.s3 = QSlider(Qt.Horizontal)
        self.s3.setMinimum(-200)
        self.s3.setMaximum(200)
        self.s3.setValue(75)
        self.s3.setTickInterval(1)
        #self.s3.sliderReleased.connect(self.handle_s3)

        self.label4 = QLabel("d:", self)
        self.s4 = QSlider(Qt.Horizontal)
        self.s4.setMinimum(-200)
        self.s4.setMaximum(200)
        self.s4.setValue(10)
        self.s4.setTickInterval(1)
        #self.s4.sliderReleased.connect(self.handle_s4)

        self.label5 = QLabel("e:", self)
        self.s5 = QSlider(Qt.Horizontal)
        self.s5.setMinimum(-200)
        self.s5.setMaximum(200)
        self.s5.setValue(10)
        self.s5.setTickInterval(1)
        #self.s5.sliderReleased.connect(self.handle_s5)

        self.label6 = QLabel("f:", self)
        self.s6 = QSlider(Qt.Horizontal)
        self.s6.setMinimum(-200)
        self.s6.setMaximum(200)
        self.s6.setValue(10)
        self.s6.setTickInterval(1)
        #self.s6.sliderReleased.connect(self.handle_s6)

        self.label_prob = QLabel("chance of given coefficients:", self)
        self.s_prob = QSlider(Qt.Horizontal)
        self.s_prob.setMinimum(1)
        self.s_prob.setMaximum(100)
        self.s_prob.setValue(75)
        self.s_prob.setTickInterval(1)
        #self.s_prob.sliderReleased.connect(self.handle_s_prob)

        self.b_customized = QPushButton("Apply customized IFS")
        self.b_customized.clicked.connect(self.handle_customized)

        self.fig = plt.figure()
        self.ax = plt.gca()
        self.ax.scatter(*barnsley_fern(100000), color = 'g',marker = '.', s=1)
        self.ax.relim()
        self.ax.autoscale_view()
        self.plotWidget = FigureCanvas(self.fig)
        
        layout.addLayout(bt_layout_upper, 0, 0, 1, 1)
        layout.addLayout(bt_layout_lower, 1, 0, 1, 1)

        layout.addWidget(self.label_iter)
        layout.addWidget(self.s_iter)
        layout.addWidget(self.label1)
        layout.addWidget(self.s1)
        layout.addWidget(self.label2)
        layout.addWidget(self.s2)
        layout.addWidget(self.label3)
        layout.addWidget(self.s3)
        layout.addWidget(self.label4)
        layout.addWidget(self.s4)
        layout.addWidget(self.label5)
        layout.addWidget(self.s5)
        layout.addWidget(self.label6)
        layout.addWidget(self.s6)
        layout.addWidget(self.label_prob)
        layout.addWidget(self.s_prob)
        layout.addWidget(self.b_customized)
        layout.addWidget(self.plotWidget)
        self.setLayout(layout)

        self.setGeometry(20, 20, 1000, 1000)
        self.setWindowTitle("IFS FRACTALS")
        self.show()

    def handle_b1(self):
        self.fun = barnsley_fern
        (X, Y) = self.fun(self.iterations)
        self.ax.cla()
        self.ax.scatter(X, Y, color='g', marker='.', s=1)
        self.fig.canvas.draw()
        self.fig.canvas.draw_idle()

    def handle_b2(self):
        self.fun = sierpinski_triangle
        (X, Y) = self.fun(self.iterations)
        self.ax.cla()
        self.ax.scatter(X, Y, color='b', marker='.', s=0.5)
        self.fig.canvas.draw()
        self.fig.canvas.draw_idle()

    def handle_b3(self):
        self.fun = tree
        (X, Y) = self.fun(self.iterations)
        self.ax.cla()
        self.ax.scatter(X, Y, color='g', marker='.', s=1)
        self.fig.canvas.draw()
        self.fig.canvas.draw_idle()

    def handle_b4(self):
        self.fun = maple_leaf
        (X, Y) = self.fun(self.iterations)
        self.ax.cla()
        self.ax.scatter(X, Y, color='g', marker='.', s=0.5)
        self.fig.canvas.draw()
        self.fig.canvas.draw_idle()

    def handle_b5(self):
        self.fun = spiral
        (X, Y) = self.fun(self.iterations)
        self.ax.cla()
        self.ax.scatter(X, Y, color='b', marker='.', s=1)
        self.fig.canvas.draw()
        self.fig.canvas.draw_idle()

    def handle_b6(self):
        self.fun = dragon
        (X, Y) = self.fun(self.iterations)
        self.ax.cla()
        self.ax.scatter(X, Y, color='r', marker='.', s=1)
        self.fig.canvas.draw()
        self.fig.canvas.draw_idle()

    def handle_s_iter(self):
        self.iterations = self.s_iter.value()
        try:
            (X, Y) = self.fun(self.iterations)
        except TypeError:
            (X, Y) = self.fun(self.a, self.b, self.c, self.d, self.e, self.f,
                              self.probability, self.iterations)
        self.ax.cla()
        self.ax.scatter(X, Y, marker='.', s=1)
        self.fig.canvas.draw()
        self.fig.canvas.draw_idle()

    def handle_customized(self):
        self.a = float(self.s1.value())/100.0
        self.b = float(self.s2.value())/100.0
        self.c = float(self.s3.value())/100.0
        self.d = float(self.s4.value())/100.0
        self.e = float(self.s5.value())/100.0
        self.f = float(self.s6.value())/100.0
        self.probability = self.s_prob.value()
        self.fun = param_ifs_1
        (X, Y) = self.fun(self.a, self.b, self.c, self.d, self.e, self.f,
                          self.probability, self.iterations)
        self.ax.cla()
        self.ax.scatter(X, Y, color='r', marker='.', s=1)
        self.fig.canvas.draw()
        self.fig.canvas.draw_idle()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec_())





























