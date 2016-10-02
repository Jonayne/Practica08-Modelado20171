#Código para mostrar la interfaz gráfica de nuestro Servidor.

import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#Aquí lo cargamos.
servidor_gui = uic.loadUiType("servidor.ui")[0]

class Servidor(QtGui.QMainWindow, servidor_gui):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		#Lo mismo que en el Cliente, acá hacemos que las celdas se adapten al tamaño de la TableWidget.
		self.tableWidget.horizontalHeader().setResizeMode(QHeaderView.Stretch)
		self.tableWidget.verticalHeader().setResizeMode(QHeaderView.Stretch)
		self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.tableWidget.verticalHeader().setStretchLastSection(True)
  	
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	ventana = Servidor(None)
	ventana.show()
	app.exec_()