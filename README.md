## Introduction

This project demonstrates the use of a content-based filtering method to build a movie recommendation system. The model processes data from the TMDB 5000 movies dataset and the TMDB 5000 credits dataset.
The recommendation system suggests movies based on the similarity of their descriptions, genres, keywords, cast, and crew.

## Dataset

The datasets used in this project are:
- [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- [TMDB 5000 Credits Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

These datasets contain information about movies, including their budget, genres, cast, crew, and more.

## Model Architecture

The recommendation system is built using the following steps:
1. **Data Preprocessing**: Merging the movies and credits datasets, removing unnecessary columns, and handling missing values.
2. **Feature Extraction**: Extracting and transforming features such as genres, keywords, cast, and crew.
3. **Text Vectorization**: Converting the text data into numerical vectors using the CountVectorizer from scikit-learn.
4. **Cosine Similarity**: Calculating the cosine similarity between the movie vectors to determine their similarity.
5. **Recommendation Function**: Implementing a function to recommend movies based on a given movie title.
