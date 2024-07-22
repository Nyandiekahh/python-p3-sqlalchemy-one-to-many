# lib/debug.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Game, Review

# Create an engine and a session
engine = create_engine('sqlite:///../lib/one_to_many.db')  # Ensure the correct path to your database
Session = sessionmaker(bind=engine)
session = Session()

# Query the database
games_count = session.query(Game).count()
print(f"Number of games in the database: {games_count}")

first_game = session.query(Game).first()
print(f"First game: {first_game}")

reviews_count = session.query(Review).count()
print(f"Number of reviews in the database: {reviews_count}")

first_review = session.query(Review).first()
print(f"First review: {first_review}")

# Accessing related data
if first_review:
    print(f"First review's game: {first_review.game}")

if first_game:
    print(f"First game's reviews: {first_game.reviews}")
