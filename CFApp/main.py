import os
import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import random as random


class OpenWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.CashLabel = QLabel(f"Money: {self.Money()}", self)
        self.CFInput = QLineEdit("500", self)
        self.CFHeads = QPushButton("Flip Heads", self)
        self.CFTails = QPushButton("Flip Tails", self)

        self.Choice = ['heads', 'tails', 'tails', 'heads', 'tails', 'heads']
        self.comchoice = random.choice(self.Choice)
        
        self.initUI()
        self.Money()
    def Money(self):
        with open("Money.txt", "r") as file:
            return float(file.read())
    def initUI(self):
        self.setWindowTitle("Gambling")
        self.setGeometry(900, 50, 500, 400)
        self.CashLabel.setStyleSheet('font: Arial;' 'font-size: 30px;')
        self.CashLabel.setGeometry(870, 50, 4000, 30)
        self.CFInput.setGeometry(750, 120, 400, 30)
        self.CFTails.setGeometry(750, 180, 190, 30)
        self.CFHeads.setGeometry(960, 180, 190, 30)

        self.CFHeads.clicked.connect(self.heads)
        self.CFTails.clicked.connect(self.tails)


    def tails(self):
        try:
            bet_amount = float(self.CFInput.text())

            current_money = self.Money()

            current_money -= bet_amount
        
            with open("Money.txt", 'w') as f:
                f.write(str(current_money))

                self.CashLabel.setText(f"Money: {current_money}")
        
        except ValueError:
            print("Invalid input. Please enter a number.")
    def heads(self):
        self.comchoice = random.choice(self.Choice)
        self.comchoice = random.choice(self.Choice)
        if self.comchoice == "heads":
            try:
                bet_amount = float(self.CFInput.text())

                current_money = self.Money()

                current_money += bet_amount
        
                with open("Money.txt", 'w') as f:
                    f.write(str(current_money))
                    self.CashLabel.setText(f"Money: {current_money}")
        
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif self.comchoice == "tails":
            try:
                bet_amount = float(self.CFInput.text())

                current_money = self.Money()

                current_money -= bet_amount
        
                with open("Money.txt", 'w') as f:
                    f.write(str(current_money))
                    self.CashLabel.setText(f"Money: {current_money}")
        
            except ValueError:
                print("Invalid input. Please enter a number.")















if __name__ == "__main__":
    App = QApplication(sys.argv)
    CFApp = OpenWindow()
    CFApp.showMaximized()
    sys.exit(App.exec_())