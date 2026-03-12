
from flask import Blueprint, render_template, session

from flask_socketio import emit, join_room, leave_room
from flask_login import login_required, current_user

from app import db, socketio

from app.user.models import User
from app.chat.models import MessageRoom

from datetime import datetime

roomBp = Blueprint('room',__name__)

@roomBp.route("/room")
@login_required
def index():
    rooms = ['room 1','room 2','room 3','room 4']
    return render_template("room/index.html", rooms=rooms)

@login_required
def chat(message):    
    # Preparamos los metadatos para el evento
    message['created_at'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message['user'] = {
        'username': current_user.username,
        'id': current_user.id
    }

    # Persistencia en base de datos
    new_message = MessageRoom()
    new_message.message = message['message']
    new_message.user_id = current_user.id
    new_message.room = message['room']
    
    db.session.add(new_message)
    db.session.commit()

    print(f"Room Event [{new_message.room}]: {new_message.message}")
    # Emitimos el diccionario serializado a la sala específica
    emit('chat', new_message.as_dict(), to=message['room'], namespace='/chat')

socketio.on_event('chat', chat, namespace='/chat')

@socketio.on('join', namespace='/chat')
@login_required
def join(room):
    username = current_user.username   
    print(f"Join: {username} to {room['room']}")
    join_room(room['room'])
    addRoomSession(room['room'])
    emit('join', f"{username} se unió a la habitación {room['room']}", to=room['room'], namespace='/chat')

@socketio.on('leave', namespace='/chat')
@login_required
def leave(room):
    username = current_user.username   
    print(f"Leave: {username} from {room['room']}")
    leave_room(room['room'])
    removeRoomSession(room['room'])
    emit('leave', f"{username} abandonó la habitación {room['room']}", to=room['room'], namespace='/chat')

@socketio.on('connect')
def connect():
    session['rooms'] = []
    print("Conectado!!!!!!!")

@socketio.on('disconnect')
def disconnect():
    session['rooms'] = []
    print("Desconectado!!!!!!!")

@socketio.on_error()
def error_handle(e):
    print("error_handle")

@socketio.on_error("/chat")
def error_handle_ns(e):
    print("error_handle_ns")

def addRoomSession(room):

    if 'rooms' not in session:
        session['rooms'] = []

    rooms = session['rooms']

    rooms.append(room)
    session['rooms'] = rooms

    print(session['rooms'])

def removeRoomSession(room):

    rooms = session['rooms']

    rooms.remove(room)
    session['rooms'] = rooms

    print(session['rooms'])