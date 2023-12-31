import pandas as pd
import numpy as np

credit = pd.read_csv("/content/drive/MyDrive/tmdb_5000_credits.csv")
movies = pd.read_csv("/content/drive/MyDrive/tmdb_5000_movies.csv")
movies.head(1)

credit.head()

credit.head(1)['cast'].values

movies = movies.merge(credit, on="title")
movies

movies.shape

credit.shape

movies.head(1)

movies.info()

#data preprocessing:-
#genres
#id
#keywords
#title
#overview
#release_date
#revenue
#cast
#crew

movies = movies[['id','genres','keywords','title','overview','release_date','revenue','cast','crew']]
 movies

movies.head()

movies.isnull().sum()

movies.dropna(inplace=True)

movies.duplicated().sum()

movies = movies.drop_duplicates()

movies.duplicated().sum()

movies.iloc[0].genres

def convert(obj):
  L = []
  for i in ast.literal_eval(obj):
    L.append(i['name'])
  return L

import ast

movies['genres'] = movies['genres'].apply(convert)

movies.head()

movies['keywords'] = movies['keywords'].apply(convert)

movies.head()

def convert3(obj):
  L = []
  counter = 0
  for i in ast.literal_eval(obj):
    if counter !=3:
      L.append(i['name'])
      counter+=1
    else:
      break
  return L

movies['cast'] = movies['cast'].apply(convert3)

movies.info()

movies.head()

def fetch_director(obj):
   L =[]
   for i in ast.literal_eval(obj):
     if i['job'] == 'Director':
        L.append(i['name'])
        break
   return L

movies['crew'] = movies['crew'].apply(fetch_director)

movies.head()

movies['overview'] = movies['overview'].apply(lambda x:x.split())

movies.head()

movies['overview']

# convert "Sam worthington" to "samworthington"

movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])

movies.head()

movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies.head()

movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies.head()

movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x] )

movies.head()

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords']+movies["cast"]+movies["crew"]

movies.head()

movies['tags'].info

new_df = movies[['id','title','tags']]
new_df

new_df['tags'] = new_df['tags'].apply(lambda x:" ".join(x))

new_df['tags']

new_df.head()

pip install nltk #it is used for remove the similar words like: activity, activities, love, loves etc

import nltk

from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem(text):
  y = []
  for i in text.split():
    y.append(ps.stem(i))
  return " ".join(y)

new_df['tags'] = new_df['tags'].apply(stem)

new_df['tags']

new_df['tags'][0]

new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())

new_df['tags'][0]

new_df.head()

new_df['tags'][1]

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000,stop_words="english")

vectors = cv.fit_transform(new_df['tags']).toarray()

vectors

vectors[0]

cv.get_feature_names_out()

ps.stem("loving")

stem("in the 22nd century, a paraplegic marine is dispatched to the moon pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization. action adventure fantasy sciencefiction cultureclash future spacewar spacecolony society spacetravel futuristic romance space alien tribe alienplanet cgi marine soldier battle loveaffair antiwar powerrelations mindandsoul 3d samworthington zoesaldana sigourneyweaver jamescameron")

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)

similarity

#sorted(similarity[0], reverse = True)
sorted(list(enumerate(similarity[0])), reverse = True, key = lambda x:x[1])[1:6]

def recommend(movie):
  movie_index = new_df[new_df['title'] == movie].index[0]
  distances = similarity[movie_index]
  movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:5]
  for i in movies_list:
    print(new_df.iloc[i[0]].title)

recommend('Batman Begins')

new_df.iloc[1216].title

import pickle

pickle.dump(new_df, open('movies.pkl','wb'))

import gc
import pickle
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

pick_insert = open('drive/My Drive/movies.pkl','wb')
pickle.dump(new_df, pick_insert)
pick_insert.close()

pick_read = open('drive/My Drive/movies.pkl','rb')
data = pickle.load(pick_read)
pick_read.close()

new_df['title'].values

pickle.dump(new_df.to_dict(), open('movie_dict.pkl','wb'))

import gc
import pickle
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

pick_insert = open('drive/My Drive/movie_dict.pkl','wb')
pickle.dump(new_df, pick_insert)
pick_insert.close()

pick_read = open('drive/My Drive/movie_dict.pkl','rb')
data = pickle.load(pick_read)
pick_read.close()

pickle.dump(similarity, open('similarity.pkl', 'wb'))

import gc
import pickle
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

pick_insert = open('drive/My Drive/similarity.pkl','wb')
pickle.dump(new_df, pick_insert)
pick_insert.close()

pick_read = open('drive/My Drive/similarity.pkl','rb')
data = pickle.load(pick_read)
pick_read.close()

