#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


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

if __name__ == '__main__':
    app = QApplication([])

    slider = SliderDisplay('Magnitude', low=0, high=2000, ticks=1000, units='dB')

    slider.show()

    app.exec_()

