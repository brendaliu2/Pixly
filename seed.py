"""Seed database with sample data."""

"""NOTE: Seed images cannot be uploaded directly to 
bucket because they will lose content_type."""

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
    filename="test_snake.png",
    published=True,
    content_type="image/png"
)




db.session.add_all([i1, i2])
db.session.commit()
