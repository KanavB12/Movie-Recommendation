import numpy as np
import pandas as pd
from flask import Flask, render_template, request

# Libraries for making count matrix and similarity matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Function that creates a similarity matrix
def create_sim():
    data = pd.read_csv('data.csv')
    count = CountVectorizer()
    count_matrix = count.fit_transform(data['bag_of_words'])
    sim = cosine_similarity(count_matrix)
    return data, sim


# Function that recommends 10 most similar movies / Web series
def rcmd(title):
    title = title.lower()
    data, sim = create_sim()

    # Check if the movie is in our database or not
    if title not in data['title'].unique():
        str = "This movie is not in our database :(.\nPlease check if you spelled it correctly."
        return str
    else:
        index = data.loc[data['title'] == title].index[0]
        lst = list(enumerate(sim[index]))
        lst = sorted(lst, key=lambda x: x[1], reverse=True)
        lst = lst[1:11]

        content = []
        for i in range(len(lst)):
            a = lst[i][0]
            content.append(data['title'][a])

        return content


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/recommend")
def recommend():
    movie = request.args.get('movie')
    r = rcmd(movie)
    movie = movie.upper()
    if isinstance(r, str):
        return render_template('recommend.html', movie=movie, r=r, t='s')
    else:
        return render_template('recommend.html', movie=movie, r=r, t='l')


if __name__ == '__main__':
    app.run()