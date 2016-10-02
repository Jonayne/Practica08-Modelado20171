#Código para mostrar la interfaz gráfica de un Cliente.

import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#Aquí lo cargamos.
cliente_gui = uic.loadUiType("cliente.ui")[0]

class Cliente(QtGui.QMainWindow, cliente_gui):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		#En las siguientes 5 lineas hacemos que las celdas de la TableWidget se adapten al tamaño de esta. 
		self.tableWidget.horizontalHeader().setResizeMode(QHeaderView.Stretch)
		self.tableWidget.verticalHeader().setResizeMode(QHeaderView.Stretch)
		self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #Para que no exista barra de scroll.
		self.tableWidget.horizontalHeader().setStretchLastSection(True)
		self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.tableWidget.verticalHeader().setStretchLastSection(True)
		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	ventana = Cliente(None)
	ventana.show()
	app.exec_()