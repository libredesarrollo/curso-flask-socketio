
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

#@socketio.on('chat')
@login_required
def chat(message):    
    #0/0
    print("Estamos en evento ")
    emit('chat', message['message'], broadcast=True, to=message['room'])

socketio.on_event('chat',chat, namespace='/chat')

@socketio.on('join', namespace='/chat')
@login_required
def join(room):
    username=current_user.name   
    print("Join")
    join_room(room['room'])
    addRoomSession(room['room'])
    emit('join', username+" se unio a la habitacion "+room['room'], to=room['room'], namespace='/chat')

@socketio.on('leave', namespace='/chat')
@login_required
def leave(room):
    username=current_user.name   
    print("leave")
    leave_room(room['room'])
    removeRoomSession(room['room'])
    emit('leave', username+" se unio a la habitacion "+room['room'], to=room['room'], namespace='/otro')

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