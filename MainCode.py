from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi
import sys
import random
import countryCapitalsDict as country_capitals_dict

numbers_list = ["1","2","3","4","5","6"]

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		loadUi("MainWindow.ui",self)
		self.Country_capital.clicked.connect(self.main_capital)
		self.Dice_roll.clicked.connect(self.roll)
		self.Marauders_map.clicked.connect(self.Marauder_sich)
		self.joke_button.clicked.connect(self.tellAJoke)

	def main_capital(self):
		widget.setCurrentIndex(1)

	def roll(self):
		widget.setCurrentIndex(2)

	def Marauder_sich(self):
		widget.setCurrentIndex(3)

	def tellAJoke(self):
		widget.setCurrentIndex(4)

class rolling_screen(QMainWindow):
	def __init__(self):
		super(rolling_screen, self).__init__()
		loadUi("diceroll.ui",self)
		self.roll_button.clicked.connect(self.diceroll)
		self.home_button.clicked.connect(self.gotohome)

	def gotohome(self):
		widget.setCurrentIndex(0)

	def diceroll(self):
		rolled = random.choice(numbers_list)
		self.rolled_text.setText("You rolled a "+rolled+"!")
		if rolled == '1':
			self.photos.setPixmap(QtGui.QPixmap("dice1.png"))
		elif rolled == "2":
			self.photos.setPixmap(QtGui.QPixmap("dice2.png"))
		elif rolled == "3":
			self.photos.setPixmap(QtGui.QPixmap("dice3.png"))
		elif rolled == "4":
			self.photos.setPixmap(QtGui.QPixmap("dice4.png"))
		elif rolled =="5":
			self.photos.setPixmap(QtGui.QPixmap("dice5.png"))
		elif rolled == "6":
			self.photos.setPixmap(QtGui.QPixmap("dice6.png"))

class capitals(QMainWindow):
	def __init__(self):
		super(capitals,self).__init__()
		loadUi("capital.ui",self)
		self.ok_button.clicked.connect(self.capital)
		self.label.adjustSize()
		self.home_button.clicked.connect(self.gotohome)

	def capital(self):
		country = self.country_box.text()
		capital = country_capitals_dict.find(country)
		self.output_label.setText(capital)
		self.output_label.adjustSize()

		if capital == None:
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Critical)
			msg.setWindowTitle("Invalid country name")
			msg.setText("The country name you have entered is invalid")
			msg.setInformativeText("Please make sure the value you have entered is the name of a country. If it is, double-check the spelling, and make sure that the first letter of each word in the name of the country is capital.")
			msg.exec_()

	def gotohome(self):
		widget.setCurrentIndex(0)

class MaraudersMap(QMainWindow):
	def __init__(self):
		super(MaraudersMap,self).__init__()
		loadUi("marauders_map.ui",self)
		self.ok_button.clicked.connect(self.tellme)
		self.home_button.clicked.connect(self.gotohome)
		self.clear_button.clicked.connect(self.mischief_managed)

	def tellme(self):
		self.output_label.setWordWrap(True)
		self.label.setPixmap(QtGui.QPixmap("marauders-map.jpg"))
		list1 = [1,2,3]
		situation_no = random.choice(list1)
		if situation_no == 1:
			self.output_label.setText("Hermione is in the library. Ron is on the quidditch pitch with Harry. Hagrid is in the garden. Flich is spying on the Weasly twins with Ms. Norris.")
		elif situation_no == 2:
			self.output_label.setText('''Hermione is in the Gryffindor common room. Harry is in the Great Hall. Ron is... not on the map? I guess he's in the room of requirement, and Snape's right behind me.
        
        	WAIT, WHAT?! 
        	"Hello, Aarik..."''')
		elif situation_no == 3:
			self.output_label.setText("Harry, Hermione, and Ron are walking across the grounds (they're quite close together, but I can't see them from the common room window...) Neville is... on the quidditch pitch, moving rather fast... (he can't be flying, could he?) and... HOLD ON!! There's a man named Peter in Ron's bed! *Runs up to check, but there's no one there* I decide that I am dreaming.")
		self.output_label.adjustSize()
	
	def mischief_managed(self):
		self.label.setPixmap(QtGui.QPixmap("marauders_map.jpg"))
		self.output_label.setText("")
	
	def gotohome(self):
		widget.setCurrentIndex(0)

class joke_screen(QMainWindow):
	def __init__(self):
		super(joke_screen,self).__init__()
		loadUi("joke.ui",self)
		self.home_button.clicked.connect(self.gotohome)
		self.one_more.clicked.connect(self.joke)
		self.output_label.setWordWrap(True)

	def joke(self):
		joke1 = '''Patient: Doctor, doctor, I broke my arm in 3 places!
Doctor: Then don't go to those 3 places!'''
		joke2 = '''Why don't koala bears hang out with other bears?
Because they dont meet the koala-fications.'''
		joke3 = '''Does anyone want to buy my old vacuum cleaner? It's just gathering dust.'''
		joke4 = '''What's Harry Potter's favorite way of getting down a hill?
Walking...
JK. Rolling'''
		joke5 = '''How should you address an alligator in a vest?
In-vest-igator'''
		joke6 = '''I got my best friend a fridge for her birthday. I can't wait to see her face light up when she opens it!!'''
		joke7 = '''What do you call a gigantic pile of kittens? 
A meow-ntain.'''
		joke8 = '''I once stayed up all night trying to figure out where the sun went. Then it dawned on me.'''
		joke9 = '''The Hokey Pokey can be tough the first time you try it. But eventually, you turn yourself around.'''
		joke10 = "I think circles are pointless."
		jokes_list = [joke1,joke2,joke3,joke4,joke5,joke6,joke7,joke8,joke9,joke10]
		joke_chosen = random.choice(jokes_list)
		self.output_label.setText(joke_chosen)
		self.output_label.adjustSize()

	def gotohome(self):
		widget.setCurrentIndex(0)

app = QApplication(sys.argv)
mainwindow = MainWindow()
capital_screen = capitals()
dice_screen = rolling_screen()
marauder = MaraudersMap()
joking = joke_screen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.addWidget(capital_screen)
widget.addWidget(dice_screen)
widget.addWidget(marauder)
widget.addWidget(joking)
widget.show()
app.exec_()

#mainwindow index = 0
#capital index = 1
#dice index = 2
#marauder's map = 3