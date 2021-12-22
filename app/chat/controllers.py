
from flask import Blueprint,render_template

from flask_socketio import emit
from flask_login import login_required, current_user

from app import db, socketio

from app.user.models import User
from app.chat.models import MessageRoom

from datetime import datetime

chatBp = Blueprint('chat',__name__)

@chatBp.route("/normal_chat")
@chatBp.route("/normal_chat/<string:room>")
@login_required
def index(room='default'):
    messageRoom = MessageRoom.query.filter_by(room=room).all()
    return render_template("chat/index.html",messages = messageRoom, room=room)

@socketio.on('chat')
@login_required
def event(message):

    #message['user'] = "andres"
    message['created_at'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    message['user'] ={
        'username': current_user.username,
        'id': current_user.id,
    }

    messageRoom = MessageRoom()
    messageRoom.message = message['message']
    messageRoom.user_id = current_user.id
    messageRoom.room = message['room']

    db.session.add(messageRoom)
    db.session.commit()
    
    print("Estamos en evento "+str(message))
    emit('chat', messageRoom.as_dict(), broadcast=True)

@socketio.on('event')
@login_required
def event(name,surname):
    print("Estamos en evento "+str(name)+" "+surname)
    emit('event', name, broadcast=True)

@socketio.on('event_json')
@login_required
def event(json, n):
    print("Estamos en evento "+str(json), n)
    emit('event', json, broadcast=True)
