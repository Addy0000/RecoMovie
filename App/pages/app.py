import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('pages/Assets/movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('pages/Assets/similarities.pkl', 'rb'))


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    rec_movies = []

    for i in movies_list:
        rec_movies.append(movies.iloc[i[0]].title)

    return rec_movies


st.title('Movie Recommender')

movie_name = st.selectbox('bruh', movies['title'])
st.write('You selected:', movie_name)

if st.button('Recommend'):
    recommendations = recommend(movie_name)
    for rec in recommendations:
        st.write(rec)
