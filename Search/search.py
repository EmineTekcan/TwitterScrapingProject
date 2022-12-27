import pandas as pd
"""""
data_words_negative = pd.read_csv("TwitterScrapingProject/datas/NegativeWordsEng.csv",index_col=0)
column_name_negative = data_words_negative["NegativeWords"]

data_words_positive = pd.read_csv("TwitterScrapingProject/datas/PositiveWordsEng.csv",index_col=0)
column_name_positive = data_words_positive["PositiveWords"]

data_tw = pd.read_csv("TwitterScrapingProject/datas/tweets.csv")
data_tw = data_tw["Text"]
"""


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

"""
data_negative = search_tw(column_name_negative,data_tw)
NegativeSentence = pd.DataFrame(data_negative,columns=["Tweets"])
NegativeSentence.to_csv("TwitterScrapingProject/Search/NegativeSentence.csv")

data_positive = search_tw(column_name_positive,data_tw)
PositiveSentence = pd.DataFrame(data_positive,columns=["Tweets"])
PositiveSentence.to_csv("TwitterScrapingProject/Search/PositiveSentence.csv")
"""

#Most positive and negative tweets

def most(data_tw,data_words):
    liste = []
    most_num = []
    most_tweet = []
    for x in range(0,len(data_words)):
        count = 0
        for y in range(0, len(data_tw)):
            word = str(data_words[x]).lower().strip()
            tweet = data_tw[y]
            tweet = str(tweet).lower().split(" ")
            for z in tweet:
                if str(z) != str(word):
                    continue
                else:
                    count+=1
                    most_num.append(count)

    for x in range(0,len(data_words)):
        count = 0
        for y in range(0, len(data_tw)):
            word = str(data_words[x]).lower().strip()
            tweet = data_tw[y]
            tweet = str(tweet).lower().split(" ")
            for z in tweet:
                if str(z) != str(word):
                    continue
                else:
                    count+=1
                    if count == max(most_num) and len(most_tweet) == 0:
                        most_tweet.append(data_tw[y])
                       
    return most_tweet

"""""
data_positive_tweets = pd.read_csv("TwitterScrapingProject/Search/PositiveSentence.csv")
data_positive_column = data_positive_tweets["Tweets"]
most_positive_tweet = most(data_positive_column,column_name_positive)  

MostPositiveSentence = pd.DataFrame(most_positive_tweet,columns=["Tweets"])
MostPositiveSentence.to_csv("TwitterScrapingProject/Search/MostPositiveSentence.csv")

#########

data_negative_tweets = pd.read_csv("TwitterScrapingProject/Search/NegativeSentence.csv")
data_negative_column = data_negative_tweets["Tweets"]
most_negative_tweet = most(data_negative_column,column_name_negative)  

MostNegativeSentence = pd.DataFrame(most_negative_tweet,columns=["Tweets"])
MostNegativeSentence.to_csv("TwitterScrapingProject/Search/MostNegativeSentence.csv")"""