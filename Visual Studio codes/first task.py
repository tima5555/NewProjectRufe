from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

def show_winner():
    num = randint(1, 100)
    text.setText("Переможець")
    winner.setText(str(num))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Генератор переможця")
main_win.resize(400, 200)

winner = QLabel("?")
text = QLabel("Натисніть, щоб дізнатися переможця")
button = QPushButton("Згенерувати")
line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(line)
button.clicked.connect(show_winner)

main_win.show()
app.exec_()