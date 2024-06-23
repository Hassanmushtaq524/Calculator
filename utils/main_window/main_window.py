import PyQt5.QtWidgets as qtw
import utils.calculator.calculator as c

class MainWindow(qtw.QWidget):
    """
    
    Class that creates the main window in PYQT5. It adds the 
    Calculator class as its widget and uses vertical box layout.

    """
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setLayout(qtw.QVBoxLayout())
        self.setGeometry(100, 100, 400, 400)
        self.layout().addWidget(c.Calculator())
        self.show()

   
