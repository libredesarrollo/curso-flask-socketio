from app import db

from datetime import datetime

class MessageRoom(db.Model):
    __tablename__="messages_room"
    id=db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at=db.Column(db.DateTime, default=datetime.utcnow)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    message=db.Column(db.String(500))
    room=db.Column(db.String(10))

    user = db.relationship('User')

    def as_dict(self):
        return {
            'id':self.id,
            'user_id':self.user_id,
            'updated_at':self.updated_at.strftime("%d/%m/%Y %H:%M:%S"),
            'created_at':self.created_at.strftime("%d/%m/%Y %H:%M:%S"),
            'message':self.message,
            'room':self.room,
            'username': self.user.username
        }

    def __str__(self):
        return self.message