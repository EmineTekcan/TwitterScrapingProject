import pandas as pd

data_words_negative = pd.read_csv("Datas/NegativeWords.csv",index_col=0)
column_name_negative = data_words_negative["NegativeWords"]

data_words_positive = pd.read_csv("Datas/PositiveWords.csv",index_col=0)
column_name_positive = data_words_positive["PositiveWords"]

data_tw = pd.read_csv("tweets.csv")
data_tw = data_tw["Text"]
#print(len(data_tw))

def search_tw(data_words,data_tw):
    liste = []
    count=0
    #data_words = data_words.values.tolist()
    #data_tw = data_tw.values.tolist()
    for x in range(0,len(data_words)):
        for y in range(0, len(data_tw)):
            word = str(data_words[x]).lower().strip()
            tweet = data_tw[y]
            tweet = str(tweet).lower().split(" ")
            for z in tweet:
                if str(z) != str(word):
                    continue
                else:
                    liste.append(data_tw[y])
                    count+=1
         
    return liste 


data_negative = search_tw(column_name_negative,data_tw)
NegativeSentence = pd.DataFrame(data_negative,columns=["Tweets"])
NegativeSentence.to_csv("NegativeSentence.csv")

data_positive = search_tw(column_name_positive,data_tw)
PositiveSentence = pd.DataFrame(data_positive,columns="Tweets")
PositiveSentence.to_csv("PositiveSentence.csv")
