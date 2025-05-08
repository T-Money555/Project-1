from PyQt6.QtWidgets import QApplication
from logic import *

def main():
    application = QApplication([])
    window = Logic()
    window.setGeometry(0, 0, 500, 700)
    window.show()
    application.exec()

if __name__ == "__main__":
    main()