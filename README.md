# Movie Recommender (Django Project)

This project is based on [this EDX course from IBM](https://www.edx.org/learn/django/ibm-guided-project-build-a-movie-recommender-with-django?index=product&queryID=fe6e9f50cedf1278c45d9536ce6f2874&position=1&results_level=first-level-results&term=Guided+Project%3A+Build+a+Movie+Recommender+with+Django&objectID=course-94fa0a80-8657-43b7-8fbe-6bacc69b4712&campaign=Guided+Project%3A+Build+a+Movie+Recommender+with+Django&source=edX&product_category=course&placement_url=https%3A%2F%2Fwww.edx.org%2Fsearch). Jaccard Similarity is used to recommend movies based on previous watch history.

#### Follow these steps to run the project:

- **Setup Project**
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt 
```

- **Prepare Database**
```
python manage.py makemigrations
python manage.py migrate
python3 manage.py load_movies --path movies.csv
```

- **Create Admin/Superuser**
```
python manage.py createsuperuser
```

- **Start Server**
```
python manage.py runserver
```

- **Login to Admin panel and update some movie as watched**
- **Then generate the recommendation by running the following command**
```
python manage.py make_recommendations
```
