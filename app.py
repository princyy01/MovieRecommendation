from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html', movie_titles=movies['title'].values)

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    selected_movie_name = request.form['movie']
    recommendations = recommend(selected_movie_name)
    return render_template('index.html', movie_titles=movies['title'].values, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
