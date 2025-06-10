import streamlit as st
import pickle
import pandas as pd
import os
import gdown


@st.cache_resource
def load_data():
    # Replace these with your actual Google Drive file IDs
    movies_file_id = "1-ynEv9lDHMz2gy8we54y2jp0fMPAx8Em"
    similarity_file_id = "1hJkiUcAy9hrK2aV6bpzjbOcUcniGmTeT"

    if not os.path.exists("movies.pkl"):
        gdown.download(f"https://drive.google.com/uc?id={movies_file_id}", "movies.pkl", quiet=False)

    if not os.path.exists("similarity.pkl"):
        gdown.download(f"https://drive.google.com/uc?id={similarity_file_id}", "similarity.pkl", quiet=False)

    with open("movies.pkl", "rb") as f:
        movies_df = pickle.load(f)

    with open("similarity.pkl", "rb") as f:
        similarity = pickle.load(f)

    return movies_df, similarity


# Load data
movies_df, similarity = load_data()
movies = movies_df['title'].values


# Recommendation function
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies


# Streamlit UI
st.title('Movie Recommender System')
selected_movie = st.selectbox('Pick a movie', movies)

if st.button('Recommend'):
    recommended_movies = recommend(selected_movie)
    for i in recommended_movies:
        st.write(i)
