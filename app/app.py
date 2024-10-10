# app.py
import streamlit as st
import pickle
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from IPython.display import IFrame
import unicodedata
import config

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=config.client_id,
                                                            client_secret=config.client_secret))

# Load data and models
def load_data():
    file_path = os.path.join(os.path.dirname(__file__), 'playlist5000_final.csv')
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        raise

@st.cache_resource()
def load_model():
    return joblib.load('kmeans_model.pkl')

@st.cache_resource()
def load_scaler():
    return joblib.load('scaler.pkl')

# Global objects
cache = {}
df = load_data()
scaler = load_scaler()
kmeans = load_model()

# Function to get audio features from Spotify
def get_audio_features(song_name, limit=1, market="DE"):
    normalized_name = unicodedata.normalize('NFKC', song_name).lower()
    
    if normalized_name in cache:
        return cache[normalized_name]

    result = sp.search(q=song_name, limit=1, market=market)
    if result["tracks"]["items"]:
        song_id = result["tracks"]["items"][0]["id"]
        features = sp.audio_features(song_id)
        cache[normalized_name] = (features, song_id, result)
        return features, song_id, result
    else:
        return None, None, None

# Bring song with Spotify IFrame
def bring_song(song_name):
    features, song_id, result = get_audio_features(song_name)
    view = IFrame(src="https://open.spotify.com/embed/track/"+song_id,
                    width="320", height="80", frameborder="0", allowtransparency="true",
                    allow="encrypted-media")
    return view

# Classify song
def classify_song(song_name):
    features, song_id, result = get_audio_features(song_name)
    X = pd.DataFrame(features)
    X = X[['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness',
            'liveness', 'valence', 'tempo', 'duration_ms']]
    scaled_X = scaler.transform(X)   
    predicted_cluster = kmeans.predict(scaled_X)[0]
    return predicted_cluster

# Song recommender function
def song_recommender(classification, random_state = 42):
    same_cluster_songs = df.loc[df['cluster'] == classification]
    random_sample = same_cluster_songs.sample(n=1, random_state=random_state)
    recommended_song_name = random_sample['names'].values[0]
    recommended_song_id = random_sample['id'].values[0]
    view = IFrame(
        src=f"https://open.spotify.com/embed/track/{recommended_song_id}",
        width="320", height="80", frameborder="0", allowtransparency="true",
        allow="encrypted-media"
    )
    return view

# MusicMaster App into a function
def music_master():
    st.title("MusicMaster")
    st.markdown("### Welcome to the Music Recommendation App!")
    st.markdown("This application is designed to recommend you songs based on your selected tracks.")

    song_name = st.text_input("Insert the name of a song:")
    
    if song_name:
        st.write("### Selected Song:")
        st.components.v1.html(bring_song(song_name)._repr_html_(), height=100)
        
        classification = classify_song(song_name)
        st.write(f"Predicted Cluster: {classification}")
        
        st.write("### Recommended Song:")
        st.components.v1.html(song_recommender(classification)._repr_html_(), height=100)