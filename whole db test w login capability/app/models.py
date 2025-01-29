from app import db  # Import db from app/__init__.py

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)  # Primary key for the movie
    title = db.Column(db.String(255), nullable=False)  # Title of the movie
    description = db.Column(db.Text, nullable=True)  # Description of the movie
    poster_url = db.Column(db.String(255), nullable=True)  # URL for the movie's poster
    api_id = db.Column(db.String(255), unique=True, nullable=False)  # TMDb API ID for the movie

    def __init__(self, title, description, poster_url, api_id):
        self.title = title
        self.description = description
        self.poster_url = poster_url
        self.api_id = api_id

    def __repr__(self):
        return f"<Movie {self.title}>"

