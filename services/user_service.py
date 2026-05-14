from models import User
from database import db

def get_all_users():

    users = User.query.all()

    return [
        user.to_dict()
        for user in users
    ]