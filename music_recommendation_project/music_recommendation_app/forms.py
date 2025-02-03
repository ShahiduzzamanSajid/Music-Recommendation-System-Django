from django import forms

class SeedSongsForm(forms.Form):
    seed_songs = forms.CharField(label='Seed Songs', widget=forms.Textarea)
    n_recommendations = forms.IntegerField(label='Number of Recommendations', min_value=1, max_value=20, initial=10)