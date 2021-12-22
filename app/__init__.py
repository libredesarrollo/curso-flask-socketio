from flask import Flask
from flask_socketio import SocketIO

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('configuration.DevConfig')

#Configuraciones
socketio = SocketIO(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login_manager = LoginManager(app)

#vistas importaciones
from app.chat.controllers import chatBp
from app.room.controllers import roomBp
from app.user.controllers import userBp
app.register_blueprint(chatBp)
app.register_blueprint(roomBp)
app.register_blueprint(userBp)

