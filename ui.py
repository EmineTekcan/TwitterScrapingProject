import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QTableView, QVBoxLayout, QWidget,QHeaderView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Kelime arama alanı oluşturun
        self.line_edit = QLineEdit(self)
        self.line_edit.returnPressed.connect(self.search)

        # CSV dosyalarını gösterecek tablo oluşturun
        self.table_view = QTableView(self)
        self.table_view1 = QTableView(self)
        self.table_view2 = QTableView(self)
        self.table_view3 = QTableView(self)


        # Arayüzü oluşturun
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Search:'))
        layout.addWidget(self.line_edit)
        layout.addWidget(self.table_view)
        
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('CSV Viewer')
        self.show()


    def search(self):
        file_names = ["Search/PositiveSentence.csv","Search/NegativeSentence.csv","Search/MostPositiveSentence.csv","Search/MostNegativeSentence.csv"]
        # Girilen kelimeye göre fonksiyonu çalıştırın ve üretilen CSV dosyalarını okuyun ve verileri bir tablo modeline yükleyin
        #import twitter_scraping
        #twitter_scraping.search(self.line_edit.text())
        
        data = []
        for i in range(0, 4):
            file_name = file_names[i]
            with open(file_name, 'r') as f:
                data.extend([line.split(',') for line in f.read().split('\n') if line])
            model = QStandardItemModel(len(data), len(data[0]))
        for row, row_data in enumerate(data):
            for col, col_data in enumerate(row_data):
                item = QStandardItem(col_data)
                model.setItem(row, col, item)  
            
        self.table_view.setModel(model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)     


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
