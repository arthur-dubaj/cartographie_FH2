# app.py
from flask import Flask
import os

# 1) On crée le serveur Flask ici
server = Flask(__name__)
server.secret_key = os.environ.get("SECRET_KEY", "dev")
# 2) On charge les routes Flask
import app.routes as routes   # <-- routes voit déjà "server"


# 3) On charge l’application Dash
from app.main import app  # <-- dash_app reçoit server sans circular import

