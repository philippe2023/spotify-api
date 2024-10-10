# Project Overview

This project is a Spotify song recommender application built using Streamlit, Spotipy, and Tableau Public. It allows users to:
- Enter a song name to receive a cluster-based song recommendation using audio features retrieved from the Spotify API.
- View a Tableau dashboard visualization showcasing Spotify-related data.

## Key Features
- Song classification using K-Means Clustering based on song audio features.
- Spotify song recommendations from the same cluster using Spotify’s API.
- Integration of a Tableau Public dashboard for visual insights.

## Technologies Used
- **Python**: Main programming language for the application.
- **Streamlit**: For building the web application.
- **Spotipy**: A lightweight Python library for the Spotify Web API.
- **Pandas**: For data manipulation and analysis.
- **Scikit-learn**: For K-Means clustering model.
- **Pillow (PIL)**: To load and display images in the app.
- **Joblib**: For loading saved machine learning models.
- **Tableau Public**: For creating and displaying visualizations.

## How to Run
1. **Running the Streamlit App**
Run the Streamlit app using the following command:
```bash
streamlit run main.py
```
This will launch the app in your default browser. You can choose between two options from the sidebar:
- MusicMaster: Enter a song and receive a recommendation from the same cluster.
- Visuals: View a Tableau dashboard visualization related to Spotify.
2. **Spotify Song Recommender**
In the MusicMaster section:
- Enter a song name in the input field.
- The app will retrieve the song’s audio features and classify it into a cluster.
- A recommendation from the same cluster will be displayed along with the original song.
3. **Tableau Dashboard Visualization**
In the Visuals section:
- View a static image of the Spotify dashboard created with Tableau Public.
- You can also click a link to view the full interactive Tableau dashboard in a new tab.

## What you would need
- Spotify credential in a config file