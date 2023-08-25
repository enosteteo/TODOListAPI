from flask import Flask,url_for
from flask_login import LoginManager

from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_mapping(config_class.config)

    # flask extensions
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from app.users.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix="/users")
    
    from app.tasks import bp as tasks_bp
    app.register_blueprint(tasks_bp, url_prefix="/tasks")
    
    from app.auth.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")
    
    @app.route("/test/")
    def test():
        return "<h1>Test Page</h1>"
    
    with app.app_context():
        db.create_all()
    
    return app