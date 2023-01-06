import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton, QTextEdit
from twitter_scraping import twitter_func,get_tweets,search_tweets
import time

from Search import search
import pandas as pd
#coding:uft8
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
        # Dört adet QTextEdit oluştur ve yerleşim nesnesine ekle
        self.title_label = QLabel("Positive Tweets", self)
        layout.addWidget(self.title_label)
        self.textedit1 = QTextEdit(self)
        layout.addWidget(self.textedit1)

        self.title_label = QLabel("Negative Tweets", self)
        layout.addWidget(self.title_label)
        self.textedit2 = QTextEdit(self)
        layout.addWidget(self.textedit2)

        self.title_label = QLabel("Most Positive Tweets", self)
        layout.addWidget(self.title_label)
        self.textedit3 = QTextEdit(self)
        layout.addWidget(self.textedit3)


        self.title_label = QLabel("Most Negative Tweets", self)
        layout.addWidget(self.title_label)
        self.textedit4 = QTextEdit(self)
        layout.addWidget(self.textedit4)
        # "ara" düğmesine tıklandığında çalışacak fonksiyonu bağla
        self.search_button.clicked.connect(self.on_search_button_clicked)

    def on_search_button_clicked(self):
    # Burada, arama çubuğundan alınan kelimeyi kullanarak
    # başka bir dosyadaki fonksiyonu çağırın ve csv dosyalarını alın
        twitter_func()
        time.sleep(5)
        search_term = self.search_edit.text()
        search_tweets(search_term)
        time.sleep(1)
        get_tweets()
        # Örneğin:
        # csv1, csv2, csv3, csv4 = other_module.your_function(search_term)
        
        data_words_negative = pd.read_csv("TwitterScrapingProject/datas/NegativeWordsEng.csv",index_col=0)
        column_name_negative = data_words_negative["NegativeWords"]

        data_words_positive = pd.read_csv("TwitterScrapingProject/datas/PositiveWordsEng.csv",index_col=0)
        column_name_positive = data_words_positive["PositiveWords"]

        data_tw = pd.read_csv("TwitterScrapingProject/datas/tweets.csv")
        data_tw = data_tw["Text"]
        data_negative = search.search_tw(column_name_negative,data_tw)
        NegativeSentence = pd.DataFrame(data_negative,columns=["Negative Tweets"])
        NegativeSentence.to_csv("TwitterScrapingProject/Search/NegativeSentence.csv")

        data_positive = search.search_tw(column_name_positive,data_tw)
        PositiveSentence = pd.DataFrame(data_positive,columns=["Positive Tweets"])
        PositiveSentence.to_csv("TwitterScrapingProject/Search/PositiveSentence.csv")

        data_positive_tweets = pd.read_csv("TwitterScrapingProject/Search/PositiveSentence.csv")
        data_positive_column = data_positive_tweets["Positive Tweets"]
        most_positive_tweet = search.most(data_positive_column,column_name_positive)  

        MostPositiveSentence = pd.DataFrame(most_positive_tweet,columns=["Most Positive Tweets"])
        MostPositiveSentence.to_csv("TwitterScrapingProject/Search/MostPositiveSentence.csv")


        data_negative_tweets = pd.read_csv("TwitterScrapingProject/Search/NegativeSentence.csv")
        data_negative_column = data_negative_tweets["Negative Tweets"]
        most_negative_tweet = search.most(data_negative_column,column_name_negative)  

        MostNegativeSentence = pd.DataFrame(most_negative_tweet,columns=["Most Negative Tweets"])
        MostNegativeSentence.to_csv("TwitterScrapingProject/Search/MostNegativeSentence.csv")
    


        csv_1 = "TwitterScrapingProject/Search/PositiveSentence.csv"
        csv_2 = "TwitterScrapingProject/Search/NegativeSentence.csv"
        csv_3 = "TwitterScrapingProject/Search/MostPositiveSentence.csv"
        csv_4 = "TwitterScrapingProject/Search/MostNegativeSentence.csv"

        with open(csv_1,encoding="utf-8") as f:
            csv1_content = f.read()
        with open(csv_2,encoding="utf-8") as f:
            csv2_content = f.read()
        with open(csv_3,encoding="utf-8") as f:
            csv3_content = f.read()
        with open(csv_4,encoding="utf-8") as f:
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
