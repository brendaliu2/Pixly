from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


DEFAULT_IMAGE_URL = "https://static.independent.co.uk/2021/12/03/15/Pisco%20Cat%20puss%20in%20boots-1.jpg?width=1200"
