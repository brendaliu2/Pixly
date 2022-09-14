from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Image(db.Model):
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

    blackandwhite = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )
    
    sepia = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )
    
    downsized = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )
    
    border = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )
    
    exifdata = db.Column(
        db.String,
        nullable=True
    )

    # tags = db.Column(
    #     db.Boolean,
    #     nullable=False,
    #     default=False
    # )



def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

