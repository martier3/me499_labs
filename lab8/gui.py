#!/usr/bin/env python3


from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QSlider
from PyQt5.QtCore import Qt


class SliderDisplay(QWidget):
    gui = None

    def __init__(self, name, low, high, initial_value, ticks=10):
        """
        Give me a name, the low and high values, and an initial value to set
        :param name: Name displayed on slider
        :param low: Minimum value slider returns
        :param high: Maximum value slider returns
        :param initial_value: Should be a value between low and high
        :param ticks: Resolution of slider - all sliders are integer/fixed number of ticks
        """
        # Save input values
        self.name = name
        self.low = low
        self.range = high - low
        self.ticks = ticks

        # I'm a widget with a text value next to a slider
        QWidget.__init__(self)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(high)
        # call back - call change_value when slider changed
        self.slider.valueChanged.connect(self.change_value)

        self.display = QLabel()
        self.set_value(initial_value)
        self.change_value()

        layout.addWidget(self.display)
        layout.addWidget(self.slider)

    # Use this to get the value between low/high
    def value(self):
        """Return the current value of the slider"""
        return self.slider.value()

    # Called when the value changes - resets text
    def change_value(self):
        if SliderDisplay.gui != None:
            SliderDisplay.gui.repaint()
        self.display.setText('{0}: {1:0.0f}'.format(self.name, self.value()))

    # Use this to change the value (does clamping)
    def set_value(self, value_f):
        value_tick = self.ticks * (value_f - self.low) / self.range
        value_tick = min(max(0, value_tick), self.ticks)
        self.slider.setValue(int(value_tick))
        self.display.setText('{0}: {1:.3f}'.format(self.name, self.value()))


class Interface(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('I am an example window')

        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)

        # A layout
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # A button
        quit_button = QPushButton('Quit')
        quit_button.clicked.connect(app.exit)

        # Slider
        slider = SliderDisplay('slider', 0, 10, 0, 500)

        # Label
        label = QLabel()

        label.setAlignment(Qt.AlignHCenter)

        # Add things to the layout
        layout.addWidget(label)
        layout.addWidget(slider)
        layout.addWidget(quit_button)

        # Add other widgets to the layout here.  Possibly other layouts.

if __name__ == '__main__':
    app = QApplication([])

    interface = Interface()

    interface.show()

    app.exec_()

