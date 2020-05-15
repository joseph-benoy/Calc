from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from ui import *

class GUIForm(Ui_MainWindow):
	def __init__(self,window):
		self.setupUi(window)
		self.initOutput()
		self.oneBtn.clicked.connect(self.oneClicked)
		self.twoBtn.clicked.connect(self.twoClicked)
		self.threeBtn.clicked.connect(self.threeClicked)
		self.fourBtn.clicked.connect(self.fourClicked)
		self.fiveBtn.clicked.connect(self.fiveClicked)
		self.sixBtn.clicked.connect(self.sixClicked)
		self.sevenBtn.clicked.connect(self.sevenClicked)
		self.eightBtn.clicked.connect(self.eightClicked)
		self.nineBtn.clicked.connect(self.nineClicked)
		self.zeroBtn.clicked.connect(self.zeroClicked)
		self.factBtn.clicked.connect(self.factClicked)
		self.addBtn.clicked.connect(self.addClicked)
		self.subBtn.clicked.connect(self.subClicked)
		self.mulBtn.clicked.connect(self.mulClicked)
		self.divBtn.clicked.connect(self.divClicked)
		self.negBtn.clicked.connect(self.negClicked)
		self.pointBtn.clicked.connect(self.pointClicked)
		self.clearBtn.clicked.connect(self.clearClicked)
		self.backBtn.clicked.connect(self.backClicked)
		self.equalBtn.clicked.connect(self.equalClicked)
	def initOutput(self):
		self.result.setText('0')
		self.exp=''
	def setResult(self):
		self.result.setText(self.exp)
	def oneClicked(self):
		self.exp+='1'
		self.setResult()
	def twoClicked(self):
		self.exp+='2'
		self.setResult()
	def threeClicked(self):
		self.exp+='3'
		self.setResult()
	def fourClicked(self):
		self.exp+='4'
		self.setResult()
	def fiveClicked(self):
		self.exp+='5'
		self.setResult()
	def sixClicked(self):
		self.exp+='6'
		self.setResult()
	def sevenClicked(self):
		self.exp+='7'
		self.setResult()
	def eightClicked(self):
		self.exp+='8'
		self.setResult()
	def nineClicked(self):
		self.exp+='9'
		self.setResult()
	def zeroClicked(self):
		self.exp+='0'
		self.setResult()
	def pointClicked(self):
		self.exp+='.'
		self.setResult()
	def addClicked(self):
		self.exp+='+'
		self.setResult()
	def subClicked(self):
		self.exp+='-'
		self.setResult()
	def mulClicked(self):
		self.exp+='*'
		self.setResult()
	def divClicked(self):
		self.exp+='/'
		self.setResult()
	def factClicked(self):
		self.exp+='!'
		self.setResult()
	def negClicked(self):
		self.exp+='-'
		self.setResult()
	def pointCliked(self):
		self.exp+='.'
		self.setResult()
	def clearClicked(self):
		self.initOutput()
	def backClicked(self):
		self.exp = self.exp[:-1]
		self.setResult()
	def equalClicked(self):
		if('!' in self.exp):
			if(len(self.exp)>1):
				x = [x for x in self.exp if x.isdigit()]
				x = int(''.join(x))
				fact=1
				for i in range(1,x+1):
					fact*=i
				self.exp=str(fact)
				self.setResult()
			else:
				self.exp='1'
				self.setResult()
		else:
			try:
				self.exp = str(eval(self.exp))
				self.setResult()
			except Exception:
				QMessageBox.warning(MainWindow,'Error','Invalid operation!')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUIForm(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





