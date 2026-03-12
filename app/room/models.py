# Room specific models (currently using strings for rooms in MessageRoom)
# If you want to manage rooms with more metadata (e.g., owner, description), 
# you can define a Room model here.

from app import db

# Example:
# class Room(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), unique=True)
#     description = db.Column(db.String(255))
