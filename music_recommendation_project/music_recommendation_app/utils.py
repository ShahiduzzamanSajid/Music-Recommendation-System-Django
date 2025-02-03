import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess data
music_data = pd.read_csv("data/data.csv")
number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']

# Normalize and scale the song data
min_max_scaler = MinMaxScaler()
standard_scaler = StandardScaler()
normalized_data = min_max_scaler.fit_transform(music_data[number_cols])
scaled_normalized_data = standard_scaler.fit_transform(normalized_data)

def get_song_data(name, data):
    try:
        song_data = data[data['name'].str.lower() == name.lower()].iloc[0]
        return song_data
    except IndexError:
        return None

def get_mean_vector(song_list, data):
    song_vectors = []
    for song in song_list:
        song_data = get_song_data(song['name'], data)
        if song_data is None:
            print('Warning: {} does not exist in the dataset'.format(song['name']))
            continue
        song_vector = song_data[number_cols].values
        song_vectors.append(song_vector)
    if not song_vectors:
        return None
    song_matrix = np.array(song_vectors)
    return np.mean(song_matrix, axis=0)

def recommend_songs(seed_songs, data, n_recommendations=10):
    metadata_cols = ['name', 'artists', 'year']
    song_center = get_mean_vector(seed_songs, data)
    if song_center is None:
        return []
    normalized_song_center = min_max_scaler.transform([song_center])
    scaled_normalized_song_center = standard_scaler.transform(normalized_song_center)
    similarities = cosine_similarity(scaled_normalized_song_center, scaled_normalized_data)[0]
    indices = np.argsort(similarities)[-n_recommendations:][::-1]
    rec_songs = []
    for i in indices:
        song_name = data.iloc[i]['name']
        if song_name.lower() not in [song['name'].lower() for song in seed_songs]:
            rec_songs.append(data.iloc[i])
            if len(rec_songs) == n_recommendations:
                break
    return rec_songs