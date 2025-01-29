from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from app.models import Movie, Screening, Seat
from app.routes.utils import token_required

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@token_required
def index():
    """
    Render the main page with the list of movies.
    """
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@main_bp.route('/movie/<int:movie_id>')
@token_required
def book_movie(movie_id):
    """
    Render the booking page for a specific movie.
    """
    screenings = Screening.query.filter_by(movie_id=movie_id).all()
    return render_template('booking.html', screenings=screenings)

@main_bp.route('/login')
def login_page():
    return render_template('login.html')

@main_bp.route('/register')
def register_page():
    return render_template('register.html')
