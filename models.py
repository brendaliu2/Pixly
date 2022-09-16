from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserImage(db.Model):
    """Image."""

    __tablename__ = "images"

    filename = db.Column(
        db.String,
        primary_key=True
    )

    published = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )
    
    filter = db.Column(
        db.String,
        nullable=False,
        default='none'
    )

    description = db.Column(
        db.String,
        nullable=True
    )
    
    content_type = db.Column(
        db.String,
        nullable=False
    )
    
    exifdata = db.Column(
        db.String,
        nullable=True
    )


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

