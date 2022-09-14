"""Seed database with sample data."""

from app import db
from models import Image

db.drop_all()
db.create_all()

i1 = Image(
    filename="test_lighthouse.jpg",
    published=True
)

i2 = Image(
    filename="Homepage.jpg",
    published=True
)

db.session.add_all([i1, i2])
db.session.commit()
