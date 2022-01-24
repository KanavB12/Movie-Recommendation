# Movie-Recommendation

Goal was to use NLP to make a content-based recommendation system which shows 10 most related movies/TV shows to the movie you entered. Try it - https://netflix-movies-recommendation.herokuapp.com/.

Dataset Link - https://www.kaggle.com/shivamb/netflix-shows

Dataset used contains approx 6000 entries of different movies released from 1925-2020 but added to neflix in the period 2008-2020.

## Did Exploaratory data analysis on the Dataset - 

![](Images/Content_release_over_years.png)

![](Images/Content_type.png)

![](Images/Country.png)

![](Images/Duration.png)

## Recommendation system - 

Used Count Vectorizer and Cosine similarity to find 10 most related movies to any movie in this dataset.

![](Images/Recommendations.png)

## Deployment
Used Flask Framework and Heroku to deploy this recommendation system on the web.
