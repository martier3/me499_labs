#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, QLabel, QLineEdit
from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib as plt
import numpy as np
from numpy import sin
import math


class SliderDisplay(QWidget):
    gui = None
    def __init__(self, name, low, high, ticks=1000, units=''):
        QWidget.__init__(self)
        self.slider = QSlider(Qt.Horizontal)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.units = units
        self.name = name
        self.low = low
        self.high = high
        self.range = high-low
        self.ticks = ticks
        initial_value = 0

        self.slider.setMinimum(0)
        self.slider.setMaximum(ticks)
        self.slider.valueChanged.connect(self.change_value)

        self.display = QLabel()
        self.set_value(initial_value)
        self.change_value()

        layout.addWidget(self.display)
        layout.addWidget(self.slider)

    def value(self):
        """Return the current value of the slider"""
        return (self.slider.value() / self.ticks) * self.range + self.low

    def change_value(self):
        if SliderDisplay.gui != None:
            SliderDisplay.gui.repaint()
        self.display.setText('{0}: {1:.3f} {2}'.format(self.name, self.value(), self.units))

    def set_value(self, value_f):
        value_tick = self.ticks * (value_f - self.low) / self.range
        value_tick = min(max(0, value_tick), self.ticks)
        self.slider.setValue(int(value_tick))
        self.display.setText('{0}: {1:.3f}{0}'.format(self.name, self.value(), self.units))

class Grapher(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Grapher')

        # Control buttons for the interface
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        graph_button = QPushButton('Graph')
        graph_button.clicked.connect(self.graph)

        # The display for the graph
        self.figure = Figure()
        self.display = FigureCanvas(self.figure)
        self.figure.clear()

        # Amplitude Slider
        self.amplitude_slider = SliderDisplay('Amplitude', 0, 5)

        # Frequency Slider
        self.frequency_slider = SliderDisplay('Frequency', 0, 5)

        # Phase Shift Slider
        self.phaseshift_slider = SliderDisplay('Phase Shift', 0, 1)

        # User Title Input
        self.graph_title = QLineEdit()

        # The layout of the interface
        widget = QWidget()
        self.setCentralWidget(widget)

        top_level_layout = QHBoxLayout()
        widget.setLayout(top_level_layout)
        left_side_layout = QVBoxLayout()

        left_side_layout.addWidget(graph_button)
        left_side_layout.addStretch()
        left_side_layout.addWidget(QLabel('Enter Graph Title:'))
        left_side_layout.addWidget(self.graph_title)
        left_side_layout.addStretch()
        left_side_layout.addWidget(quit_button)
        left_side_layout.addWidget(self.amplitude_slider)
        left_side_layout.addWidget(self.frequency_slider)
        left_side_layout.addWidget(self.phaseshift_slider)

        top_level_layout.addLayout(left_side_layout)
        top_level_layout.addWidget(self.display)

    def graph(self):
        self.draw()

    def draw(self):
        x_range = np.arange(0, 5, 0.001)
        self.figure.clear()
        amplitude = self.amplitude_slider.value()
        frequency = self.frequency_slider.value()
        phase_shift = self.phaseshift_slider.value()
        data = amplitude * sin(2 * frequency * math.pi * (x_range - phase_shift))
        ax = self.figure.add_subplot(111)
        ax.plot(x_range, data)
        ax.set_title('{}'.format(self.graph_title.text()))
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_xlim([0, 5])
        ax.set_ylim([-5, 5])
        self.display.draw()


if __name__ == '__main__':
    app = QApplication([])

    gui = Grapher()

    gui.show()

    app.exec_()