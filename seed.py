"""Seed database with sample data."""

from app import db
from models import #TODO:

db.drop_all()
db.create_all()

#TODO: SEED DATA HERE

# with open('generator/users.csv') as users:
#     db.session.bulk_insert_mappings(User, DictReader(users))

# with open('generator/messages.csv') as messages:
#     db.session.bulk_insert_mappings(Message, DictReader(messages))

# with open('generator/follows.csv') as follows:
#     db.session.bulk_insert_mappings(Follows, DictReader(follows))

db.session.commit()