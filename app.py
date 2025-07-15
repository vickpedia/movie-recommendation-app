import streamlit as st
import pickle
import pandas as pd

# --- Load Data ---
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# --- Poster Placeholder ---
def fetch_poster(movie_id):
    return "https://via.placeholder.com/300x450?text=No+Poster"

# --- Description Placeholder ---
def fetch_description(title):
    return "Description not available. (Connect TMDb API to fetch real overview.)"

# --- Rating Placeholder ---
def fetch_rating(title):
    return "⭐ 7.0/10"

# --- Recommendation Logic ---
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    posters = []
    descriptions = []
    ratings = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        posters.append(fetch_poster(movie_id))
        descriptions.append(fetch_description(title))
        ratings.append(fetch_rating(title))

    return recommended_movies, posters, descriptions, ratings

# --- Streamlit Page Setup ---
st.set_page_config(page_title="Movie Recommender", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
    body {
        background-color: #0f0f0f;
    }
    h1, h2 {
        color: #ff4b4b;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    }
    .movie-title {
        font-weight: bold;
        font-size: 16px;
        margin-top: 5px;
    }
    .movie-meta {
        font-size: 14px;
        color: #999999;
    }
    .desc {
        font-size: 12px;
        color: #cccccc;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h1>🎬 Movie Recommendation System</h1>", unsafe_allow_html=True)
selected_movie = st.selectbox("Choose a movie", movies['title'].values)

# --- Recommendation Output ---
if st.button("🔍 Recommend"):
    names, posters, descs, ratings = recommend(selected_movie)

    st.markdown("<h2>✨ Top 5 Recommendations</h2>", unsafe_allow_html=True)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(posters[i], use_container_width=True)
            st.markdown(f"<div class='movie-title'>{names[i]}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='movie-meta'>{ratings[i]}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='desc'>{descs[i]}</div>", unsafe_allow_html=True)
