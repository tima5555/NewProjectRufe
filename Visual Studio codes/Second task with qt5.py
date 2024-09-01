from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class DiceWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Настраиваем главное окно
        self.setWindowTitle("Випробуй удачу, друже!")
        self.setGeometry(100, 100, 300, 300)

        # Создаем сеточный макет (GridLayout)
        grid = QGridLayout()

        # Создаем кнопки и добавляем их в сетку
        button1 = QPushButton("1", self)
        button2 = QPushButton("2", self)
        button3 = QPushButton("3", self)
        button4 = QPushButton("4", self)
        button5 = QPushButton("5", self)

        grid.addWidget(button1, 0, 0)  # Верхний левый угол
        grid.addWidget(button2, 0, 2)  # Верхний правый угол
        grid.addWidget(button3, 1, 1)  # Центр
        grid.addWidget(button4, 2, 0)  # Нижний левый угол
        grid.addWidget(button5, 2, 2)  # Нижний правый угол

        # Устанавливаем макет в окно
        self.setLayout(grid)

app = QApplication([])  # Создаем экземпляр приложения
window = DiceWindow()    # Создаем основное окно
window.show()            # Показываем окно
exit(app.exec_())        # Запуск главного цикла приложения
