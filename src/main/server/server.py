from flask import Flask
from src.main.routes.tagRoutes import tagsRoutesBp
app = Flask(__name__)
app.register_blueprint(tagsRoutesBp)