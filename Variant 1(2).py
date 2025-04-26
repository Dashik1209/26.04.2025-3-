import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import matplotlib

matplotlib.use("Qt5Agg")  # Explicitly set the backend

class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

    def plot_graph(self, func_str, x_min, x_max):
        try:
            x = np.linspace(x_min, x_max, 500)
            y = eval(func_str)  # Use with caution! See security note below.

            self.axes.cla()  # Clear the old plot
            self.axes.plot(x, y)
            self.axes.set_xlabel("x")
            self.axes.set_ylabel("y")
            self.axes.grid(True)
            self.draw()
        except Exception as e:
            self.axes.cla()  # Clear the old plot
            self.axes.text(
                0.5,
                0.5,
                f"Ошибка: {str(e)}",
                horizontalalignment="center",
                verticalalignment="center",
                fontsize=12,
                color="red",
            )
            self.axes.set_xticks([]) # Remove x axis ticks
            self.axes.set_yticks([]) # Remove y axis ticks

            self.draw()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("График функции")

        # 2. Add elements
        self.function_label = QLabel("Формула функции (например, x**2 или np.sin(x)):")
        self.function_input = QLineEdit()
        self.xmin_label = QLabel("X min:")
        self.xmin_input = QLineEdit()
        self.xmax_label = QLabel("X max:")
        self.xmax_input = QLineEdit()
        self.plot_button = QPushButton("Построить график")
        self.plot_area = MatplotlibCanvas(self, width=8, height=6, dpi=100)

        # Layout setup
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.function_label)
        input_layout.addWidget(self.function_input)
        input_layout.addWidget(self.xmin_label)
        input_layout.addWidget(self.xmin_input)
        input_layout.addWidget(self.xmax_label)
        input_layout.addWidget(self.xmax_input)
        input_layout.addWidget(self.plot_button)

        main_layout = QHBoxLayout()
        main_layout.addLayout(input_layout)  # Input fields on the left
        main_layout.addWidget(
            self.plot_area, alignment=Qt.AlignRight
        )  # Graph area on the right

        self.setLayout(main_layout)

        # Button click event
        self.plot_button.clicked.connect(self.plot)

    def plot(self):
        # 3. Upon button click
        func_str = self.function_input.text()
        try:
            x_min = float(self.xmin_input.text())
            x_max = float(self.xmax_input.text())
        except ValueError:
            # 4. Handle input errors
            QMessageBox.critical(
                self, "Ошибка", "Некорректный ввод X min/max. Введите числа."
            )
            return

        self.plot_area.plot_graph(func_str, x_min, x_max)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())