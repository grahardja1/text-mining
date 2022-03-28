from imdb import Cinemagoer
import re
import string
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer




# create an instance of the Cinemagoer class
ia = Cinemagoer()

# search movie
movie = ia.search_movie("The Godfather")[0]
#print(movie.movieID)


movie_reviews = ia.get_movie_reviews('0068646')
#print(movie_reviews)
#print(movie_reviews['data']['reviews'][0]['content'])
#print(type(movie_reviews ))
#print(type(movie_reviews['data']['reviews'][0]['content']))
reviews = movie_reviews['data']['reviews'][0]['content'] + movie_reviews['data']['reviews'][1]['content'] + movie_reviews['data']['reviews'][2]['content'] + movie_reviews['data']['reviews'][3]['content']   
#print(reviews)


def sentiment_analyis(review):
    score = SentimentIntensityAnalyzer().polarity_scores(review)
    #print(type(score))
   
    print(score)

def count_num_words(reviews):
    "counts total number of words in the review"
    count = 0
    for i in reviews:
        if i == " ":
            count +=1
    return count + 1        

def clean_word_list(reviews):
    "used to remove punctuation and seperates a string into seperate words and converting it to a list of words"
    res = re.sub('['+string.punctuation+']', '', reviews).split()
    
    return res



def count_frequencies(word,list):
    " counts the frequency of word in list"
    count = 0
    for item in list:
        if item == word:
            count+=1
    return count


def get_unique_words(list):
    "returns unique words in a list"
    l = []
    for item in list:
        if item not in l:
            l.append(item)
    return len(l)

def sort(list):
    " input: list"
    "output: sorted list based on frequencies"
    maximum = 0
    l = []
    for item in list:
        if item not in l:
             l.append(item)


    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if count_frequencies(l[i],clean_word_list(reviews)) < count_frequencies(l[j], clean_word_list(reviews)):
                l[i] , l[j] = l[j] , l[i]   

   
    return l

def file_to_list():
    """return a list of words, from stopwords.txt"""
    words = []
    with open('data/stopwords.txt') as f:
        for line in f.readlines():
            words.append(line.strip())
    return words

def remove_stopwords(list):
    "removes stopwords from a given list of words"
    l = file_to_list()
    new_list = []

    for item in list:
        if item not in l:
            new_list.append(item)
    
    return new_list

def most_common(list,n):
    "prints n most common words in a list of words"
    l = sort(remove_stopwords(clean_word_list(reviews)))
    for i in range(n):
        print(f'{l[i]}   {count_frequencies(l[i],clean_word_list(reviews))}')
    
        

        





def main():
   #print(count_num_words(reviews))
   #print(type(clean_word_list(reviews)))
   #print(clean_word_list(reviews)) 
   #print(convert(clean_word_list(reviews)))
   #print(type(clean_word_list(reviews)))
   #clean_word_list(reviews)
   #sentiment_analyis(reviews)
   #most_common(clean_word_list(reviews),6)
   #print(clean_word_list(reviews))
   #print(len(clean_word_list(reviews)))
   #print(get_unique_words(remove_stopwords(clean_word_list(reviews))))
   #print(get_unique_words(clean_word_list(reviews)))    
    #print(remove_stopwords(clean_word_list(reviews)))
   #print(sort(clean_word_list(reviews)))
   #most_common(remove_stopwords(clean_word_list(reviews)),8)
   #print(file_to_list())


   sentiment_analyis(reviews)
   most_common(remove_stopwords(clean_word_list(reviews)),8)
  


  




if __name__ == '__main__':
    main()
