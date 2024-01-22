# Movie Recommender (Django Project)

**Setup Project**
```
python -m venv env
source env/bin/activate
pip install -r requirements.txt 
```

**Prepare Database**
```
python manage.py makemigrations
python manage.py migrate
python3 manage.py load_movies --path movies.csv
```