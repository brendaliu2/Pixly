"""Seed database with sample data."""

from app import db
from models import UserImage

db.drop_all()
db.create_all()

i1 = UserImage(
    filename="test_lighthouse.jpg",
    published=True,
    content_type="image/jpeg"
)

i2 = UserImage(
    filename="Homepage.jpg",
    published=True,
    content_type="image/jpeg"
    
)

db.session.add_all([i1, i2])
db.session.commit()
