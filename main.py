import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
   response =  requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4a49c148bd35050046aa5a622a5386a0'.format(movie_id))
   data = response.json()
   return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommend_movies = []
    recommend_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].id

        recommend_movies.append(movies.iloc[i[0]].title)
        # poster fetch from API
        recommend_movies_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)
st.title('movies recommender system')
selected_movie_name = st.selectbox('How would you like to be contacted?', movies['title'].values)
if st.button('Recommend'):
   names, posters =  recommend(selected_movie_name)
   col1, col2, col3, col4, col5,col6, col7, col8, col9, col10 = st.columns(10)
   with col1:
       st.text(names[0])
       st.image(posters[0])
   with col2:
       st.text(names[1])
       st.image(posters[1])
   with col3:
       st.text(names[2])
       st.image(posters[2])
   with col4:
       st.text(names[3])
       st.image(posters[3])
   with col5:
       st.text(names[4])
       st.image(posters[4])
   with col6:
       st.text(names[5])
       st.image(posters[5])
   with col7:
       st.text(names[6])
       st.image(posters[6])
   with col8:
       st.text(names[7])
       st.image(posters[7])
   with col9:
       st.text(names[8])
       st.image(posters[8])
   with col10:
       st.text(names[9])
       st.image(posters[9])