import os
from flask import Flask

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'reconbot.sqlite')
    )
    
    if test_config is None:
        # Load the instance config when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load a test config
        app.config.from_mapping(test_config)

    # Ensure the instance directory exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import db, auth
    db.init_app(app)
    app.register_blueprint(auth.bp)

    @app.route('/')
    def hello():
        ret = "<a href='" + str(app.url_for("auth.register")) + "'>Register</a>"

        return ret

    return app