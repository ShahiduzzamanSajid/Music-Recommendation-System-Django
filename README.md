## Music-Recommendation-System-Django


## Project Overview
The Music Recommendation System project is designed to enhance music exploration and discovery by leveraging data-driven insights and machine-learning techniques. This project is a web-based music recommendation system built using Django. It uses machine learning techniques to recommend songs based on user preferences. The system analyzes features like danceability, energy, and tempo to provide personalized song recommendations.

  
 **Song Recommendations :**

- **Recommend Songs :** Users can input their favorite songs as seed songs, and the system will generate a list of similar songs based on attributes such as valence, acoustics, and danceability.


# Libraries and Tools Used

- **Django :** Web framework for building the application.
- **Pandas :** A data manipulation and analysis library for Python.
- **NumPy :** A library for numerical operations in Python.
- **Plotly :** A library for interactive data visualizations and charts.
- **Matplotlib :** A library for creating static plots.
- **WordCloud :** A library for generating word clouds from text data.
- **Scipy :** A library for scientific computing, including spatial distance calculations.
- **Scikit-Learn :** A machine learning library for Python, used for preprocessing data and calculating similarity.
- **SQLite :** Database for storing user preferences and recommendations.
- **Features Used :**
  - **MinMaxScaler :** Normalizes features to a range between 0 and 1.
  - **StandardScaler :** Standardizes features by removing the mean and scaling to unit variance.
  - **Cosine Similarity :** Measures the cosine of the angle between two non-zero vectors.

## Installation Instructions
To get a local copy of the project up and running, follow these simple steps:

**1. Clone the Repository :**

   ```bash
   git clone https://github.com/ShahiduzzamanSajid/Interactive-Music-Recommendation-and-Visualization-System.git
   cd Interactive-Music-Recommendation-and-Visualization-System
```

**2. Install the Required Libraries :**

To install all the necessary libraries and dependencies for the project, you can use the following commands:

```bash
pip install pandas
pip install numpy
pip install plotly
pip install matplotlib
pip install wordcloud
pip install scipy
pip install scikit-learn
pip install imbalanced-learn
```

**3. Set Up the Database :**

```bash
python manage.py makemigrations
python manage.py migrate
```

**4. Run the Server :**

```bash
python manage.py runserver
```

## Contributing
Contributions to improve Real-Time Spam ham Detection are welcome. To contribute, follow these steps :

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them with clear comments.
4. Push your changes to your fork.
5. Open a pull request, explaining the changes made.

## License
This project is licensed under the MIT License.

