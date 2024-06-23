import sys
import PyQt5.QtWidgets as qtw
import utils.main_window.main_window as main_window


def main():
    """
    
    Calculator program that allows computation using the four
    basic operations.

    Usage:

        $ python main.py
    
    """
    app = qtw.QApplication([])
    mw = main_window.MainWindow()
    app.setStyle(qtw.QStyleFactory.create('Fusion'))
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

