import sys
import os
from flask import Flask

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')
    
    from .routes import main
    app.register_blueprint(main)

    return app