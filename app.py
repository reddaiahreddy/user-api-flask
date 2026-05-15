import os
from flask import Flask

from database import db
from routes.user_routes import user_bp


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db.init_app(app)

app.register_blueprint(
    user_bp
)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(
    host="0.0.0.0",
    port=5000,
    debug=os.getenv("DEBUG", "False") == "True"
)