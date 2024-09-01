from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel

class DiceWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Настраиваем главное окно
        self.setWindowTitle("Мови програмування")
        self.setGeometry(100, 100, 300, 300)

        # Создаем сеточный макет (GridLayout)
        grid = QGridLayout()

        # Создаем кнопки и добавляем их в сетку
        from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout

class DiceWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Настраиваем главное окно
        self.setWindowTitle("Мови програмування")
        self.setGeometry(100, 100, 300, 300)

        # Создаем сеточный макет (GridLayout)
        grid = QGridLayout()

        # Создаем текстовые метки и добавляем их в сетку
        label1 = QLabel("PHP", self)
        label2 = QLabel("Java Script", self)
        label3 = QLabel("Python", self)
        label4 = QLabel("SQL", self)
        label5 = QLabel("C++", self)
        label6 = QLabel("Pascal", self)

        grid.addWidget(label1, 0, 0)  
        grid.addWidget(label2, 0, 2)  
        grid.addWidget(label3, 1, 0)  
        grid.addWidget(label4, 2, 0)  
        grid.addWidget(label5, 2, 2)  
        grid.addWidget(label6, 1, 2)        

        # Устанавливаем макет в окно
        self.setLayout(grid)

app = QApplication([])  # Создаем экземпляр приложения
window = DiceWindow()    # Создаем основное окно
window.show()            # Показываем окно
exit(app.exec_())        # Запуск главного цикла приложения
        

        # Устанавливаем макет в окно
self.setLayout(grid)

app = QApplication([])  # Создаем экземпляр приложения
window = DiceWindow()    # Создаем основное окно
window.show()            # Показываем окно
exit(app.exec_())        # Запуск главного цикла приложения
