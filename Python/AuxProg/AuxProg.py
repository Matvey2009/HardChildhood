import sys
from PySide2 import QtWidgets
from modules.Main import Main

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())