from django.shortcuts import render, redirect
from .forms import SeedSongsForm
from .utils import recommend_songs
import pandas as pd
from .models import Recommendation

def index(request):
    if request.method == 'POST':
        form = SeedSongsForm(request.POST)
        if form.is_valid():
            seed_songs = form.cleaned_data['seed_songs']
            n_recommendations = form.cleaned_data['n_recommendations']
            
            # Load music data
            music_data = pd.read_csv("data/data.csv")
            
            # Get recommendations
            seed_songs_list = [{'name': song.strip()} for song in seed_songs.split(',')]
            recommendations = recommend_songs(seed_songs_list, music_data, n_recommendations)
            
            # Save recommendations to the database
            Recommendation.objects.create(
                seed_songs=seed_songs,
                recommended_songs=str(recommendations)
            )
            
            return render(request, 'music_recommendation_app/recommendations.html', {'recommendations': recommendations})
    else:
        form = SeedSongsForm()
    return render(request, 'music_recommendation_app/index.html', {'form': form})