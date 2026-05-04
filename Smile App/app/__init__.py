from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# TODO: (milestone 3) import LoginManager and Moment extensions here
from flask_login import LoginManager
from flask_moment import Moment
moment = Moment()

db = SQLAlchemy()
# TODO: (milestone 3) create LoginManager object and configure the login view as 'auth.login', i.e, `login` route in `auth` Blueprint. 
login = LoginManager()
login.login_view = 'auth.login'
# TODO: (milestone 3) create Moment object
migrate = Migrate()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.static_folder = config_class.STATIC_FOLDER
    app.template_folder = config_class.TEMPLATE_FOLDER_MAIN

    db.init_app(app)
    migrate.init_app(app,db)
    # TODO: (milestone 3) Configure the app object for login using `init_app` function. 
    login.init_app(app)
    # TODO: (milestone 3) Configure the app object for moment using `init_app` function. 
    moment.init_app(app)
    
    # blueprint registration
    from app.main import main_blueprint as main
    main.template_folder = Config.TEMPLATE_FOLDER_MAIN
    app.register_blueprint(main)

    from app.auth import auth_blueprint as auth
    auth.template_folder = Config.TEMPLATE_FOLDER_AUTH
    app.register_blueprint(auth)

    from app.errors import error_blueprint as errors
    errors.template_folder = Config.TEMPLATE_FOLDER_ERRORS
    app.register_blueprint(errors)

    return app
