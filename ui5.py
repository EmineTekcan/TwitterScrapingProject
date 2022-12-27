import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Pencere oluştur
        self.setWindowTitle("STALKLA")
        self.resize(400, 300)

        # QWidget oluştur ve yerleşim nesnesine ekle
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # "STALKLA" yazısı oluştur ve yerleşim nesnesine ekle
        self.title_label = QLabel("STALKLA", self)
        layout.addWidget(self.title_label)

        # Arama çubuğu oluştur ve yerleşim nesnesine ekle
        self.search_edit = QLineEdit(self)
        layout.addWidget(self.search_edit)

        # "ara" düğmesi oluştur ve yerleşim nesnesine ekle
        self.search_button = QPushButton("Ara", self)
        layout.addWidget(self.search_button)

        # Dört adet QTextEdit oluştur ve yerleşim nesnesine ekle
        self.textedit1 = QTextEdit(self)
        layout.addWidget(self.textedit1)
        self.textedit2 = QTextEdit(self)
        layout.addWidget(self.textedit2)
        self.textedit3 = QTextEdit(self)
        layout.addWidget(self.textedit3)
        self.textedit4 = QTextEdit(self)
        layout.addWidget(self.textedit4)

        # "ara" düğmesine tıklandığında çalışacak fonksiyonu bağla
        self.search_button.clicked.connect(self.on_search_button_clicked)

    def on_search_button_clicked(self):
    # Burada, arama çubuğundan alınan kelimeyi kullanarak
    # başka bir dosyadaki fonksiyonu çağırın ve csv dosyalarını alın
        #search_term = self.search_edit.text()
        # Örneğin:
        # csv1, csv2, csv3, csv4 = other_module.your_function(search_term)
        csv_1 = "Search/PositiveSentence.csv"
        csv_2 = "Search/NegativeSentence.csv"
        csv_3 = "Search/MostPositiveSentence.csv"
        csv_4 = "Search/MostNegativeSentence.csv"

        with open("Search/PositiveSentence.csv") as f:
            csv1_content = f.read()
        with open("Search/NegativeSentence.csv") as f:
            csv2_content = f.read()
        with open("Search/MostPositiveSentence.csv") as f:
            csv3_content = f.read()
        with open("Search/MostNegativeSentence.csv") as f:
            csv4_content = f.read()

        # QTextEdit nesnelerine csv dosyalarını yükleyin
        self.textedit1.setPlainText(csv1_content)
        self.textedit2.setPlainText(csv2_content)
        self.textedit3.setPlainText(csv3_content)
        self.textedit4.setPlainText(csv4_content)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

